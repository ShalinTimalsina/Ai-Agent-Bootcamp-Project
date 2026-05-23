import { Bell, Menu, Search, Sparkles } from 'lucide-react'
import { ThemeToggle } from '@/features/theme/components/ThemeToggle.jsx'
import { Input } from '@/shared/ui/Input.jsx'

export function TopNav({ onOpenSidebar }) {
    return (
        <header className="sticky top-0 z-20 border-b border-border/70 bg-bg/70 backdrop-blur">
            <div className="mx-auto flex h-16 w-full max-w-[1600px] items-center gap-3 px-4 sm:px-6 lg:px-8">
                <button
                    type="button"
                    onClick={onOpenSidebar}
                    className="grid h-10 w-10 place-items-center rounded-xl border border-border/70 bg-card/40 text-text2 shadow-soft transition hover:bg-card hover:text-text xl:hidden"
                    aria-label="Open navigation"
                >
                    <Menu className="h-4 w-4" />
                </button>

                <div className="flex items-center gap-2">
                    <div className="grid h-9 w-9 place-items-center rounded-xl bg-card shadow-soft">
                        <Sparkles className="h-4 w-4 text-accent" />
                    </div>
                    <div className="hidden sm:block">
                        <div className="text-sm font-semibold">DevOps Dashboard</div>
                        <div className="text-xs text-muted">Ship confidently — with readable UI.</div>
                    </div>
                </div>

                <div className="mx-auto hidden w-full max-w-xl items-center sm:flex">
                    <div className="relative w-full">
                        <Search className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted" />
                        <Input className="w-full pl-9" placeholder="Search lessons, commands, topics…" />
                    </div>
                </div>

                <div className="ml-auto flex items-center gap-2">
                    <ThemeToggle />

                    <button
                        type="button"
                        className="grid h-10 w-10 place-items-center rounded-xl border border-border/70 bg-card/40 text-text2 shadow-soft transition hover:bg-card hover:text-text"
                        aria-label="Notifications"
                    >
                        <Bell className="h-4 w-4" />
                    </button>

                    <div className="hidden sm:flex items-center gap-2 rounded-xl border border-border/70 bg-card/40 px-3 py-2 shadow-soft">
                        <div className="grid h-7 w-7 place-items-center rounded-lg bg-accent/15 font-mono text-xs font-semibold text-accent">
                            LO
                        </div>
                        <div className="leading-tight">
                            <div className="text-xs font-semibold">Learner</div>
                            <div className="text-[11px] text-muted">Free plan</div>
                        </div>
                    </div>
                </div>
            </div>
        </header>
    )
}
