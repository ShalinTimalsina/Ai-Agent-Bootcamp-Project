import { useMemo } from 'react'
import { cn } from '@/shared/lib/cn.js'

/**
 * Terminal line types:
 * - command: user command input
 * - output: normal output
 * - success: success output
 * - warning: warning output
 * - error: error output
 * - muted: secondary output (tips)
 */

function Line({ line }) {
    const tone =
        line.type === 'command'
            ? 'text-accent'
            : line.type === 'success'
                ? 'text-accent2'
                : line.type === 'warning'
                    ? 'text-warn'
                    : line.type === 'error'
                        ? 'text-danger'
                        : line.type === 'muted'
                            ? 'text-[hsl(var(--terminalMuted))]'
                            : 'text-[hsl(var(--terminalText))]'

    if (line.type === 'command') {
        // Small, readable command highlighting: prompt vs command vs args.
        const parts = String(line.text ?? '').trim().split(/\s+/)
        const cmd = parts[0] ?? ''
        const args = parts.slice(1).join(' ')

        return (
            <div className={cn('flex gap-2', tone)}>
                <span className="select-none text-[hsl(var(--terminalMuted))]">$</span>
                <span className="font-semibold text-accent">{cmd}</span>
                {args ? <span className="text-[hsl(var(--terminalText))]">{args}</span> : null}
            </div>
        )
    }

    return <div className={cn('whitespace-pre-wrap', tone)}>{line.text}</div>
}

export function Terminal({
    title = 'Terminal',
    lines = [],
    className,
    height = 340,
    hint
}) {
    const safeLines = useMemo(() => (Array.isArray(lines) ? lines : []), [lines])

    return (
        <div
            className={cn(
                'overflow-hidden rounded-2xl border border-[hsl(var(--terminalBorder))] bg-[hsl(var(--terminal))] shadow-card',
                className
            )}
            style={{ height }}
        >
            <div className="flex items-center gap-3 border-b border-white/10 bg-[hsl(var(--terminalBar))] px-4 py-3">
                <div className="flex items-center gap-2">
                    <span className="h-3 w-3 rounded-full bg-[#ff5f56]" />
                    <span className="h-3 w-3 rounded-full bg-[#ffbd2e]" />
                    <span className="h-3 w-3 rounded-full bg-[#27c93f]" />
                </div>
                <div className="min-w-0 flex-1">
                    <div className="truncate font-mono text-xs font-semibold text-white/85">{title}</div>
                </div>
                {hint ? <div className="text-xs text-white/55">{hint}</div> : null}
            </div>

            <div className="h-full overflow-auto px-4 py-4 font-mono text-[13px] leading-relaxed">
                <div className="space-y-2">
                    {safeLines.map((line, idx) => (
                        <Line key={idx} line={line} />
                    ))}
                </div>
            </div>
        </div>
    )
}
