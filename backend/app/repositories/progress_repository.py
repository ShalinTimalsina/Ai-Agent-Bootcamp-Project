from __future__ import annotations

from datetime import datetime, timezone

from app.core.config import DEFAULT_USER_ID
from app.db.database import get_connection, row_to_dict, rows_to_dicts


class ProgressRepository:
    def upsert_lesson_progress(
        self,
        *,
        user_id: int,
        course_id: int,
        lesson_id: int,
        completed: bool,
        attempts_increment: int = 1,
    ) -> dict:
        now = datetime.now(timezone.utc).isoformat()
        with get_connection() as connection:
            existing = connection.execute(
                'SELECT * FROM progress WHERE user_id = ? AND lesson_id = ?',
                (user_id, lesson_id),
            ).fetchone()

            if existing is None:
                connection.execute(
                    '''
                    INSERT INTO progress (user_id, course_id, lesson_id, is_completed, percent, attempts_count, completed_at, last_activity_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''',
                    (
                        user_id,
                        course_id,
                        lesson_id,
                        1 if completed else 0,
                        100 if completed else 0,
                        attempts_increment,
                        now if completed else None,
                        now,
                    ),
                )
            else:
                attempts_count = int(existing['attempts_count']) + attempts_increment
                is_completed = 1 if completed else int(existing['is_completed'])
                percent = 100 if is_completed else int(existing['percent'])
                completed_at = existing['completed_at'] or (now if completed else None)
                connection.execute(
                    '''
                    UPDATE progress
                    SET course_id = ?, is_completed = ?, percent = ?, attempts_count = ?, completed_at = ?, last_activity_at = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE user_id = ? AND lesson_id = ?
                    ''',
                    (
                        course_id,
                        is_completed,
                        percent,
                        attempts_count,
                        completed_at,
                        now,
                        user_id,
                        lesson_id,
                    ),
                )

            row = connection.execute(
                'SELECT * FROM progress WHERE user_id = ? AND lesson_id = ?',
                (user_id, lesson_id),
            ).fetchone()
            return row_to_dict(row) or {}

    def list_lesson_progress_for_course(self, *, user_id: int, course_id: int) -> list[dict]:
        with get_connection() as connection:
            rows = connection.execute(
                '''
                SELECT p.*, l.title AS lesson_title, c.slug AS course_slug
                FROM progress p
                JOIN lessons l ON l.id = p.lesson_id
                JOIN courses c ON c.id = p.course_id
                WHERE p.user_id = ? AND p.course_id = ?
                ORDER BY l.order_index, l.id
                ''',
                (user_id, course_id),
            ).fetchall()
            return rows_to_dicts(rows)

    def get_course_progress_counts(self, *, user_id: int, course_id: int) -> dict:
        with get_connection() as connection:
            completed_row = connection.execute(
                '''
                SELECT COUNT(*) AS completed
                FROM progress p
                JOIN lessons l ON l.id = p.lesson_id
                WHERE p.user_id = ? AND p.course_id = ? AND p.is_completed = 1
                ''',
                (user_id, course_id),
            ).fetchone()
            last_row = connection.execute(
                '''
                SELECT MAX(last_activity_at) AS last_activity_at
                FROM progress
                WHERE user_id = ? AND course_id = ?
                ''',
                (user_id, course_id),
            ).fetchone()
            return {
                'completed_lessons': int(completed_row['completed'] if completed_row else 0),
                'last_activity_at': last_row['last_activity_at'] if last_row else None,
            }

    def get_overall_progress(self, *, user_id: int = DEFAULT_USER_ID) -> list[dict]:
        with get_connection() as connection:
            rows = connection.execute(
                '''
                SELECT
                    c.id AS course_id,
                    c.slug AS course_slug,
                    c.title AS course_title,
                    COUNT(l.id) AS total_lessons,
                    COALESCE(SUM(CASE WHEN p.is_completed = 1 THEN 1 ELSE 0 END), 0) AS completed_lessons,
                    MAX(p.last_activity_at) AS last_activity_at
                FROM courses c
                LEFT JOIN lessons l ON l.course_id = c.id
                LEFT JOIN progress p ON p.course_id = c.id AND p.lesson_id = l.id AND p.user_id = ?
                GROUP BY c.id, c.slug, c.title
                ORDER BY c.order_index, c.id
                ''',
                (user_id,),
            ).fetchall()
            return rows_to_dicts(rows)
