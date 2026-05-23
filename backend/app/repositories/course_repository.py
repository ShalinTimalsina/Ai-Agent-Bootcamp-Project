from __future__ import annotations

from app.db.database import get_connection, row_to_dict, rows_to_dicts


class CourseRepository:
    def list_courses(
        self,
        *,
        search: str | None = None,
        category: str | None = None,
        level: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> list[dict]:
        clauses = []
        params: list[object] = []

        if search:
            clauses.append('(title LIKE ? OR description LIKE ? OR category LIKE ? OR slug LIKE ?)')
            like = f'%{search.strip()}%'
            params.extend([like, like, like, like])
        if category:
            clauses.append('category = ?')
            params.append(category)
        if level:
            clauses.append('level = ?')
            params.append(level)

        sql = 'SELECT * FROM courses'
        if clauses:
            sql += ' WHERE ' + ' AND '.join(clauses)
        sql += ' ORDER BY order_index, id'
        if limit is not None:
            sql += ' LIMIT ?'
            params.append(limit)
        elif offset is not None:
            sql += ' LIMIT -1 OFFSET ?'
            params.append(offset)
        if limit is not None and offset is not None:
            sql += ' OFFSET ?'
            params.append(offset)

        with get_connection() as connection:
            rows = connection.execute(sql, tuple(params)).fetchall()
            return rows_to_dicts(rows)

    def get_course(self, course_id: int) -> dict | None:
        with get_connection() as connection:
            row = connection.execute('SELECT * FROM courses WHERE id = ?', (course_id,)).fetchone()
            return row_to_dict(row)

    def get_course_by_slug(self, slug: str) -> dict | None:
        with get_connection() as connection:
            row = connection.execute('SELECT * FROM courses WHERE slug = ?', (slug,)).fetchone()
            return row_to_dict(row)
