import { useMemo, useState } from 'react'
import Highlight, { defaultProps } from 'prism-react-renderer'
import { Copy, Check } from 'lucide-react'
import { cn } from '@/shared/lib/cn.js'

export function CodeBlock({ code, language = 'bash', className, title }) {
    const [copied, setCopied] = useState(false)
    const safeCode = useMemo(() => String(code ?? '').trimEnd(), [code])

    async function onCopy() {
        try {
            await navigator.clipboard.writeText(safeCode)
            setCopied(true)
            window.setTimeout(() => setCopied(false), 900)
        } catch {
            // ignore
        }
    }

    return (
        <div className={cn('overflow-hidden rounded-2xl border border-border/70 bg-bg2/40 shadow-card', className)}>
            <div className="flex items-center justify-between gap-3 border-b border-border/60 px-4 py-3">
                <div className="min-w-0">
                    <div className="truncate text-xs font-semibold text-text2">{title ?? 'Code'}</div>
                    <div className="text-[11px] text-muted">{language}</div>
                </div>
                <button
                    type="button"
                    onClick={onCopy}
                    className="inline-flex items-center gap-2 rounded-xl border border-border/70 bg-card/40 px-3 py-2 text-xs font-semibold text-text2 shadow-soft transition hover:bg-card hover:text-text"
                >
                    {copied ? <Check className="h-4 w-4 text-accent2" /> : <Copy className="h-4 w-4" />}
                    {copied ? 'Copied' : 'Copy'}
                </button>
            </div>

            <Highlight {...defaultProps} code={safeCode} language={language}>
                {({ className: hlClass, tokens, getLineProps, getTokenProps }) => (
                    <pre
                        className={cn(
                            hlClass,
                            'overflow-auto p-4 font-mono text-[13px] leading-relaxed',
                            'bg-transparent text-text'
                        )}
                        style={{ background: 'transparent' }}
                    >
                        {tokens.map((line, i) => (
                            <div key={i} {...getLineProps({ line })}>
                                <span className="mr-4 select-none text-muted">{String(i + 1).padStart(2, '0')}</span>
                                {line.map((token, key) => {
                                    const tokenProps = getTokenProps({ token })
                                    // Prism injects inline styles; we ignore them and drive color via Tailwind.
                                    // eslint-disable-next-line no-unused-vars
                                    const { style: _style, ...rest } = tokenProps

                                    return (
                                        <span
                                            key={key}
                                            {...rest}
                                            className={cn(
                                                tokenProps.className,
                                                'text-text2',
                                                token.types.includes('comment') && 'text-muted',
                                                token.types.includes('string') && 'text-accent2',
                                                token.types.includes('keyword') && 'text-accent',
                                                token.types.includes('function') && 'text-accent',
                                                token.types.includes('number') && 'text-warn'
                                            )}
                                        />
                                    )
                                })}
                            </div>
                        ))}
                    </pre>
                )}
            </Highlight>
        </div>
    )
}
