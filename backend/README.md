# DevOps Academy Backend

A small but scalable FastAPI backend for the DevOps learning platform.

## What it provides

- Course catalog for the sidebar and dashboard
- Lesson roadmap data for each course
- Lesson progress tracking for the single-user flow
- Terminal command simulation with log persistence
- SQLite storage with automatic schema creation and seed data

## Structure

- `app/main.py` — FastAPI app, middleware, startup hooks
- `app/api/routers/` — route layer
- `app/services/` — business logic
- `app/repositories/` — SQLite access layer
- `app/db/` — schema creation and seed data
- `app/models/` — domain entities
- `app/schemas/` — request/response validation

## Run with uv

```bash
uv sync
uv run uvicorn app.main:app --reload
```

## API overview

- `GET /api/dashboard`
- `GET /health`
- `GET /api/courses`
- `GET /api/courses/{course_id}`
- `GET /api/lessons/{lesson_id}`
- `GET /api/lessons/course/{course_id}`
- `PATCH /api/lessons/{lesson_id}/progress`
- `GET /api/progress/summary`
- `GET /api/progress/courses/{course_id}`
- `POST /api/terminal/execute`
- `GET /api/terminal/history`

## Useful query params

- `GET /api/courses?search=docker&category=Containers&level=Beginner&limit=10&offset=0`
- `GET /api/lessons/course/{course_id}?search=deploy`
- `GET /api/dashboard?user_id=1`
