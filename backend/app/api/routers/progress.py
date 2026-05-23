from fastapi import APIRouter, HTTPException, Query

from app.core.config import DEFAULT_USER_ID
from app.schemas.progress import CourseProgressResponse, ProgressSummaryResponse
from app.services.progress_service import ProgressService

router = APIRouter(prefix='/api/progress', tags=['progress'])
service = ProgressService()


@router.get('/summary', response_model=ProgressSummaryResponse)
def get_summary(user_id: int = Query(DEFAULT_USER_ID, ge=1)):
    return service.get_summary(user_id=user_id)


@router.get('/courses/{course_id}', response_model=CourseProgressResponse)
def get_course_progress(course_id: int, user_id: int = Query(DEFAULT_USER_ID, ge=1)):
    progress = service.get_course_progress(course_id=course_id, user_id=user_id)
    if progress is None:
        raise HTTPException(status_code=404, detail='Course not found')
    return progress
