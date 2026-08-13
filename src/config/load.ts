import { readFile } from "node:fs/promises";
import { parse } from "yaml";
import { parseConfig, type RadarConfig } from "./schema.js";

export async function loadConfig(path = "config.yml"): Promise<RadarConfig> {
  let source: string;
  try {
    source = await readFile(path, "utf8");
  } catch (error) {
    throw new Error(`Unable to read config file ${path}`, { cause: error });
  }

  try {
    return parseConfig(parse(source));
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    throw new Error(`Unable to load ${path}: ${message}`, { cause: error });
  }
}
