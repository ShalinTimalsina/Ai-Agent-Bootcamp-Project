from __future__ import annotations

from app.db.database import get_connection, row_to_dict, rows_to_dicts


class CourseRepository:
    def list_courses(self) -> list[dict]:
        with get_connection() as connection:
            rows = connection.execute(
                'SELECT * FROM courses ORDER BY order_index, id'
            ).fetchall()
            return rows_to_dicts(rows)

    def get_course(self, course_id: int) -> dict | None:
        with get_connection() as connection:
            row = connection.execute('SELECT * FROM courses WHERE id = ?', (course_id,)).fetchone()
            return row_to_dict(row)

    def get_course_by_slug(self, slug: str) -> dict | None:
        with get_connection() as connection:
            row = connection.execute('SELECT * FROM courses WHERE slug = ?', (slug,)).fetchone()
            return row_to_dict(row)
