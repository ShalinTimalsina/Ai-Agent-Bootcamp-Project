from fastapi import APIRouter, HTTPException, Query

from app.core.config import DEFAULT_USER_ID
from app.schemas.course import CourseDetail, CourseSummary
from app.services.course_service import CourseService

router = APIRouter(prefix='/api/courses', tags=['courses'])
service = CourseService()


@router.get('', response_model=list[CourseSummary])
def list_courses(
    user_id: int = Query(DEFAULT_USER_ID, ge=1),
    search: str | None = Query(default=None, min_length=1, max_length=80),
    category: str | None = Query(default=None, min_length=1, max_length=40),
    level: str | None = Query(default=None, min_length=1, max_length=30),
    limit: int | None = Query(default=None, ge=1, le=50),
    offset: int | None = Query(default=None, ge=0),
):
    return service.list_courses(
        user_id=user_id,
        search=search,
        category=category,
        level=level,
        limit=limit,
        offset=offset,
    )


@router.get('/{course_id}', response_model=CourseDetail)
def get_course(course_id: int, user_id: int = Query(DEFAULT_USER_ID, ge=1)):
    course = service.get_course_detail(course_id=course_id, user_id=user_id)
    if course is None:
        raise HTTPException(status_code=404, detail='Course not found')
    return course
