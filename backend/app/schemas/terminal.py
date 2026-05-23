from typing import Optional

from app.schemas.common import BaseSchema, OutputLine


class TerminalExecuteRequest(BaseSchema):
    command: str
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
