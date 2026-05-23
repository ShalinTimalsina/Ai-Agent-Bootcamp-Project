import {
    Boxes,
    Gauge,
    GitBranch,
    GraduationCap,
    Layers,
    Package,
    TerminalSquare
} from 'lucide-react'
import { cn } from '@/shared/lib/cn.js'

const NAV = [
    { id: 'dashboard', label: 'Dashboard', icon: Gauge, badge: 'New' },
    { id: 'lessons', label: 'Lessons', icon: GraduationCap },
    { id: 'terminal', label: 'Terminal Practice', icon: TerminalSquare },
    { id: 'examples', label: 'Code Examples', icon: Boxes }
]

const TRACKS = [
    { id: 'docker', label: 'Docker', icon: Package, disabled: true },
    { id: 'k8s', label: 'Kubernetes', icon: Layers, disabled: true },
    { id: 'cicd', label: 'CI/CD', icon: GitBranch, disabled: true }
]

function NavItem({ active, icon: Icon, label, badge, disabled, onClick }) {
    return (
        <button
            type="button"
            onClick={onClick}
            disabled={disabled}
            className={cn(
                'group flex w-full items-center gap-2 rounded-xl px-3 py-2 text-left transition',
                'hover:bg-card/60 hover:shadow-soft',
                active ? 'bg-card shadow-soft' : 'bg-transparent',
                disabled && 'cursor-not-allowed opacity-50 hover:bg-transparent hover:shadow-none'
            )}
        >
            <Icon className={cn('h-4 w-4', active ? 'text-accent' : 'text-text2 group-hover:text-text')} />
            <span className={cn('text-sm font-medium', active ? 'text-text' : 'text-text2 group-hover:text-text')}>
                {label}
            </span>
            {badge ? (
                <span className="ml-auto rounded-full bg-accent/15 px-2 py-0.5 text-[11px] font-semibold text-accent">
                    {badge}
                </span>
            ) : null}
        </button>
    )
}

export function Sidebar({ activeView, onChangeView, className }) {
    return (
        <aside
            className={cn(
                'w-[280px] shrink-0 border-r border-border/70 bg-bg2/60 p-4 backdrop-blur',
                className
            )}
        >
            <div className="flex items-center gap-2 px-2 py-2">
                <div className="grid h-9 w-9 place-items-center rounded-xl bg-accent/15">
                    <span className="font-mono text-sm font-semibold text-accent">$</span>
                </div>
                <div className="min-w-0">
                    <div className="truncate text-sm font-semibold">DevOps Academy</div>
                    <div className="truncate text-xs text-muted">Learn • Practice • Ship</div>
                </div>
            </div>

            <div className="mt-5 space-y-1">
                {NAV.map((item) => (
                    <NavItem
                        key={item.id}
                        active={activeView === item.id}
                        icon={item.icon}
                        label={item.label}
                        badge={item.badge}
                        disabled={item.disabled}
                        onClick={() => onChangeView(item.id)}
                    />
                ))}
            </div>

            <div className="mt-6 px-2">
                <div className="text-xs font-semibold uppercase tracking-wider text-muted">Tracks</div>
            </div>

            <div className="mt-2 space-y-1">
                {TRACKS.map((item) => (
                    <NavItem
                        key={item.id}
                        active={activeView === item.id}
                        icon={item.icon}
                        label={item.label}
                        disabled={item.disabled}
                        onClick={() => onChangeView(item.id)}
                    />
                ))}
            </div>

            <div className="mt-auto" />

            <div className="mt-6 rounded-2xl border border-border/60 bg-card/40 p-4 shadow-card">
                <div className="flex items-start gap-3">
                    <div className="mt-0.5 grid h-8 w-8 place-items-center rounded-xl bg-accent2/15">
                        <TerminalSquare className="h-4 w-4 text-accent2" />
                    </div>
                    <div className="min-w-0">
                        <div className="text-sm font-semibold">Terminal-first learning</div>
                        <p className="mt-1 text-xs leading-relaxed text-muted">
                            Practice commands in a realistic terminal. Copy/paste friendly. Built for clarity.
                        </p>
                    </div>
                </div>
            </div>
        </aside>
    )
}
