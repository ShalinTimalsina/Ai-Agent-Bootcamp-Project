from app.schemas.common import BaseSchema
from app.schemas.course import CourseSummary
from app.schemas.progress import ProgressSummaryResponse
from app.schemas.terminal import TerminalLogResponse


class DashboardResponse(BaseSchema):
    user_id: int
    courses: list[CourseSummary]
    progress: ProgressSummaryResponse
    recent_terminal_logs: list[TerminalLogResponse]
