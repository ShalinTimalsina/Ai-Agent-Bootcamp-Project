from __future__ import annotations

from app.core.config import DEFAULT_USER_ID
from app.repositories.course_repository import CourseRepository
from app.repositories.lesson_repository import LessonRepository
from app.repositories.progress_repository import ProgressRepository


class ProgressService:
    def __init__(self) -> None:
        self.courses = CourseRepository()
        self.lessons = LessonRepository()
        self.progress = ProgressRepository()

    def get_summary(self, user_id: int = DEFAULT_USER_ID) -> dict:
        course_progress = self.progress.get_overall_progress(user_id=user_id)
        total_lessons = sum(int(item['total_lessons']) for item in course_progress)
        total_completed = sum(int(item['completed_lessons']) for item in course_progress)
        percent = int(round((total_completed / total_lessons) * 100)) if total_lessons else 0
        last_activity = max(
            (item['last_activity_at'] for item in course_progress if item.get('last_activity_at')),
            default=None,
        )

        return {
            'user_id': user_id,
            'overall_percent': percent,
            'total_completed_lessons': total_completed,
            'total_lessons': total_lessons,
            'streak_days': 4,
            'last_activity_at': last_activity,
            'courses': [
                {
                    'course_id': item['course_id'],
                    'course_slug': item['course_slug'],
                    'course_title': item['course_title'],
                    'completed_lessons': int(item['completed_lessons']),
                    'total_lessons': int(item['total_lessons']),
                    'percent_complete': int(round((int(item['completed_lessons']) / int(item['total_lessons'])) * 100)) if int(item['total_lessons']) else 0,
                    'last_activity_at': item['last_activity_at'],
                }
                for item in course_progress
            ],
        }

    def get_course_progress(self, course_id: int, user_id: int = DEFAULT_USER_ID) -> dict | None:
        course = self.courses.get_course(course_id)
        if course is None:
            return None
        lessons = self.lessons.list_lessons_for_course(course_id)
        progress_rows = self.progress.list_lesson_progress_for_course(user_id=user_id, course_id=course_id)
        progress_map = {item['lesson_id']: item for item in progress_rows}
        completed = sum(1 for lesson in lessons if progress_map.get(lesson['id'], {}).get('is_completed'))
        total = len(lessons)
        percent = int(round((completed / total) * 100)) if total else 0
        return {
            'user_id': user_id,
            'course_id': course_id,
            'course_slug': course['slug'],
            'completed_lessons': completed,
            'total_lessons': total,
            'percent_complete': percent,
            'streak_days': 4,
            'last_activity_at': max(
                (item['last_activity_at'] for item in progress_rows if item.get('last_activity_at')),
                default=None,
            ),
        }
