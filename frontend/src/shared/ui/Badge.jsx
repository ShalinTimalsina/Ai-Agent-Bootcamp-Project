import { cn } from '@/shared/lib/cn.js'

export function Badge({ className, variant = 'default', ...props }) {
    const variants = {
        default: 'bg-card/70 text-text2 border-border/70',
        info: 'bg-accent/15 text-accent border-accent/25',
        success: 'bg-accent2/15 text-accent2 border-accent2/25',
        warn: 'bg-warn/15 text-warn border-warn/25',
        danger: 'bg-danger/15 text-danger border-danger/25'
    }

    return (
        <span
            className={cn(
                'inline-flex items-center rounded-full border px-2 py-0.5 text-[11px] font-semibold',
                variants[variant],
                className
            )}
            {...props}
        />
    )
}
