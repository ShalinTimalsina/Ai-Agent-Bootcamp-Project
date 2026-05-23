from __future__ import annotations

from app.core.config import DEFAULT_USER_ID
from app.repositories.course_repository import CourseRepository
from app.repositories.lesson_repository import LessonRepository
from app.repositories.progress_repository import ProgressRepository


class LessonService:
    def __init__(self) -> None:
        self.courses = CourseRepository()
        self.lessons = LessonRepository()
        self.progress = ProgressRepository()

    def get_lesson(self, lesson_id: int, user_id: int = DEFAULT_USER_ID) -> dict | None:
        lesson = self.lessons.get_lesson(lesson_id)
        if lesson is None:
            return None

        course = self.courses.get_course(int(lesson['course_id']))
        if course is None:
            return None

        progress_rows = self.progress.list_lesson_progress_for_course(user_id=user_id, course_id=course['id'])
        progress_map = {item['lesson_id']: item for item in progress_rows}
        progress = progress_map.get(lesson_id)

        return {
            'id': lesson['id'],
            'course_id': lesson['course_id'],
            'slug': lesson['slug'],
            'title': lesson['title'],
            'description': lesson['description'],
            'content': lesson['content'],
            'code_example': lesson['code_example'],
            'lesson_type': lesson['lesson_type'],
            'minutes': lesson['minutes'],
            'order_index': lesson['order_index'],
            'course_slug': course['slug'],
            'course_title': course['title'],
            'course_category': course['category'],
            'completed': bool(progress and progress['is_completed']),
            'progress_percent': int(progress['percent']) if progress else 0,
        }

    def list_course_lessons(
        self,
        course_id: int,
        user_id: int = DEFAULT_USER_ID,
        *,
        search: str | None = None,
    ) -> list[dict]:
        course = self.courses.get_course(course_id)
        if course is None:
            return []
        lessons = self.lessons.list_lessons_for_course(course_id, search=search)
        progress_rows = self.progress.list_lesson_progress_for_course(user_id=user_id, course_id=course_id)
        progress_map = {item['lesson_id']: item for item in progress_rows}
        return [
            {
                'id': lesson['id'],
                'course_id': lesson['course_id'],
                'slug': lesson['slug'],
                'title': lesson['title'],
                'description': lesson['description'],
                'minutes': lesson['minutes'],
                'order_index': lesson['order_index'],
                'completed': bool(progress_map.get(lesson['id'], {}).get('is_completed')),
                'progress_percent': int(progress_map.get(lesson['id'], {}).get('percent', 0)),
            }
            for lesson in lessons
        ]

    def mark_progress(self, lesson_id: int, completed: bool, user_id: int = DEFAULT_USER_ID, attempts_increment: int = 1) -> dict | None:
        lesson = self.lessons.get_lesson(lesson_id)
        if lesson is None:
            return None
        return self.progress.upsert_lesson_progress(
            user_id=user_id,
            course_id=int(lesson['course_id']),
            lesson_id=lesson_id,
            completed=completed,
            attempts_increment=attempts_increment,
        )
