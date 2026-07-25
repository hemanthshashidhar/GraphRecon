from collections import defaultdict
from collections.abc import Callable
from typing import Any


class EventBus:
    """
    Lightweight synchronous event bus.
    """

    def __init__(self) -> None:
        self._subscribers: dict[str, list[Callable[..., None]]] = defaultdict(list)

    def subscribe(
        self,
        event_name: str,
        callback: Callable[..., None],
    ) -> None:
        self._subscribers[event_name].append(callback)

    def emit(
        self,
        event_name: str,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        for callback in self._subscribers[event_name]:
            callback(*args, **kwargs)
