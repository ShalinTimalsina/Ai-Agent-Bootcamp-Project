import { createContext, useCallback, useContext, useEffect, useMemo, useState } from 'react'
import { isValidThemeId, THEMES } from '@/shared/theme/theme.js'

const STORAGE_KEY = 'devops.ui.theme'

const ThemeContext = createContext(null)

function applyThemeToDocument(themeId) {
    const root = document.documentElement
    root.classList.remove(THEMES.dark.className, THEMES.dim.className, THEMES.light.className)
    const theme = THEMES[themeId] ?? THEMES.dark
    root.classList.add(theme.className)
}

export function ThemeProvider({ children }) {
    const [themeId, setThemeId] = useState(() => {
        const saved = localStorage.getItem(STORAGE_KEY)
        return isValidThemeId(saved) ? saved : 'dark'
    })

    useEffect(() => {
        applyThemeToDocument(themeId)
        localStorage.setItem(STORAGE_KEY, themeId)
    }, [themeId])

    const setTheme = useCallback((nextThemeId) => {
        setThemeId(isValidThemeId(nextThemeId) ? nextThemeId : 'dark')
    }, [])

    const value = useMemo(() => ({ themeId, setTheme }), [themeId, setTheme])

    return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>
}

export function useTheme() {
    const ctx = useContext(ThemeContext)
    if (!ctx) throw new Error('useTheme must be used inside <ThemeProvider>')
    return ctx
}
