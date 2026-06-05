from app.schemas.memory_state import MemoryState


class MemoryManager:

    def __init__(self):

        self.state = MemoryState()

    def get_state(self):

        return self.state

    def load_state(
        self,
        state,
    ):
        self.state = state