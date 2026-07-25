class GraphReconError(Exception):
    """Base exception for GraphRecon."""


class BrowserError(GraphReconError):
    """Browser-related errors."""


class CrawlError(GraphReconError):
    """Crawler-related errors."""


class CollectorError(GraphReconError):
    """Collector-related errors."""


class ExportError(GraphReconError):
    """Export-related errors."""
