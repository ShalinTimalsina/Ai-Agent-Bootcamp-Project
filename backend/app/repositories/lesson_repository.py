from __future__ import annotations

from app.db.database import get_connection, row_to_dict, rows_to_dicts


class LessonRepository:
    def list_lessons_for_course(self, course_id: int, *, search: str | None = None) -> list[dict]:
        clauses = ['course_id = ?']
        params: list[object] = [course_id]

        if search:
            clauses.append('(title LIKE ? OR description LIKE ? OR slug LIKE ?)')
            like = f'%{search.strip()}%'
            params.extend([like, like, like])

        with get_connection() as connection:
            rows = connection.execute(
                f"SELECT * FROM lessons WHERE {' AND '.join(clauses)} ORDER BY order_index, id",
                tuple(params),
            ).fetchall()
            return rows_to_dicts(rows)

    def get_lesson(self, lesson_id: int) -> dict | None:
        with get_connection() as connection:
            row = connection.execute('SELECT * FROM lessons WHERE id = ?', (lesson_id,)).fetchone()
            return row_to_dict(row)

    def get_lesson_by_slug(self, slug: str) -> dict | None:
        with get_connection() as connection:
            row = connection.execute('SELECT * FROM lessons WHERE slug = ?', (slug,)).fetchone()
            return row_to_dict(row)

    def count_lessons_for_course(self, course_id: int) -> int:
        with get_connection() as connection:
            row = connection.execute(
                'SELECT COUNT(*) AS total FROM lessons WHERE course_id = ?',
                (course_id,),
            ).fetchone()
            return int(row['total'] if row else 0)
