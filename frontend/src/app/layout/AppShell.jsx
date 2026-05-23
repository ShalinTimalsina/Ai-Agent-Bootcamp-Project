import { useState } from 'react'
import { MobileSidebar } from './MobileSidebar.jsx'
import { Sidebar } from './Sidebar.jsx'
import { TopNav } from './TopNav.jsx'

export function AppShell({ activeView, onChangeView, children }) {
    const [mobileNavOpen, setMobileNavOpen] = useState(false)

    return (
        <div className="min-h-screen bg-bg text-text">
            <div className="mx-auto flex min-h-screen w-full max-w-[1600px]">
                <Sidebar className="hidden xl:block" activeView={activeView} onChangeView={onChangeView} />

                <MobileSidebar
                    open={mobileNavOpen}
                    onClose={() => setMobileNavOpen(false)}
                    activeView={activeView}
                    onChangeView={onChangeView}
                />

                <div className="flex min-w-0 flex-1 flex-col">
                    <TopNav onOpenSidebar={() => setMobileNavOpen(true)} />
                    <main className="min-w-0 flex-1 p-4 sm:p-6 lg:p-8">
                        <div className="mx-auto w-full max-w-6xl">{children}</div>
                    </main>
                </div>
            </div>
        </div>
    )
}
