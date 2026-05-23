import { useMemo, useState } from 'react'
import { AppShell } from '@/app/layout/AppShell.jsx'
import { CodeExamples } from '@/pages/CodeExamples.jsx'
import { Dashboard } from '@/pages/Dashboard.jsx'
import { Lessons } from '@/pages/Lessons.jsx'
import { TerminalPractice } from '@/pages/TerminalPractice.jsx'

const VIEWS = {
    dashboard: 'dashboard',
    lessons: 'lessons',
    terminal: 'terminal',
    examples: 'examples'
}

export default function App() {
    const [view, setView] = useState(VIEWS.dashboard)

    const content = useMemo(() => {
        switch (view) {
            case VIEWS.lessons:
                return <Lessons />
            case VIEWS.terminal:
                return <TerminalPractice />
            case VIEWS.examples:
                return <CodeExamples />
            case VIEWS.dashboard:
            default:
                return <Dashboard />
        }
    }, [view])

    return (
        <AppShell activeView={view} onChangeView={setView}>
            {content}
        </AppShell>
    )
}
