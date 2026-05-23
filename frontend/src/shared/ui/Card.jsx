import { cn } from '@/shared/lib/cn.js'

export function Card({ className, ...props }) {
    return (
        <div
            className={cn(
                'rounded-2xl border border-border/70 bg-card/70 shadow-card',
                'backdrop-blur-sm',
                className
            )}
            {...props}
        />
    )
}

export function CardHeader({ className, ...props }) {
    return <div className={cn('px-5 pt-5', className)} {...props} />
}

export function CardTitle({ className, ...props }) {
    return <div className={cn('text-base font-semibold text-text', className)} {...props} />
}

export function CardDescription({ className, ...props }) {
    return <div className={cn('mt-1 text-sm text-muted', className)} {...props} />
}

export function CardContent({ className, ...props }) {
    return <div className={cn('px-5 pb-5 pt-4', className)} {...props} />
}
