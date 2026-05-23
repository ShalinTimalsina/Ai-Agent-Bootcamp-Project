from fastapi import APIRouter, HTTPException, Query

from app.core.config import DEFAULT_USER_ID
from app.schemas.lesson import LessonPreview, LessonProgressUpdate, LessonResponse
from app.services.lesson_service import LessonService

router = APIRouter(prefix='/api/lessons', tags=['lessons'])
service = LessonService()


@router.get('/{lesson_id}', response_model=LessonResponse)
def get_lesson(lesson_id: int, user_id: int = Query(DEFAULT_USER_ID, ge=1)):
    lesson = service.get_lesson(lesson_id=lesson_id, user_id=user_id)
    if lesson is None:
        raise HTTPException(status_code=404, detail='Lesson not found')
    return lesson


@router.get('/course/{course_id}', response_model=list[LessonPreview])
def list_lessons_for_course(
    course_id: int,
    user_id: int = Query(DEFAULT_USER_ID, ge=1),
    search: str | None = Query(default=None, min_length=1, max_length=80),
):
    return service.list_course_lessons(course_id=course_id, user_id=user_id, search=search)


@router.patch('/{lesson_id}/progress')
def update_lesson_progress(lesson_id: int, payload: LessonProgressUpdate, user_id: int = Query(DEFAULT_USER_ID, ge=1)):
    progress = service.mark_progress(
        lesson_id=lesson_id,
        completed=payload.completed,
        user_id=user_id,
        attempts_increment=payload.attempts_increment,
    )
    if progress is None:
        raise HTTPException(status_code=404, detail='Lesson not found')
    return {'ok': True, 'progress': progress}
