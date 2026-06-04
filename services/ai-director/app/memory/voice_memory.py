from pydantic import BaseModel

from typing import Optional


class VoiceMemory(BaseModel):

    voice_id: str

    name: str

    language: Optional[str] = None

    accent: Optional[str] = None

    emotion: Optional[str] = None