from fastapi import APIRouter, Query

from app.core.config import DEFAULT_USER_ID
from app.schemas.dashboard import DashboardResponse
from app.services.dashboard_service import DashboardService

router = APIRouter(prefix='/api/dashboard', tags=['dashboard'])
service = DashboardService()


@router.get('', response_model=DashboardResponse)
def get_dashboard(user_id: int = Query(DEFAULT_USER_ID, ge=1)):
    return service.get_dashboard(user_id=user_id)
