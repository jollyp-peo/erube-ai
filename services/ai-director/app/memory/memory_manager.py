from app.schemas.memory_state import MemoryState


class MemoryManager:

    def __init__(self):

        self.state = MemoryState()

    def get_state(self) -> MemoryState:

        return self.state

    def update_state(
        self,
        state: MemoryState,
    ) -> None:

        self.state = state