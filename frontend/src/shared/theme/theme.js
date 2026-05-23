export const THEMES = {
    dark: { id: 'dark', label: 'Dark', className: 'theme-dark' },
    dim: { id: 'dim', label: 'Dim', className: 'theme-dim' },
    light: { id: 'light', label: 'Light', className: 'theme-light' }
}

export const THEME_ORDER = [THEMES.dark, THEMES.dim, THEMES.light]

export function isValidThemeId(themeId) {
    return themeId === 'dark' || themeId === 'dim' || themeId === 'light'
}
