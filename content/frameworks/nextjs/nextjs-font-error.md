---
title: "next/font Error in Next.js"
description: "next/font errors occur when custom fonts fail to load, optimize, or display correctly"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

`next/font` errors occur when the built-in font optimization system fails to load, process, or serve custom fonts. These errors manifest as font loading failures, incorrect font display, or build-time errors.

## Common Causes

- Font file not found at specified path
- Network failure loading remote fonts
- Invalid font configuration
- Font subset or display settings mismatch
- Missing `next/font/google` or `next/font/local` import

## How to Fix

Use Google Fonts:

```tsx
// app/layout.tsx
import { Inter } from 'next/font/google';

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
});

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={inter.className}>
      <body>{children}</body>
    </html>
  );
}
```

Use local fonts:

```tsx
// app/layout.tsx
import localFont from 'next/font/local';

const myFont = localFont({
  src: './fonts/MyFont.woff2',
  display: 'swap',
  variable: '--font-my-font',
});

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={myFont.variable}>
      <body>{children}</body>
    </html>
  );
}
```

Apply font variables in Tailwind:

```tsx
const inter = Inter({ subsets: ['latin'], variable: '--font-inter' });

// In layout
<html className={inter.variable}>
<body className="font-sans">
  {/* Uses --font-inter */}
</body>
</html>
```

Use font subsets correctly:

```tsx
const roboto = Roboto({
  weight: ['400', '700'],
  subsets: ['latin'],
  display: 'swap',
});
```

## Examples

```tsx
import { NonExistentFont } from 'next/font/google';
// Error: Module not found
```

```text
Error: Failed to fetch font "NonExistentFont" from Google Fonts
```

## Related Errors

- [CSS Modules error]({{< relref "/frameworks/nextjs/nextjs-css-modules-error" >}})
- [Build error]({{< relref "/frameworks/nextjs/build-error" >}})
