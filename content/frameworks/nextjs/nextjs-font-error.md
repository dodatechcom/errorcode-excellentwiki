---
title: "[Solution] Next.js Font Loading Error — How to Fix"
description: "Fix Next.js font loading errors. Resolve custom font, font display, and font optimization issues in Next.js."
frameworks: ["nextjs"]
error-types: ["configuration-error"]
severities: ["error"]
weight: 5
comments: true
---

A Next.js font loading error occurs when custom fonts fail to load, display incorrectly, or cause layout shifts. Next.js provides built-in font optimization with `next/font` to prevent layout shifts.

## Why It Happens

Font loading errors occur when the font file path is incorrect, when the font format is not supported, when `next/font` is misconfigured, when external font CDNs are blocked, when font-display strategy causes visual issues, or when CSS font-face declarations conflict with the font optimization.

## Common Error Messages

```
Error: Font file not found: /fonts/inter.woff2
```

```
Error: Invalid font weight: "900" for font "Inter"
```

```
Failed to fetch font: https://fonts.googleapis.com/css2?family=Inter
```

```
Error: next/font/google requires a "family" parameter
```

## How to Fix It

### 1. Use next/font for Local Fonts

Load local fonts with optimization:

```typescript
// app/layout.tsx
import { Inter, Roboto } from 'next/font/google';
import localFont from 'next/font/local';

const inter = Inter({
    subsets: ['latin'],
    display: 'swap',
    variable: '--font-inter',
});

const roboto = Roboto({
    weight: ['400', '700'],
    subsets: ['latin'],
    display: 'swap',
});

const myLocalFont = localFont({
    src: './fonts/my-font.woff2',
    display: 'swap',
    variable: '--font-local',
});

export default function RootLayout({ children }) {
    return (
        <html lang="en" className={`${inter.variable} ${roboto.variable}`}>
            <body className={inter.className}>
                {children}
            </body>
        </html>
    );
}
```

### 2. Use Google Fonts

Load fonts from Google Fonts:

```typescript
// app/layout.tsx
import { Roboto_Mono, Source_Sans_Pro } from 'next/font/google';

const robotoMono = Roboto_Mono({
    subsets: ['latin'],
    display: 'swap',
    weight: ['400', '700'],
    variable: '--font-mono',
});

const sourceSans = Source_Sans_Pro({
    subsets: ['latin'],
    display: 'swap',
    weight: ['300', '400', '600', '700'],
});

export default function RootLayout({ children }) {
    return (
        <html lang="en">
            <body className={sourceSans.className}>
                <code className={robotoMono.variable}>Hello</code>
                {children}
            </body>
        </html>
    );
}
```

### 3. Apply Fonts with CSS Variables

Use CSS variables for flexible font application:

```css
/* globals.css */
:root {
    --font-primary: var(--font-inter), system-ui, sans-serif;
    --font-mono: var(--font-mono), 'Courier New', monospace;
}

body {
    font-family: var(--font-primary);
}

code, pre {
    font-family: var(--font-mono);
}
```

### 4. Handle Font Loading Fallbacks

Set up fallback fonts to prevent layout shifts:

```typescript
const inter = Inter({
    subsets: ['latin'],
    display: 'swap',
    fallback: ['system-ui', 'arial', 'sans-serif'],
    adjustFontFallback: 'Arial',
});
```

## Common Scenarios

**Scenario 1: Font causes FOIT (Flash of Invisible Text).**
Use `display: 'swap'` to show fallback text while the custom font loads.

**Scenario 2: Font loads on first page but not after navigation.**
Ensure the font variable is applied at the `<html>` level so it's available throughout the app.

**Scenario 3: Font differs between development and production.**
Check that font files are in the correct directory and `next.config.js` allows the font source.

## Prevent It

1. **Use `next/font` instead of external `<link>` tags** for automatic optimization.

2. **Set `display: 'swap'`** to prevent invisible text during font loading.

3. **Limit font weights and subsets** to reduce download size.
