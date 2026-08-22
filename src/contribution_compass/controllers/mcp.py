from __future__ import annotations

from mcp.server import MCPServer


def create_server() -> MCPServer:
    server = MCPServer(
        "Contribution Compass",
        instructions=(
            "Contribution Compass v2 is being rebuilt as a personalized OSS investment "
            "recommender. Recommendation tools will be added only after the evidence and "
            "evaluation model passes its validation fixtures."
        ),
        website_url="https://amk9978.github.io/contribution-compass/",
    )

    @server.resource("compass://status", mime_type="application/json")
    def status() -> dict[str, str]:
        return {
            "phase": "v2-rewrite",
            "product": "personalized OSS investment recommender",
            "principle": "project first, issue second",
        }

    return server


mcp = create_server()


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
