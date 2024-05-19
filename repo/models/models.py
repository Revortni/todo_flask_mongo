from pydantic import BaseModel, Field
from typing import Optional
from pydantic_mongo import PydanticObjectId

from datetime import datetime


class Todo(BaseModel):
    id: Optional[PydanticObjectId] = Field(default=None)
    title: str
    description: Optional[str] = Field(default=None)
    completed: bool
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Something to do",
                "description": "Do this and that too",
                "completed": False,
                "created_at": "2022-01-01T00:00:00Z",
                "updated_at": "2022-01-01T00:00:00Z"
            }
        }
