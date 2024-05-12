from pydantic import BaseModel, Field
from typing import Optional
from pydantic_mongo import PydanticObjectId


class Todo(BaseModel):
    id: Optional[PydanticObjectId] = Field(default=None)
    title: str
    completed: bool

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Something to do",
                "completed": False,
            }
        }
