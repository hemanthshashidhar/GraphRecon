import logging
from rich.logging import RichHandler


def configure_logger() -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[
            RichHandler(
                rich_tracebacks=True,
                show_path=False,
            )
        ],
    )

    return logging.getLogger("graphrecon")


logger = configure_logger()
