from __future__ import annotations

from urllib.parse import urlparse

from jinja2 import Environment, PackageLoader, StrictUndefined, select_autoescape

from contribution_compass.domain.importance import importance_score
from contribution_compass.views.machine import signal_anchor


def safe_url(value: str) -> str:
    """Allow evidence links only through browser-safe HTTP schemes."""
    return value if urlparse(value).scheme in {"http", "https"} else "#"


def compact(value: int) -> str:
    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    if value >= 1_000:
        return f"{value / 1_000:.1f}K"
    return str(value)


def short_date(value: str | None) -> str:
    return value[:10] if value else "date unavailable"


def create_environment() -> Environment:
    """Create the single, strict rendering environment used by every HTML page."""
    environment = Environment(
        loader=PackageLoader("contribution_compass.views", "templates"),
        autoescape=select_autoescape(enabled_extensions=("html", "xml"), default=True),
        undefined=StrictUndefined,
        auto_reload=False,
        keep_trailing_newline=True,
    )
    environment.filters.update(
        {
            "compact": compact,
            "safe_url": safe_url,
            "short_date": short_date,
        }
    )
    environment.globals.update(
        {
            "importance_score": importance_score,
            "signal_anchor": signal_anchor,
        }
    )
    return environment
