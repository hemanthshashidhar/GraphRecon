from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass(slots=True)
class QueueItem:
    url: str
    depth: int


class URLQueue:
    """
    Breadth-first queue used by the crawler.

    Features:
    - Deduplication
    - BFS traversal
    - Depth tracking
    """

    def __init__(self) -> None:
        self._queue: deque[QueueItem] = deque()
        self._visited: set[str] = set()

    def add(
        self,
        url: str,
        depth: int = 0,
    ) -> bool:
        """
        Queue a URL.

        Returns True if added.
        """

        if url in self._visited:
            return False

        self._visited.add(url)

        self._queue.append(
            QueueItem(
                url=url,
                depth=depth,
            )
        )

        return True

    def pop(self) -> QueueItem:
        return self._queue.popleft()

    def empty(self) -> bool:
        return not self._queue

    @property
    def visited(self) -> set[str]:
        return self._visited

    @property
    def visited_count(self) -> int:
        return len(self._visited)

    @property
    def pending_count(self) -> int:
        return len(self._queue)
