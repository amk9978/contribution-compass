/* Local-only personalization over the published machine catalog. */

const compass = document.querySelector("#personal-compass");

if (compass) {
  const storageKey = "contribution-compass-projects-v1";
  const checkboxes = [...compass.querySelectorAll("[data-project]")];
  const projectOptions = [...compass.querySelectorAll("[data-project-option]")];
  const knownProjects = new Set(checkboxes.map((checkbox) => checkbox.value));
  const pageSize = 10;
  let opportunities = [];
  let news = [];
  let leadPage = 1;
  let newsPage = 1;

  function safeStoredProjects() {
    try {
      const parsed = JSON.parse(localStorage.getItem(storageKey) ?? "[]");
      return Array.isArray(parsed) ? parsed.filter((item) => knownProjects.has(item)) : [];
    } catch {
      return [];
    }
  }

  function selectedFromUrl() {
    const value = new URLSearchParams(window.location.search).get("projects");
    if (!value) return [];
    return value.split(",").filter((item) => knownProjects.has(item));
  }

  const initial = selectedFromUrl();
  const selected = new Set(initial.length ? initial : safeStoredProjects());

  function element(name, text, className) {
    const node = document.createElement(name);
    if (text !== undefined) node.textContent = text;
    if (className) node.className = className;
    return node;
  }

  function evidenceLink(url, text) {
    const link = element("a", text);
    try {
      const parsed = new URL(url);
      link.href = ["http:", "https:"].includes(parsed.protocol) ? parsed.href : "#";
    } catch {
      link.href = "#";
    }
    link.target = "_blank";
    link.rel = "noreferrer";
    return link;
  }

  function syncSelection() {
    for (const checkbox of checkboxes) checkbox.checked = selected.has(checkbox.value);
    localStorage.setItem(storageKey, JSON.stringify([...selected].sort()));
    const count = compass.querySelector("#profile-selected-count");
    if (count) count.textContent = `${selected.size} selected`;
    const url = new URL(window.location.href);
    if (selected.size) url.searchParams.set("projects", [...selected].sort().join(","));
    else url.searchParams.delete("projects");
    history.replaceState({}, "", url);
    leadPage = 1;
    newsPage = 1;
    render();
  }

  function renderPagination(containerId, total, current, onChange) {
    const container = compass.querySelector(`#${containerId}`);
    if (!container) return;
    container.replaceChildren();
    const pages = Math.max(1, Math.ceil(total / pageSize));
    if (pages <= 1) return;
    const previous = element("button", "← Previous");
    previous.type = "button";
    previous.disabled = current <= 1;
    previous.addEventListener("click", () => onChange(current - 1));
    const status = element("span", `Page ${current} of ${pages}`);
    const next = element("button", "Next →");
    next.type = "button";
    next.disabled = current >= pages;
    next.addEventListener("click", () => onChange(current + 1));
    container.append(previous, status, next);
  }

  function renderLeads() {
    const body = compass.querySelector("#profile-leads");
    const count = compass.querySelector("#profile-lead-count");
    if (!body || !count) return;
    const filtered = opportunities.filter((lead) => selected.has(lead.signal?.project));
    const pages = Math.max(1, Math.ceil(filtered.length / pageSize));
    leadPage = Math.min(leadPage, pages);
    const visible = filtered.slice((leadPage - 1) * pageSize, leadPage * pageSize);
    body.replaceChildren();
    count.textContent = selected.size ? `${filtered.length} matching leads` : "Choose projects to begin";
    if (!visible.length) {
      const row = element("tr");
      const cell = element(
        "td",
        selected.size
          ? "No evidence-qualified leads match the selected projects."
          : "Your selected projects will appear here.",
      );
      cell.colSpan = 4;
      row.append(cell);
      body.append(row);
    }
    for (const lead of visible) {
      const row = element("tr");
      row.append(element("td", lead.signal?.project ?? "Unknown"));
      const opportunity = element("td");
      opportunity.append(evidenceLink(lead.evidenceUrl, lead.signal?.title ?? "Open evidence"));
      const reason = element("td");
      const reasons = Array.isArray(lead.reasons) ? lead.reasons : [];
      reason.append(element("span", reasons.join(" · ")));
      const details = element("details", undefined, "profile-measures");
      details.append(element("summary", "Score breakdown"));
      const list = element("ul");
      for (const measure of lead.measures ?? []) {
        if (!measure.points) continue;
        list.append(element("li", `${measure.points >= 0 ? "+" : ""}${measure.points} ${measure.label}: ${measure.evidence}`));
      }
      details.append(list);
      reason.append(details);
      row.append(reason, element("td", String(lead.rankScore ?? 0), "profile-score"));
      body.append(row);
    }
    renderPagination("profile-lead-pages", filtered.length, leadPage, (page) => {
      leadPage = page;
      renderLeads();
    });
  }

  function renderNews() {
    const body = compass.querySelector("#profile-news");
    const count = compass.querySelector("#profile-news-count");
    if (!body || !count) return;
    const filtered = news.filter((entry) => selected.has(entry.project?.repository));
    const pages = Math.max(1, Math.ceil(filtered.length / pageSize));
    newsPage = Math.min(newsPage, pages);
    const visible = filtered.slice((newsPage - 1) * pageSize, newsPage * pageSize);
    body.replaceChildren();
    count.textContent = selected.size ? `${filtered.length} project snapshots` : "";
    if (!visible.length) {
      const row = element("tr");
      const cell = element(
        "td",
        selected.size ? "No project news is available for this selection." : "News for selected projects will appear here.",
      );
      cell.colSpan = 4;
      row.append(cell);
      body.append(row);
    }
    for (const entry of visible) {
      const row = element("tr");
      row.append(element("td", entry.project?.name ?? entry.project?.repository ?? "Unknown"));
      const releaseCell = element("td");
      const release = entry.news?.latestRelease;
      releaseCell.append(
        release ? evidenceLink(release.url, `${release.title} (${release.tag})`) : element("span", "No stable release found"),
      );
      const upcomingCell = element("td");
      const upcoming = entry.news?.upcoming?.[0];
      upcomingCell.append(
        upcoming ? evidenceLink(upcoming.url, `${upcoming.kind}: ${upcoming.title}`) : element("span", "No supported public item"),
      );
      const discussionCell = element("td");
      const discussion = entry.news?.communityDiscussions?.[0];
      discussionCell.append(
        discussion
          ? evidenceLink(discussion.discussionUrl, `HN · ${discussion.score} points · ${discussion.comments} comments`)
          : element("span", "No matched HN discussion"),
      );
      row.append(releaseCell, upcomingCell, discussionCell);
      body.append(row);
    }
    renderPagination("profile-news-pages", filtered.length, newsPage, (page) => {
      newsPage = page;
      renderNews();
    });
  }

  function render() {
    renderLeads();
    renderNews();
  }

  for (const checkbox of checkboxes) {
    checkbox.addEventListener("change", () => {
      if (checkbox.checked) selected.add(checkbox.value);
      else selected.delete(checkbox.value);
      syncSelection();
    });
  }

  compass.querySelector("#profile-select-all")?.addEventListener("click", () => {
    for (const project of knownProjects) selected.add(project);
    syncSelection();
  });
  compass.querySelector("#profile-clear")?.addEventListener("click", () => {
    selected.clear();
    syncSelection();
  });
  for (const button of compass.querySelectorAll("[data-select-group]")) {
    button.addEventListener("click", () => {
      const group = button.dataset.selectGroup;
      for (const checkbox of compass.querySelectorAll(`[data-profile-group="${CSS.escape(group)}"] [data-project]`)) {
        selected.add(checkbox.value);
      }
      syncSelection();
    });
  }

  compass.querySelector("#profile-project-search")?.addEventListener("input", (event) => {
    const query = event.target.value.trim().toLowerCase();
    for (const option of projectOptions) {
      option.classList.toggle("hidden", Boolean(query) && !(option.dataset.projectSearch ?? "").includes(query));
    }
  });

  compass.querySelector("#profile-match-import")?.addEventListener("click", () => {
    const input = compass.querySelector("#profile-import-text")?.value.toLowerCase() ?? "";
    let matches = 0;
    for (const option of projectOptions) {
      const checkbox = option.querySelector("[data-project]");
      let candidates = [];
      try {
        candidates = JSON.parse(option.dataset.projectAliases ?? "[]")
          .map((value) => String(value).toLowerCase())
          .filter((value) => value.length >= 3);
      } catch {
        candidates = [];
      }
      const slug = checkbox?.value.toLowerCase();
      if (checkbox && (input.includes(slug) || candidates.some((candidate) => input.includes(candidate)))) {
        if (!selected.has(checkbox.value)) matches += 1;
        selected.add(checkbox.value);
      }
    }
    const result = compass.querySelector("#profile-import-result");
    if (result) result.textContent = `${matches} newly matched project${matches === 1 ? "" : "s"}`;
    syncSelection();
  });

  compass.querySelector("#profile-share")?.addEventListener("click", async (event) => {
    const button = event.currentTarget;
    try {
      await navigator.clipboard.writeText(window.location.href);
      button.textContent = "Copied";
    } catch {
      button.textContent = "Copy unavailable";
    }
    window.setTimeout(() => {
      button.textContent = "Copy share link";
    }, 1600);
  });

  syncSelection();
  Promise.all([
    fetch(compass.dataset.opportunitiesUrl).then((response) => response.json()),
    fetch(compass.dataset.newsUrl).then((response) => response.json()),
  ])
    .then(([leadData, newsData]) => {
      opportunities = Array.isArray(leadData.leads) ? leadData.leads : [];
      news = Array.isArray(newsData.projects) ? newsData.projects : [];
      render();
    })
    .catch(() => {
      const count = compass.querySelector("#profile-lead-count");
      if (count) count.textContent = "Published data could not be loaded";
    });
}
