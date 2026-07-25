import typer
from rich.console import Console

from graphrecon.browser.browser_manager import BrowserManager
from graphrecon.constants import APP_NAME, VERSION
from graphrecon.events.event_bus import EventBus
from graphrecon.utils.logger import logger

console = Console()

app = typer.Typer(
    name="graphrecon",
    help="Dependency graph generator for modern web applications.",
    no_args_is_help=True,
)


@app.callback()
def main() -> None:
    """GraphRecon CLI."""


@app.command()
def version() -> None:
    logger.info("Displaying version information")
    console.print(f"[bold cyan]{APP_NAME}[/bold cyan]")
    console.print(f"Version: {VERSION}")


@app.command()
def scan(url: str) -> None:

    bus = EventBus()

    browser = BrowserManager(bus)

    browser.open(url)
