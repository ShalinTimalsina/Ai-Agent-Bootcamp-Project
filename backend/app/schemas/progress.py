from datetime import datetime
from typing import Optional

from app.schemas.common import BaseSchema


class CourseProgressItem(BaseSchema):
    course_id: int
    course_slug: str
    course_title: str
    completed_lessons: int
    total_lessons: int
    percent_complete: int
    last_activity_at: Optional[datetime] = None


class ProgressLessonState(BaseSchema):
    lesson_id: int
    lesson_title: str
    course_id: int
    course_slug: str
    is_completed: bool
    percent: int
    attempts_count: int
    last_activity_at: datetime
    completed_at: Optional[datetime] = None


class ProgressSummaryResponse(BaseSchema):
    user_id: int
    overall_percent: int
    total_completed_lessons: int
    total_lessons: int
    streak_days: int
    last_activity_at: Optional[datetime] = None
    courses: list[CourseProgressItem]


class CourseProgressResponse(BaseSchema):
    user_id: int
    course_id: int
    course_slug: str
    completed_lessons: int
    total_lessons: int
    percent_complete: int
    streak_days: int
    last_activity_at: Optional[datetime] = None
