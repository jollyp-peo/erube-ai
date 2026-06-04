from pydantic import BaseModel

from typing import Optional


class LocationMemory(BaseModel):

    name: str

    time_of_day: Optional[str] = None

    weather: Optional[str] = None