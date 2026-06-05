from app.clients.django_client import DjangoClient
from app.memory.memory_manager import MemoryManager
from app.planners.story_planner import StoryPlanner
from app.memory.memory_builder import MemoryBuilder
from app.schemas.memory_state import MemoryState


class GenerationOrchestrator:

    def __init__(self):

        self.client = DjangoClient()

        self.memory_manager = MemoryManager()

        self.story_planner = StoryPlanner(
            memory_manager=self.memory_manager,
        )
        
        self.memory_builder = MemoryBuilder()

    async def create_plan(
        self,
        story_id: str,
    ):
        

        story = await self.client.get_story(
            story_id,
        )

        scene_response = await self.client.get_story_scenes(
            story_id,
        )

        scenes = scene_response["scenes"]

        total_shots = 0

        for scene in scenes:

            shot_response = await self.client.get_scene_shots(
                scene["id"],
            )

            scene["shots"] = shot_response["shots"]

            total_shots += len(
                shot_response["shots"]
            )
        
        memory_state: MemoryState = self.memory_builder.build(
            story=story,
            scenes=scenes,
        )
        
        self.memory_manager.load_state(
            memory_state
        )   
    
        return self.story_planner.create_generation_plan(
            story=story,
            scenes=scenes,
            total_shots=total_shots,
        )