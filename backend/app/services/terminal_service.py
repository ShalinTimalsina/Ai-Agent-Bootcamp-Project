from __future__ import annotations

import re
import json
from dataclasses import dataclass
from typing import Callable

from app.core.config import DEFAULT_USER_ID
from app.repositories.terminal_repository import TerminalRepository
from app.schemas.common import OutputLine


@dataclass(frozen=True)
class TerminalCommand:
    pattern: re.Pattern[str]
    handler: Callable[[str, re.Match[str]], list[OutputLine]]
    name: str


class TerminalService:
    def __init__(self) -> None:
        self.logs = TerminalRepository()
        self.commands = [
            TerminalCommand(re.compile(r'^(help|\?)$'), self._help, 'help'),
            TerminalCommand(re.compile(r'^clear$'), self._clear, 'clear'),
            TerminalCommand(re.compile(r'^echo\s+(.+)$', re.IGNORECASE), self._echo, 'echo'),
            TerminalCommand(re.compile(r'^docker\s+ps$', re.IGNORECASE), self._docker_ps, 'docker_ps'),
            TerminalCommand(re.compile(r'^kubectl\s+get\s+pods(?:\s+-n\s+(?P<namespace>[\w-]+))?$', re.IGNORECASE), self._kubectl_get_pods, 'kubectl_get_pods'),
            TerminalCommand(re.compile(r'^docker\s+build\s+-t\s+app\s+\.$', re.IGNORECASE), self._docker_build, 'docker_build'),
        ]

    def execute(self, *, command: str, user_id: int = DEFAULT_USER_ID, course_id: int | None = None, lesson_id: int | None = None) -> dict:
        command = command.strip()
        if not command:
            output = [OutputLine(type='warning', text='Type a command to continue.')]
            status = 'warning'
        else:
            output, status = self._dispatch(command)

        log = self.logs.create_log(
            user_id=user_id,
            course_id=course_id,
            lesson_id=lesson_id,
            command=command,
            status=status,
            output=[line.model_dump() for line in output],
        )
        return {
            'id': log['id'],
            'command': command,
            'status': status,
            'output': output,
            'course_id': course_id,
            'lesson_id': lesson_id,
        }

    def list_history(self, user_id: int = DEFAULT_USER_ID, limit: int = 25) -> list[dict]:
        logs = self.logs.list_logs(user_id=user_id, limit=limit)
        return [
            {
                **log,
                'output': json.loads(log['output_json']) if log.get('output_json') else [],
            }
            for log in logs
        ]

    def _dispatch(self, command: str) -> tuple[list[OutputLine], str]:
        for entry in self.commands:
            match = entry.pattern.match(command)
            if match:
                return entry.handler(command, match), self._status_for(entry.name)
        return [
            OutputLine(type='warning', text=f'Unknown command: {command}'),
            OutputLine(type='muted', text='Try help, docker ps, kubectl get pods -n platform, or echo hello'),
        ], 'warning'

    def _status_for(self, name: str) -> str:
        return 'success'

    def _help(self, command: str, match: re.Match[str]) -> list[OutputLine]:
        return [
            OutputLine(type='muted', text='Commands: help, clear, echo <text>, docker ps, kubectl get pods, docker build -t app .'),
            OutputLine(type='muted', text='This terminal is simulated now and can be connected to real execution later.'),
        ]

    def _clear(self, command: str, match: re.Match[str]) -> list[OutputLine]:
        return [OutputLine(type='muted', text='__CLEAR__')]

    def _echo(self, command: str, match: re.Match[str]) -> list[OutputLine]:
        return [OutputLine(type='output', text=match.group(1))]

    def _docker_ps(self, command: str, match: re.Match[str]) -> list[OutputLine]:
        return [
            OutputLine(type='output', text='CONTAINER ID   IMAGE          COMMAND                  STATUS        PORTS     NAMES'),
            OutputLine(type='output', text='b1a2c3d4e5f6   nginx:alpine   "nginx -g \'daemon…"   Up 7 minutes  80/tcp    web'),
        ]

    def _kubectl_get_pods(self, command: str, match: re.Match[str]) -> list[OutputLine]:
        namespace = match.groupdict().get('namespace') or 'platform'
        return [
            OutputLine(type='success', text='NAME                         READY   STATUS    RESTARTS   AGE'),
            OutputLine(type='success', text=f'api-7c7c7f7c85-8xw2v          1/1     Running   0          12m   # ns={namespace}'),
            OutputLine(type='success', text=f'worker-6d9b87f48c-4c9p7       1/1     Running   0          12m   # ns={namespace}'),
        ]

    def _docker_build(self, command: str, match: re.Match[str]) -> list[OutputLine]:
        return [
            OutputLine(type='output', text='Sending build context to Docker daemon  52.3kB'),
            OutputLine(type='output', text='Step 1/5 : FROM node:20-alpine'),
            OutputLine(type='output', text=' ---> 6c8c6f1a'),
            OutputLine(type='success', text='Successfully tagged app:latest'),
        ]
