from __future__ import annotations

import json
from datetime import datetime, timezone

from app.db.database import get_connection, row_to_dict, rows_to_dicts


class TerminalRepository:
    def create_log(
        self,
        *,
        user_id: int,
        command: str,
        status: str,
        output: list[dict],
        course_id: int | None = None,
        lesson_id: int | None = None,
    ) -> dict:
        now = datetime.now(timezone.utc).isoformat()
        with get_connection() as connection:
            cursor = connection.execute(
                '''
                INSERT INTO terminal_logs (user_id, course_id, lesson_id, command, status, output_json, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''',
                (user_id, course_id, lesson_id, command, status, json.dumps(output), now),
            )
            row = connection.execute('SELECT * FROM terminal_logs WHERE id = ?', (cursor.lastrowid,)).fetchone()
            return row_to_dict(row) or {}

    def list_logs(self, *, user_id: int, limit: int = 25) -> list[dict]:
        with get_connection() as connection:
            rows = connection.execute(
                'SELECT * FROM terminal_logs WHERE user_id = ? ORDER BY id DESC LIMIT ?',
                (user_id, limit),
            ).fetchall()
            return rows_to_dicts(rows)
