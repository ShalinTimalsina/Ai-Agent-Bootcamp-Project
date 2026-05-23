import { X } from 'lucide-react'
import { Sidebar } from './Sidebar.jsx'

export function MobileSidebar({ open, onClose, activeView, onChangeView }) {
    if (!open) return null

    return (
        <div className="fixed inset-0 z-50 xl:hidden">
            <div
                className="absolute inset-0 bg-black/60"
                onClick={onClose}
                aria-hidden="true"
            />

            <div className="absolute left-0 top-0 h-full w-[320px] max-w-[90vw]">
                <div className="relative h-full">
                    <div className="absolute right-3 top-3 z-10">
                        <button
                            type="button"
                            onClick={onClose}
                            className="grid h-10 w-10 place-items-center rounded-xl border border-border/70 bg-card/60 text-text2 shadow-soft transition hover:bg-card hover:text-text"
                            aria-label="Close navigation"
                        >
                            <X className="h-4 w-4" />
                        </button>
                    </div>

                    <div className="h-full overflow-auto">
                        <Sidebar
                            className="block"
                            activeView={activeView}
                            onChangeView={(v) => {
                                onChangeView(v)
                                onClose()
                            }}
                        />
                    </div>
                </div>
            </div>
        </div>
    )
}
