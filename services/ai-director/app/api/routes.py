from fastapi import APIRouter

from app.orchestrators.generation_orchestrator import (
    GenerationOrchestrator,
)

router = APIRouter()

orchestrator = GenerationOrchestrator()


@router.get("/generate-plan/{story_id}")
async def generate_plan(
    story_id: str,
):
    return await orchestrator.create_plan(
        story_id=story_id,
    )