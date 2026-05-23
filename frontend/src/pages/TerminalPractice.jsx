import { useMemo, useRef, useState } from 'react'
import { Terminal } from '@/features/terminal/components/Terminal.jsx'
import { Badge } from '@/shared/ui/Badge.jsx'
import { Button } from '@/shared/ui/Button.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/shared/ui/Card.jsx'
import { Input } from '@/shared/ui/Input.jsx'

function nowStamp() {
    const d = new Date()
    return d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
}

function simulate(command) {
    const cmd = String(command ?? '').trim()
    if (!cmd) return []

    const lower = cmd.toLowerCase()

    if (lower === 'help' || lower === '?') {
        return [
            { type: 'muted', text: `Commands: help, clear, docker ps, kubectl get pods, echo <text>` },
            { type: 'muted', text: `Tip: Try “docker ps” then “kubectl get pods -n platform”.` }
        ]
    }

    if (lower === 'clear') {
        return [{ type: 'muted', text: '__CLEAR__' }]
    }

    if (lower.startsWith('echo ')) {
        return [{ type: 'output', text: cmd.slice(5) }]
    }

    if (lower === 'docker ps') {
        return [
            { type: 'output', text: 'CONTAINER ID   IMAGE          COMMAND                  STATUS        PORTS     NAMES' },
            { type: 'output', text: 'b1a2c3d4e5f6   nginx:alpine   "nginx -g \'daemon…"   Up 7 minutes  80/tcp    web' }
        ]
    }

    if (lower.startsWith('kubectl get pods')) {
        return [
            { type: 'success', text: 'NAME                         READY   STATUS    RESTARTS   AGE' },
            { type: 'success', text: 'api-7c7c7f7c85-8xw2v          1/1     Running   0          12m' },
            { type: 'success', text: 'worker-6d9b87f48c-4c9p7       1/1     Running   0          12m' }
        ]
    }

    if (lower === 'docker build -t app .' || lower === 'docker build -t app .') {
        return [
            { type: 'output', text: 'Sending build context to Docker daemon  52.3kB' },
            { type: 'output', text: 'Step 1/5 : FROM node:20-alpine' },
            { type: 'output', text: ' ---> 6c8c6f1a' },
            { type: 'success', text: 'Successfully tagged app:latest' }
        ]
    }

    return [
        { type: 'warning', text: `Unknown command: ${cmd}` },
        { type: 'muted', text: `Type “help” to see supported commands.` }
    ]
}

export function TerminalPractice() {
    const [command, setCommand] = useState('')
    const [lines, setLines] = useState(() => [
        { type: 'muted', text: `practice terminal · ${nowStamp()} · type “help”` }
    ])

    const scrollHint = useRef(0)

    const terminalLines = useMemo(() => {
        // Support a special pseudo-line to clear the terminal.
        const cleared = []
        for (const l of lines) {
            if (l.type === 'muted' && l.text === '__CLEAR__') {
                cleared.length = 0
                continue
            }
            cleared.push(l)
        }
        return cleared
    }, [lines])

    function run() {
        const cmd = command.trim()
        if (!cmd) return

        setLines((prev) => [
            ...prev,
            { type: 'command', text: cmd },
            ...simulate(cmd)
        ])
        setCommand('')
        scrollHint.current++
    }

    return (
        <div className="space-y-6">
            <div className="flex flex-col gap-2 sm:flex-row sm:items-end sm:justify-between">
                <div>
                    <div className="text-2xl font-semibold tracking-tight">Terminal practice</div>
                    <p className="mt-1 text-sm text-muted">
                        A VS Code-style terminal you can use for interactive drills.
                    </p>
                </div>

                <div className="flex items-center gap-2">
                    <Badge variant="info">Interactive</Badge>
                    <Badge>bash</Badge>
                </div>
            </div>

            <Card>
                <CardHeader>
                    <CardTitle>Practice session</CardTitle>
                    <CardDescription>
                        Run commands and read output with clear, high-contrast syntax tones.
                    </CardDescription>
                </CardHeader>
                <CardContent>
                    <Terminal title="practice: local" lines={terminalLines} height={420} hint="bash" />

                    <div className="mt-4 flex flex-col gap-2 sm:flex-row">
                        <Input
                            value={command}
                            onChange={(e) => setCommand(e.target.value)}
                            onKeyDown={(e) => {
                                if (e.key === 'Enter') run()
                            }}
                            placeholder="Type a command (try: help, docker ps, kubectl get pods -n platform)"
                            className="flex-1 font-mono"
                        />
                        <Button onClick={run}>Run</Button>
                        <Button
                            variant="secondary"
                            onClick={() => setLines([{ type: 'muted', text: `practice terminal · ${nowStamp()} · type “help”` }])}
                        >
                            Reset
                        </Button>
                    </div>
                </CardContent>
            </Card>
        </div>
    )
}
