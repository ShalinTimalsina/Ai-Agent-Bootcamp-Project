from typing import Optional

from pydantic import Field

from app.schemas.common import BaseSchema


class LessonBase(BaseSchema):
    course_id: int
    slug: str
    title: str
    description: str
    content: str
    code_example: str
    lesson_type: str = 'lesson'
    minutes: int = Field(..., ge=1)
    order_index: int = 0


class LessonResponse(LessonBase):
    id: int
    course_slug: str
    course_title: str
    course_category: str
    completed: bool = False
    progress_percent: int = 0


class LessonProgressUpdate(BaseSchema):
    completed: bool = True
    attempts_increment: int = Field(1, ge=0, le=50)
