/** @type {import('tailwindcss').Config} */
export default {
    content: ['./index.html', './src/**/*.{js,jsx}'],
    theme: {
        extend: {
            colors: {
                bg: 'hsl(var(--bg) / <alpha-value>)',
                bg2: 'hsl(var(--bg2) / <alpha-value>)',
                card: 'hsl(var(--card) / <alpha-value>)',
                text: 'hsl(var(--text) / <alpha-value>)',
                text2: 'hsl(var(--text2) / <alpha-value>)',
                muted: 'hsl(var(--muted) / <alpha-value>)',
                border: 'hsl(var(--border) / <alpha-value>)',
                accent: 'hsl(var(--accent) / <alpha-value>)',
                accent2: 'hsl(var(--accent2) / <alpha-value>)',
                warn: 'hsl(var(--warn) / <alpha-value>)',
                danger: 'hsl(var(--danger) / <alpha-value>)'
            },
            fontFamily: {
                sans: ['var(--font-sans)'],
                mono: ['var(--font-mono)']
            },
            boxShadow: {
                soft: '0 10px 30px -18px rgba(0,0,0,0.55)',
                card: '0 16px 40px -22px rgba(0,0,0,0.6)'
            }
        }
    },
    plugins: []
}
