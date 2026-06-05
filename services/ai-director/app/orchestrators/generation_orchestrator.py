# from app.clients.django_client import DjangoClient
# from app.memory.memory_manager import MemoryManager
# from app.planners.story_planner import StoryPlanner


# class GenerationOrchestrator:

#     def __init__(self):

#         self.client = DjangoClient()

#         self.memory_manager = MemoryManager()

#         self.story_planner = StoryPlanner(
#             memory_manager=self.memory_manager,
#         )

#     async def create_plan(
#         self,
#         story_id: str,
#     ):

#         story = await self.client.get_story(
#             story_id,
#         )

#         return self.story_planner.create_generation_plan(
#             story_id=story["id"],
#         )

from app.memory.memory_manager import MemoryManager
from app.planners.story_planner import StoryPlanner


class GenerationOrchestrator:

    def __init__(self):

        self.memory_manager = MemoryManager()

        self.story_planner = StoryPlanner(
            memory_manager=self.memory_manager,
        )

    async def create_plan(
        self,
        story_id: str,
    ):

        return self.story_planner.create_generation_plan(
            story_id=story_id,
        )