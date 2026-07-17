---
title: "CSS Modules Error in Next.js"
description: "Next.js CSS Modules errors occur when scoped styles fail to compile, import, or apply correctly"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

CSS Modules errors occur when `.module.css` files fail to compile, are imported incorrectly, or when class names are referenced incorrectly in components. These errors appear during build or render time.

## Common Causes

- CSS file does not end with `.module.css`
- Class names accessed incorrectly (camelCase vs kebab-case)
- Global styles mixed with scoped styles
- Invalid CSS syntax in module file
- Missing CSS file at import path

## How to Fix

Create and use CSS modules correctly:

```css
/* styles/Button.module.css */
.button {
  background: blue;
  color: white;
  padding: 10px 20px;
}

.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

```tsx
import styles from './styles/Button.module.css';

export default function Button({ children, disabled }) {
  return (
    <button
      className={`${styles.button} ${disabled ? styles.disabled : ''}`}
      disabled={disabled}
    >
      {children}
    </button>
  );
}
```

Use dynamic class names:

```tsx
import styles from './Card.module.css';

interface CardProps {
  variant: 'primary' | 'secondary';
  children: React.ReactNode;
}

export default function Card({ variant, children }: CardProps) {
  return (
    <div className={`${styles.card} ${styles[variant]}`}>
      {children}
    </div>
  );
}
```

Combine CSS modules with global styles:

```css
/* globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

```tsx
// Use CSS modules for component-specific styles
import styles from './Hero.module.css';
import '../styles/globals.css';
```

## Examples

```tsx
import styles from './Button.module.css';

// Wrong: accessing kebab-case class
<button className={styles['my-button']}>Click</button>

// Correct: CSS modules convert to camelCase
<button className={styles.myButton}>Click</button>
```

```text
TypeError: Cannot read properties of undefined (reading 'my-button')
```

## Related Errors

- [Tailwind error]({{< relref "/frameworks/nextjs/nextjs-tailwind-error" >}})
- [Font error]({{< relref "/frameworks/nextjs/nextjs-font-error" >}})
