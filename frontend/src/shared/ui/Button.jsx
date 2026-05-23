import { cn } from '@/shared/lib/cn.js'

const VARIANTS = {
    primary: 'bg-accent text-bg hover:bg-accent/90 active:bg-accent/85',
    secondary: 'bg-card text-text hover:bg-card/70 active:bg-card/60 border border-border/70',
    outline: 'border border-border/80 bg-transparent text-text hover:bg-card/40',
    ghost: 'bg-transparent text-text2 hover:bg-card/50 hover:text-text',
    danger: 'bg-danger text-white hover:bg-danger/90 active:bg-danger/85'
}

const SIZES = {
    sm: 'h-9 px-3 text-sm',
    md: 'h-10 px-4 text-sm',
    lg: 'h-11 px-5 text-sm'
}

export function Button({
    className,
    variant = 'primary',
    size = 'md',
    leftIcon: LeftIcon,
    rightIcon: RightIcon,
    ...props
}) {
    return (
        <button
            className={cn(
                'inline-flex items-center justify-center gap-2 rounded-xl font-semibold shadow-soft transition',
                'focus:outline-none focus-visible:ring-2 focus-visible:ring-accent/60 focus-visible:ring-offset-0',
                VARIANTS[variant],
                SIZES[size],
                className
            )}
            {...props}
        >
            {LeftIcon ? <LeftIcon className="h-4 w-4" /> : null}
            {props.children}
            {RightIcon ? <RightIcon className="h-4 w-4" /> : null}
        </button>
    )
}
