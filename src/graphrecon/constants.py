"""
Global constants used throughout GraphRecon.
"""

APP_NAME = "GraphRecon"
VERSION = "0.1.0"

DEFAULT_TIMEOUT = 30000  # milliseconds
DEFAULT_MAX_DEPTH = 3
DEFAULT_MAX_PAGES = 100

USER_AGENT = (
    "GraphRecon/0.1 (+https://github.com/yourusername/graphrecon)"
)

SUPPORTED_RESOURCE_TYPES = {
    "document",
    "stylesheet",
    "script",
    "image",
    "font",
    "media",
    "xhr",
    "fetch",
    "websocket",
    "manifest",
}
