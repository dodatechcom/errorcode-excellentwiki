---
title: "Tailwind CSS Error in Next.js"
description: "Tailwind CSS errors in Next.js occur when utility classes are not compiled, purged, or applied correctly"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["tailwind", "css", "utility", "purge", "nextjs"]
weight: 5
---

## What This Error Means

Tailwind CSS errors in Next.js occur when the utility-first CSS framework fails to compile classes, purge unused styles, or apply configurations. These errors manifest as missing styles, build failures, or class name conflicts.

## Common Causes

- Tailwind not installed or configured properly
- Content paths not set in `tailwind.config.js`
- JIT mode not enabled (default in v3+)
- Custom classes not defined in config
- PostCSS configuration issues

## How to Fix

Configure Tailwind CSS properly:

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#0070f3',
      },
    },
  },
  plugins: [],
};
```

Set up PostCSS:

```js
// postcss.config.js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

Include Tailwind directives in your CSS:

```css
/* styles/globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Use Tailwind classes in components:

```tsx
export default function Card({ title, description }) {
  return (
    <div className="rounded-lg bg-white p-6 shadow-md">
      <h2 className="text-xl font-bold text-gray-900">{title}</h2>
      <p className="mt-2 text-gray-600">{description}</p>
    </div>
  );
}
```

Use dynamic class names safely:

```tsx
const variants = {
  primary: 'bg-blue-500 text-white',
  secondary: 'bg-gray-500 text-white',
};

export default function Button({ variant = 'primary', children }) {
  return (
    <button className={`rounded px-4 py-2 ${variants[variant]}`}>
      {children}
    </button>
  );
}
```

## Examples

```tsx
// tailwind.config.js content not including this file
<div className="text-red-500">This might not render</div>
```

```text
Error: Cannot apply unknown utility class `text-red-500`
```

## Related Errors

- [CSS Modules error]({{< relref "/frameworks/nextjs/nextjs-css-modules-error" >}})
- [Build error]({{< relref "/frameworks/nextjs/build-error" >}})
