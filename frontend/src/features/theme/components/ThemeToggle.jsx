import { Moon, Sun, Sunset } from 'lucide-react'
import { useTheme } from '@/app/providers/ThemeProvider.jsx'
import { cn } from '@/shared/lib/cn.js'

const OPTIONS = [
    { id: 'dark', label: 'Dark', icon: Moon },
    { id: 'dim', label: 'Dim', icon: Sunset },
    { id: 'light', label: 'Light', icon: Sun }
]

export function ThemeToggle() {
    const { themeId, setTheme } = useTheme()

    return (
        <div className="flex items-center rounded-xl border border-border/70 bg-card/30 p-1 shadow-soft">
            {OPTIONS.map((opt) => {
                const Icon = opt.icon
                const active = themeId === opt.id
                return (
                    <button
                        key={opt.id}
                        type="button"
                        onClick={() => setTheme(opt.id)}
                        className={cn(
                            'flex items-center gap-2 rounded-lg px-2.5 py-1.5 text-xs font-semibold transition',
                            active
                                ? 'bg-accent/15 text-accent'
                                : 'text-text2 hover:bg-card/60 hover:text-text'
                        )}
                        aria-pressed={active}
                    >
                        <Icon className="h-4 w-4" />
                        <span className="hidden md:inline">{opt.label}</span>
                    </button>
                )
            })}
        </div>
    )
}
