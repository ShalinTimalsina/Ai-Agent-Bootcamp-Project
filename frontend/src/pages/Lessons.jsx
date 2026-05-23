import { BookOpen, Filter } from 'lucide-react'
import { Badge } from '@/shared/ui/Badge.jsx'
import { Button } from '@/shared/ui/Button.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/shared/ui/Card.jsx'
import { Input } from '@/shared/ui/Input.jsx'

const LESSONS = [
    {
        id: 'docker-basics',
        title: 'Docker basics: images & containers',
        description: 'Understand the mental model: image → container, layers, tags.',
        tag: 'Docker',
        level: 'Beginner',
        minutes: 14
    },
    {
        id: 'k8s-pods',
        title: 'Kubernetes pods & deployments',
        description: 'Why pods exist and how deployments manage replicas safely.',
        tag: 'Kubernetes',
        level: 'Intermediate',
        minutes: 18
    },
    {
        id: 'cicd-pipelines',
        title: 'CI/CD pipelines that don’t lie',
        description: 'Build, test, and deploy with signals you can trust.',
        tag: 'CI/CD',
        level: 'Beginner',
        minutes: 16
    }
]

export function Lessons() {
    return (
        <div className="space-y-6">
            <div className="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
                <div>
                    <div className="flex items-center gap-2 text-2xl font-semibold tracking-tight">
                        <BookOpen className="h-6 w-6 text-accent" /> Lessons
                    </div>
                    <p className="mt-1 text-sm text-muted">
                        High-contrast, low-strain lesson cards. Built for long sessions.
                    </p>
                </div>

                <div className="flex w-full flex-col gap-2 sm:w-auto sm:flex-row sm:items-center">
                    <Input placeholder="Search lessons…" className="sm:w-[320px]" />
                    <Button variant="secondary" leftIcon={Filter}>
                        Filters
                    </Button>
                </div>
            </div>

            <div className="grid gap-4 lg:grid-cols-2">
                {LESSONS.map((l) => (
                    <Card key={l.id} className="transition hover:-translate-y-0.5 hover:border-accent/30">
                        <CardHeader>
                            <CardTitle className="flex items-center justify-between gap-3">
                                <span className="truncate">{l.title}</span>
                                <Badge variant="info" className="shrink-0">
                                    {l.tag}
                                </Badge>
                            </CardTitle>
                            <CardDescription>{l.description}</CardDescription>
                        </CardHeader>
                        <CardContent>
                            <div className="flex flex-wrap items-center gap-2 text-xs text-muted">
                                <span className="rounded-full border border-border/70 bg-bg2/40 px-2 py-1">
                                    {l.level}
                                </span>
                                <span className="rounded-full border border-border/70 bg-bg2/40 px-2 py-1">
                                    {l.minutes} min
                                </span>
                            </div>

                            <div className="mt-4 flex items-center gap-2">
                                <Button size="sm">Open</Button>
                                <Button size="sm" variant="ghost">
                                    Save
                                </Button>
                            </div>
                        </CardContent>
                    </Card>
                ))}
            </div>
        </div>
    )
}
