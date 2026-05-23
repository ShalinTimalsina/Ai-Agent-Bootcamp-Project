from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.dashboard import router as dashboard_router
from app.api.routers.courses import router as courses_router
from app.api.routers.lessons import router as lessons_router
from app.api.routers.progress import router as progress_router
from app.api.routers.terminal import router as terminal_router
from app.core.config import CORS_ORIGINS
from app.db.database import initialize_database
from app.db.seed import seed_database



@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_database()
    seed_database()
    yield


app = FastAPI(title='DevOps Academy API', version='1.1.0', lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(courses_router)
app.include_router(lessons_router)
app.include_router(progress_router)
app.include_router(terminal_router)
app.include_router(dashboard_router)


@app.get('/health')
def health_check() -> dict[str, str]:
    return {'status': 'ok'}


@app.get('/')
def root() -> dict[str, str]:
    return {'message': 'DevOps Academy API', 'docs': '/docs'}
