from typing import Optional

from pydantic import Field

from app.schemas.common import BaseSchema, OutputLine


class TerminalExecuteRequest(BaseSchema):
    command: str = Field(..., min_length=1, max_length=500)
    course_id: Optional[int] = None
    lesson_id: Optional[int] = None
    user_id: int = 1


class TerminalExecuteResponse(BaseSchema):
    id: int
    command: str
    status: str
    output: list[OutputLine]
    course_id: Optional[int] = None
    lesson_id: Optional[int] = None


class TerminalLogResponse(BaseSchema):
    id: int
    user_id: int
    command: str
    status: str
    output: list[OutputLine]
    course_id: Optional[int] = None
    lesson_id: Optional[int] = None
    created_at: str
