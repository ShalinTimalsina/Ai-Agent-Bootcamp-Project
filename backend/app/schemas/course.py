from typing import List, Optional

from pydantic import Field

from app.schemas.common import BaseSchema


class CourseBase(BaseSchema):
    slug: str
    title: str
    description: str
    category: str
    level: str
    icon: str
    duration_minutes: int = Field(..., ge=1)
    order_index: int = 0


class CourseSummary(CourseBase):
    id: int
    lesson_count: int
    completed_lessons: int
    percent_complete: int
    next_lesson_title: Optional[str] = None


class CourseLessonPreview(BaseSchema):
    id: int
    slug: str
    title: str
    description: str
    minutes: int
    order_index: int
    is_completed: bool = False


class CourseDetail(CourseSummary):
    lessons: List[CourseLessonPreview]
