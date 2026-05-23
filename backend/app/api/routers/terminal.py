from fastapi import APIRouter, Query

from app.core.config import DEFAULT_USER_ID
from app.schemas.terminal import TerminalExecuteRequest, TerminalExecuteResponse, TerminalLogResponse
from app.services.terminal_service import TerminalService

router = APIRouter(prefix='/api/terminal', tags=['terminal'])
service = TerminalService()


@router.post('/execute', response_model=TerminalExecuteResponse)
def execute_command(payload: TerminalExecuteRequest, user_id: int = Query(DEFAULT_USER_ID, ge=1)):
    return service.execute(
        command=payload.command,
        user_id=payload.user_id or user_id,
        course_id=payload.course_id,
        lesson_id=payload.lesson_id,
    )


@router.get('/history', response_model=list[TerminalLogResponse])
def terminal_history(user_id: int = Query(DEFAULT_USER_ID, ge=1), limit: int = Query(25, ge=1, le=100)):
    return service.list_history(user_id=user_id, limit=limit)
