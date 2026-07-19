---
title: "Next.js CSS and styling errors"
description: "Next.js errors related to CSS styling. Common issues include incorrect CSS Modules usage, global CSS import problems, or Tailwind CSS configuration errors."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["error", "css", "styling", "tailwind"]
severity: "error"
solution: "Import global CSS only in layout.tsx or _app.tsx. Use CSS Modules for component-specific styles. Ensure Tailwind is properly configured. Use className correctly with conditional styling."
---

Next.js errors related to CSS styling. Common issues include incorrect CSS Modules usage, global CSS import problems, or Tailwind CSS configuration errors.

## Solution

Import global CSS only in layout.tsx or _app.tsx. Use CSS Modules for component-specific styles. Ensure Tailwind is properly configured. Use className correctly with conditional styling.

## Code Example

```javascript
  // BAD: Importing global CSS in component
  // app/components/Header.tsx
  import '../styles/global.css'; // Error in App Router!
  
  export function Header() {
    return <header className="header">Header</header>;
  }
  
  // GOOD: Global CSS in layout.tsx
  // app/layout.tsx
  import '../styles/global.css';
  
  export default function RootLayout({ children }) {
    return (
      <html>
        <body>{children}</body>
      </html>
    );
  }
  
  // GOOD: CSS Modules
  // app/components/Header.module.css
  .header {
    padding: 1rem;
    background: blue;
  }
  
  // app/components/Header.tsx
  import styles from './Header.module.css';
  
  export function Header() {
    return <header className={styles.header}>Header</header>;
  }
  
  // GOOD: Tailwind CSS setup
  // tailwind.config.js
  module.exports = {
    content: [
      './app/**/*.{js,ts,jsx,tsx}',
      './components/**/*.{js,ts,jsx,tsx}',
    ],
    theme: {
      extend: {},
    },
    plugins: [],
  };
  
  // app/layout.tsx
  import './globals.css'; // Contains @tailwind directives;
  
  // GOOD: Conditional Tailwind classes
  function Button({ variant = 'primary', disabled }) {
    return (
      <button 
        className={`
          px-4 py-2 rounded
          ${variant === 'primary' ? 'bg-blue-500 text-white' : 'bg-gray-200'}
          ${disabled ? 'opacity-50 cursor-not-allowed' : 'hover:bg-blue-600'}
        `}
        disabled={disabled}
      >
        Click me
      </button>
    );
  }
```
