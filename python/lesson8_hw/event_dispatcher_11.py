"""Module docstring"""
from typing import Callable, Dict, List, Any


class EventDispatcher:
    """A simple event dispatcher system to register and dispatch events.

    This class allows registering event handlers and dispatching events with
    associated data. Multiple handlers can be registered for the same event.
    """

    def __init__(self):
        """Initialize an empty event registry."""
        self.events: Dict[str, List[Callable[[Any], None]]] = {}

    def register_event(self, name: str,
                       handler: Callable[[Any], None]) -> None:
        """Register an event handler for a specific event.

        Args:
            name (str): The name of the event to register the handler for.
            handler (Callable[[Any], None]): The handler function to call when
                the event is triggered. The handler should accept one argument
                (data of any type).
        """
        if name not in self.events:
            self.events[name] = []
        self.events[name].append(handler)

    def dispatch_event(self, name: str, data: Any) -> None:
        """Dispatch an event, calling all registered handlers for that event.

        Args:
            name (str): The name of the event to dispatch.
            data (Any): The data to pass to the event handlers.

        If no handlers are registered for the event, this method does nothing.
        """
        if name in self.events:
            for handler in self.events[name]:
                handler(data)


if __name__ == "__main__":
    dispatcher = EventDispatcher()


    def on_message(data: str):
        """A sample event handler that processes a message."""
        print(f"Received message: {data}")


    dispatcher.register_event("message", on_message)

    dispatcher.dispatch_event("message", "Hello, world!")
