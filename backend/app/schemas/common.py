from pydantic import BaseModel, ConfigDict, Field


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class OutputLine(BaseSchema):
    type: str = Field(..., examples=['command', 'output', 'success', 'warning', 'error', 'muted'])
    text: str


class ProgressSummary(BaseSchema):
    user_id: int
    course_id: int
    course_slug: str
    completed_lessons: int
    total_lessons: int
    percent_complete: int
    streak_days: int = 0
