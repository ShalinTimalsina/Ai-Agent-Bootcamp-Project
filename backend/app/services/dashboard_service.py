from __future__ import annotations

from app.core.config import DEFAULT_USER_ID
from app.services.course_service import CourseService
from app.services.progress_service import ProgressService
from app.services.terminal_service import TerminalService


class DashboardService:
    def __init__(self) -> None:
        self.courses = CourseService()
        self.progress = ProgressService()
        self.terminal = TerminalService()

    def get_dashboard(self, user_id: int = DEFAULT_USER_ID) -> dict:
        return {
            'user_id': user_id,
            'courses': self.courses.list_courses(user_id=user_id, limit=6),
            'progress': self.progress.get_summary(user_id=user_id),
            'recent_terminal_logs': self.terminal.list_history(user_id=user_id, limit=5),
        }
