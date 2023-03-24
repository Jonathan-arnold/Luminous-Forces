class EventManager:
    def __init__(self):
        self.listeners = {}

    def register_listener(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def deregister_listener(self, event_type, listener):
        if listener in self.listeners[event_type]:
            self.listeners[event_type].remove(listener)

    def propagate_event(self, event):
        event_type = event.type
        if event_type in self.listeners:
            for listener in self.listeners[event_type]:
                listener.handle_event(event)
