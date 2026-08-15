/* Sort the static comparison table without changing or fetching its factual rows. */

const comparisonTable = document.querySelector("#project-comparison");

if (comparisonTable) {
  const body = comparisonTable.querySelector("tbody");
  const buttons = [...comparisonTable.querySelectorAll("[data-sort-key]")];
  const status = document.querySelector("#comparison-sort-status");
  const collator = new Intl.Collator(undefined, { numeric: true, sensitivity: "base" });
  let activeKey = "";
  let activeDirection = "ascending";

  function sortValue(row, index, type) {
    const raw = row.cells[index]?.dataset.sortValue ?? "";
    if (raw === "") return null;
    return type === "number" ? Number(raw) : raw;
  }

  for (const button of buttons) {
    button.addEventListener("click", () => {
      if (!body) return;
      const key = button.dataset.sortKey ?? "";
      const index = Number(button.dataset.sortIndex ?? 0);
      const type = button.dataset.sortType ?? "text";
      activeDirection = activeKey === key && activeDirection === "ascending" ? "descending" : "ascending";
      activeKey = key;
      const direction = activeDirection === "ascending" ? 1 : -1;
      const rows = [...body.rows];

      rows.sort((left, right) => {
        const leftValue = sortValue(left, index, type);
        const rightValue = sortValue(right, index, type);
        if (leftValue === null && rightValue === null) return 0;
        if (leftValue === null) return 1;
        if (rightValue === null) return -1;
        if (typeof leftValue === "number" && typeof rightValue === "number") {
          return (leftValue - rightValue) * direction;
        }
        return collator.compare(String(leftValue), String(rightValue)) * direction;
      });

      body.replaceChildren(...rows);
      for (const candidate of buttons) {
        candidate.closest("th")?.setAttribute(
          "aria-sort",
          candidate === button ? activeDirection : "none",
        );
      }
      if (status) {
        status.textContent = `Sorted by ${button.textContent?.replace("↕", "").trim()} ${activeDirection}.`;
      }
    });
  }
}
