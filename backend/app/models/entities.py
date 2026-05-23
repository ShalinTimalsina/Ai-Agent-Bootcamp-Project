from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class Course:
    id: int
    slug: str
    title: str
    description: str
    category: str
    level: str
    icon: str
    duration_minutes: int
    order_index: int


@dataclass(slots=True)
class Lesson:
    id: int
    course_id: int
    slug: str
    title: str
    description: str
    content: str
    code_example: str
    lesson_type: str
    minutes: int
    order_index: int


@dataclass(slots=True)
class Progress:
    id: int
    user_id: int
    course_id: int
    lesson_id: int
    is_completed: bool
    percent: int
    attempts_count: int
    completed_at: Optional[str]
    last_activity_at: str


@dataclass(slots=True)
class TerminalLog:
    id: int
    user_id: int
    command: str
    status: str
    output_json: str
    course_id: Optional[int]
    lesson_id: Optional[int]
    created_at: str
