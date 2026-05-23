from __future__ import annotations

from app.core.config import DEFAULT_USER_ID
from app.repositories.course_repository import CourseRepository
from app.repositories.lesson_repository import LessonRepository
from app.repositories.progress_repository import ProgressRepository


class CourseService:
    def __init__(self) -> None:
        self.courses = CourseRepository()
        self.lessons = LessonRepository()
        self.progress = ProgressRepository()

    def list_courses(
        self,
        user_id: int = DEFAULT_USER_ID,
        *,
        search: str | None = None,
        category: str | None = None,
        level: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> list[dict]:
        courses = self.courses.list_courses(search=search, category=category, level=level, limit=limit, offset=offset)
        overall = self.progress.get_overall_progress(user_id=user_id)
        progress_map = {item['course_id']: item for item in overall}

        result = []
        for course in courses:
            lessons = self.lessons.list_lessons_for_course(course['id'])
            counts = progress_map.get(course['id'], {})
            progress_rows = self.progress.list_lesson_progress_for_course(user_id=user_id, course_id=course['id'])
            completed_ids = {item['lesson_id'] for item in progress_rows if item['is_completed']}
            completed = len(completed_ids)
            total = int(counts.get('total_lessons', len(lessons)))
            percent = int(round((completed / total) * 100)) if total else 0
            next_lesson = next((lesson['title'] for lesson in lessons if lesson['id'] not in completed_ids), None)
            result.append(
                {
                    **course,
                    'lesson_count': total,
                    'completed_lessons': completed,
                    'percent_complete': percent,
                    'next_lesson_title': next_lesson,
                }
            )
        return result

    def get_course_detail(self, course_id: int, user_id: int = DEFAULT_USER_ID) -> dict | None:
        course = self.courses.get_course(course_id)
        if course is None:
            return None

        lessons = self.lessons.list_lessons_for_course(course_id)
        progress_rows = {
            item['lesson_id']: item
            for item in self.progress.list_lesson_progress_for_course(user_id=user_id, course_id=course_id)
        }

        lesson_items = []
        for lesson in lessons:
            progress = progress_rows.get(lesson['id'])
            lesson_items.append(
                {
                    'id': lesson['id'],
                    'slug': lesson['slug'],
                    'title': lesson['title'],
                    'description': lesson['description'],
                    'minutes': lesson['minutes'],
                    'order_index': lesson['order_index'],
                    'is_completed': bool(progress and progress['is_completed']),
                }
            )

        completed_lessons = sum(1 for item in lesson_items if item['is_completed'])
        total_lessons = len(lesson_items)
        percent = int(round((completed_lessons / total_lessons) * 100)) if total_lessons else 0
        next_lesson = next((item['title'] for item in lesson_items if not item['is_completed']), None)

        return {
            **course,
            'lesson_count': total_lessons,
            'completed_lessons': completed_lessons,
            'percent_complete': percent,
            'next_lesson_title': next_lesson,
            'lessons': lesson_items,
        }
