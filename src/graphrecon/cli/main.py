import typer
from rich.console import Console

console = Console()

app = typer.Typer(
    name="graphrecon",
    help="Dependency graph generator for modern web applications.",
    no_args_is_help=True,
)


@app.callback()
def main() -> None:
    """
    GraphRecon CLI.
    """
    pass


@app.command()
def version() -> None:
    """
    Show GraphRecon version.
    """
    console.print("[bold cyan]GraphRecon[/bold cyan]")
    console.print("Version: 0.1.0")
