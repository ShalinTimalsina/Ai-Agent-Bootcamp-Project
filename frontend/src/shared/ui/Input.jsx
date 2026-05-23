import { cn } from '@/shared/lib/cn.js'

export function Input({ className, ...props }) {
    return (
        <input
            className={cn(
                'h-10 w-full rounded-xl border border-border/70 bg-bg2/60 px-3 text-sm text-text shadow-soft',
                'placeholder:text-muted',
                'focus:outline-none focus-visible:border-accent/60 focus-visible:ring-2 focus-visible:ring-accent/25',
                className
            )}
            {...props}
        />
    )
}
