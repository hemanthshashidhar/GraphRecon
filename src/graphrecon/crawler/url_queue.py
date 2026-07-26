from collections import deque


class URLQueue:
    """
    Breadth-first URL queue with deduplication.
    """

    def __init__(self) -> None:
        self._queue: deque[str] = deque()
        self._visited: set[str] = set()

    def add(self, url: str) -> bool:
        """
        Add a URL if it has not been visited.

        Returns True if the URL was queued.
        """

        if url in self._visited:
            return False

        self._visited.add(url)
        self._queue.append(url)

        return True

    def pop(self) -> str:
        return self._queue.popleft()

    def empty(self) -> bool:
        return len(self._queue) == 0

    @property
    def visited(self) -> set[str]:
        return self._visited
