import { cp, mkdir, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { loadSiteModel } from "./load.js";
import type { SiteContext, SiteOptions } from "./model.js";
import { renderDatePage, renderGroupPage, renderHome, renderRepositoryPage } from "./render.js";
import { renderRss, renderSitemap } from "./rss.js";

const sourceDirectory = path.dirname(fileURLToPath(import.meta.url));

function withoutTrailingSlash(value: string): string {
  return value.replace(/\/+$/, "");
}

export function defaultSiteContext(): SiteContext {
  const repository = process.env["GITHUB_REPOSITORY"] ?? "amk9978/engineering-radar";
  const [owner = "amk9978", name = "engineering-radar"] = repository.split("/");
  return {
    siteUrl: withoutTrailingSlash(process.env["SITE_URL"] ?? `https://${owner}.github.io/${name}`),
    repositoryUrl: withoutTrailingSlash(
      process.env["REPOSITORY_URL"] ?? `https://github.com/${repository}`,
    ),
  };
}

async function output(file: string, content: string): Promise<void> {
  await mkdir(path.dirname(file), { recursive: true });
  await writeFile(file, content, "utf8");
}

export async function generateSite(options: SiteOptions = {}): Promise<{
  outputRoot: string;
  dates: number;
  pages: number;
}> {
  const dataRoot = options.dataRoot ?? "data";
  const outputRoot = options.outputRoot ?? ".site";
  const resolvedOutput = path.resolve(outputRoot);
  if (resolvedOutput === path.parse(resolvedOutput).root || resolvedOutput === path.resolve(".")) {
    throw new Error(`Refusing to replace unsafe site output directory: ${resolvedOutput}`);
  }
  const defaults = defaultSiteContext();
  const context: SiteContext = {
    siteUrl: withoutTrailingSlash(options.siteUrl ?? defaults.siteUrl),
    repositoryUrl: withoutTrailingSlash(options.repositoryUrl ?? defaults.repositoryUrl),
  };
  const model = await loadSiteModel(dataRoot);
  let pages = 1;

  await rm(resolvedOutput, { recursive: true, force: true });
  await mkdir(resolvedOutput, { recursive: true });
  await Promise.all([
    output(path.join(outputRoot, "index.html"), renderHome(model, context)),
    output(path.join(outputRoot, "feed.xml"), renderRss(model, context)),
    output(path.join(outputRoot, "sitemap.xml"), renderSitemap(model, context)),
    output(
      path.join(outputRoot, "robots.txt"),
      `User-agent: *\nAllow: /\nSitemap: ${context.siteUrl}/sitemap.xml\n`,
    ),
    output(path.join(outputRoot, ".nojekyll"), ""),
    cp(path.join(sourceDirectory, "assets"), path.join(outputRoot, "assets"), {
      recursive: true,
    }),
  ]);

  for (const date of model.dates) {
    await output(
      path.join(outputRoot, "updates", date.date, "index.html"),
      renderDatePage(date, context),
    );
    pages += 1;
    for (const group of date.groups) {
      await output(
        path.join(outputRoot, "updates", date.date, group.id, "index.html"),
        renderGroupPage(date, group, context),
      );
      pages += 1;
      for (const repository of group.repositories) {
        await output(
          path.join(outputRoot, "updates", date.date, group.id, `${repository.id}.html`),
          renderRepositoryPage(date, group, repository, context),
        );
        pages += 1;
      }
    }
  }

  console.log(`[site] generated ${pages} pages for ${model.dates.length} dates in ${outputRoot}`);
  return { outputRoot, dates: model.dates.length, pages };
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  generateSite().catch((error: unknown) => {
    console.error(`[site] ${error instanceof Error ? error.message : String(error)}`);
    process.exitCode = 1;
  });
}
