import typer
from rich.console import Console

console = Console()

app = typer.Typer(
    name="graphrecon",
    help="Dependency graph generator for web applications.",
    no_args_is_help=True,
)


@app.command()
def version():
    """
    Display GraphRecon version.
    """
    console.print("[bold cyan]GraphRecon[/bold cyan]")
    console.print("Version: 0.1.0")


if __name__ == "__main__":
    app()
