class InMemoryQueue:
    """
    Cola en memoria para simular envío de eventos.
    """
    def __init__(self):
        self.messages = []

    def emit(self, message: dict):
        self.messages.append(message)
        print(f"[Queue] Message emitted: {message}")
