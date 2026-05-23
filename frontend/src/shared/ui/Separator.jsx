import { cn } from '@/shared/lib/cn.js'

export function Separator({ className }) {
    return <div className={cn('h-px w-full bg-border/70', className)} />
}
