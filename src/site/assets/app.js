/* global document, localStorage */

const root = document.documentElement;
const themeToggle = document.querySelector(".theme-toggle");
const storedTheme = localStorage.getItem("engineering-radar-theme");

if (storedTheme === "light" || storedTheme === "dark") {
  root.dataset.theme = storedTheme;
}

themeToggle?.addEventListener("click", () => {
  const theme = root.dataset.theme === "light" ? "dark" : "light";
  root.dataset.theme = theme;
  localStorage.setItem("engineering-radar-theme", theme);
});

const search = document.querySelector("#signal-search");
const filterButtons = [...document.querySelectorAll("[data-filter]")];
const signalCards = [...document.querySelectorAll(".signal-card")];
const count = document.querySelector("#filter-count");
let activeKind = "all";

function applyFilters() {
  const query = search?.value.trim().toLowerCase() ?? "";
  let visible = 0;

  for (const card of signalCards) {
    const kindMatches = activeKind === "all" || card.dataset.kind === activeKind;
    const textMatches = !query || (card.dataset.search ?? "").includes(query);
    const show = kindMatches && textMatches;
    card.classList.toggle("hidden", !show);
    if (show) visible += 1;
  }

  if (count) count.textContent = `${visible} shown`;
}

search?.addEventListener("input", applyFilters);
for (const button of filterButtons) {
  button.addEventListener("click", () => {
    activeKind = button.dataset.filter ?? "all";
    for (const candidate of filterButtons) {
      candidate.classList.toggle("active", candidate === button);
    }
    applyFilters();
  });
}
