import { ArrowRight, Play, TerminalSquare } from 'lucide-react'
import { Terminal } from '@/features/terminal/components/Terminal.jsx'
import { CodeBlock } from '@/shared/code/CodeBlock.jsx'
import { Badge } from '@/shared/ui/Badge.jsx'
import { Button } from '@/shared/ui/Button.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/shared/ui/Card.jsx'

const terminalLines = [
    { type: 'muted', text: 'Tip: Your goal is to understand the output, not just run commands.' },
    { type: 'command', text: 'docker ps' },
    { type: 'output', text: 'CONTAINER ID   IMAGE        COMMAND                  STATUS        PORTS     NAMES' },
    { type: 'output', text: 'b1a2c3d4e5f6   nginx:alpine  "nginx -g \'daemon…"   Up 2 minutes  80/tcp    web' },
    { type: 'command', text: 'kubectl get pods -n platform' },
    { type: 'success', text: 'NAME                         READY   STATUS    RESTARTS   AGE' },
    { type: 'success', text: 'api-7c7c7f7c85-8xw2v          1/1     Running   0          3m' },
    { type: 'success', text: 'worker-6d9b87f48c-4c9p7       1/1     Running   0          3m' }
]

const lessonCode = `# Build a minimal container image
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
CMD ["npm", "start"]
`

export function Dashboard() {
    return (
        <div className="space-y-6">
            <div className="flex flex-col gap-2 sm:flex-row sm:items-end sm:justify-between">
                <div>
                    <div className="text-2xl font-semibold tracking-tight">Welcome back</div>
                    <p className="mt-1 text-sm text-muted">
                        A modern, readable DevOps learning dashboard — inspired by VS Code + GitHub Dark.
                    </p>
                </div>
                <div className="flex items-center gap-2">
                    <Button variant="secondary" leftIcon={Play}>
                        Continue lesson
                    </Button>
                    <Button rightIcon={ArrowRight}>Start practice</Button>
                </div>
            </div>

            <div className="grid gap-4 lg:grid-cols-3">
                <Card>
                    <CardHeader>
                        <CardTitle className="flex items-center justify-between">
                            Next up
                            <Badge variant="info">Docker</Badge>
                        </CardTitle>
                        <CardDescription>Containers: images, layers, and tagging</CardDescription>
                    </CardHeader>
                    <CardContent>
                        <div className="text-sm text-text2">
                            You’re 62% through the <span className="font-semibold text-text">Containers</span> track.
                        </div>
                        <div className="mt-4 flex items-center gap-2">
                            <Button size="sm">Resume</Button>
                            <Button size="sm" variant="ghost">
                                View syllabus
                            </Button>
                        </div>
                    </CardContent>
                </Card>

                <Card>
                    <CardHeader>
                        <CardTitle className="flex items-center justify-between">
                            Learning streak
                            <Badge variant="success">+1 day</Badge>
                        </CardTitle>
                        <CardDescription>Consistency beats intensity</CardDescription>
                    </CardHeader>
                    <CardContent>
                        <div className="text-3xl font-semibold">4</div>
                        <div className="mt-1 text-sm text-muted">days in a row</div>
                        <div className="mt-4 text-xs text-muted">
                            Keep it fun: practice one command, understand one output.
                        </div>
                    </CardContent>
                </Card>

                <Card>
                    <CardHeader>
                        <CardTitle className="flex items-center justify-between">
                            Environment
                            <Badge>Local</Badge>
                        </CardTitle>
                        <CardDescription>Ready for hands-on practice</CardDescription>
                    </CardHeader>
                    <CardContent>
                        <div className="text-sm text-text2">
                            Docker: <span className="text-text">Running</span>
                        </div>
                        <div className="mt-1 text-sm text-text2">
                            Kubernetes: <span className="text-text">Connected</span>
                        </div>
                        <div className="mt-1 text-sm text-text2">
                            CI/CD: <span className="text-muted">Coming soon</span>
                        </div>
                    </CardContent>
                </Card>
            </div>

            <div className="grid gap-6 lg:grid-cols-2">
                <div className="space-y-4">
                    <Card>
                        <CardHeader>
                            <CardTitle className="flex items-center gap-2">
                                <TerminalSquare className="h-5 w-5 text-accent" /> Terminal practice
                            </CardTitle>
                            <CardDescription>VS Code-style terminal with readable, colored output.</CardDescription>
                        </CardHeader>
                        <CardContent>
                            <Terminal title="practice: local" lines={terminalLines} height={360} hint="bash" />
                        </CardContent>
                    </Card>
                </div>

                <div className="space-y-4">
                    <Card>
                        <CardHeader>
                            <CardTitle>Code example</CardTitle>
                            <CardDescription>Clear typography + syntax styling that doesn’t hurt your eyes.</CardDescription>
                        </CardHeader>
                        <CardContent>
                            <CodeBlock title="Dockerfile" language="bash" code={lessonCode} />
                        </CardContent>
                    </Card>

                    <Card>
                        <CardHeader>
                            <CardTitle>Today’s lesson queue</CardTitle>
                            <CardDescription>Quick wins for busy schedules.</CardDescription>
                        </CardHeader>
                        <CardContent>
                            <div className="space-y-3">
                                {[
                                    { title: 'Docker: Image layers explained', meta: '12 min • Beginner', badge: 'Docker' },
                                    { title: 'Kubernetes: Deployments vs Pods', meta: '15 min • Intermediate', badge: 'K8s' },
                                    { title: 'CI/CD: Build & test pipeline basics', meta: '10 min • Beginner', badge: 'CI/CD' }
                                ].map((l) => (
                                    <div
                                        key={l.title}
                                        className="flex items-center justify-between rounded-xl border border-border/60 bg-card/40 px-4 py-3 transition hover:bg-card/60"
                                    >
                                        <div className="min-w-0">
                                            <div className="truncate text-sm font-semibold text-text">{l.title}</div>
                                            <div className="mt-0.5 text-xs text-muted">{l.meta}</div>
                                        </div>
                                        <Badge className="shrink-0">{l.badge}</Badge>
                                    </div>
                                ))}
                            </div>
                        </CardContent>
                    </Card>
                </div>
            </div>
        </div>
    )
}
