---
title: "[Solution] JavaScript Preact Compatibility Error — How to Fix"
description: "Fix JavaScript Preact compatibility errors. Resolve hooks, virtual DOM, and library issues."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 5
---

# JavaScript Preact Compatibility Error

A `TypeError: Invalid hook call` or `PreactError` occurs when Preact encounters incompatible React libraries, when hooks are used incorrectly, or when the virtual DOM diffing fails.

## Why It Happens

Preact is a lightweight React alternative. Errors arise when using React-specific libraries, when hooks violate rules, when components are not properly wrapped, or when the preact-compat alias is missing.

## Common Error Messages

- `TypeError: Invalid hook call`
- `PreactError: Component is not a function`
- `TypeError: Cannot read property of undefined`
- `Error: Minified exception occurred`

## How to Fix It

### Fix 1: Configure compatibility

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import preact from '@preact/preset-vite';

export default defineConfig({
  plugins: [preact()],
  resolve: {
    alias: {
      'react': 'preact/compat',
      'react-dom/test-utils': 'preact/test-utils',
      'react-dom': 'preact/compat',
      'react/jsx-runtime': 'preact/jsx-runtime',
    },
  },
});
```

### Fix 2: Use hooks correctly

```jsx
import { useState, useEffect } from 'preact/hooks';

// Wrong — conditional hook
// if (condition) {
//   const [count, setCount] = useState(0);
// }

// Correct — hooks at top level
function Counter() {
  const [count, setCount] = useState(0);
  
  useEffect(() => {
    document.title = `Count: ${count}`;
  }, [count]);

  return (
    <button onClick={() => setCount(c => c + 1)}>
      Count: {count}
    </button>
  );
}
```

### Fix 3: Handle third-party libraries

```jsx
// Wrong — using React-specific library
// import { motion } from 'framer-motion';  // may not work

// Correct — use Preact-compatible library
import { useSpring, animated } from 'react-spring';

function AnimatedComponent() {
  const styles = useSpring({ opacity: 1 });
  return <animated.div style={styles}>Hello</animated.div>;
}
```

### Fix 4: Fix TypeScript

```json
// tsconfig.json
{
  "compilerOptions": {
    "jsx": "react",
    "jsxImportSource": "preact",
    "types": ["preact"]
  }
}
```

## Common Scenarios

- **React library incompatibility** — Library uses React-specific APIs not available in Preact.
- **Hook violation** — Hooks called conditionally or in loops.
- **Missing alias** — React imports not aliased to Preact.

## Prevent It

- Always set up aliases for `react` and `react-dom` to `preact/compat`.
- Check library compatibility before installing React-specific packages.
- Use `preact/debug` in development for better error messages.

## Related Errors

- [TypeError](/javascript/typeerror/) — hook call invalid
- [PreactError](/javascript/preact-error/) — Preact operation failed
- [CompatibilityError](/javascript/compatibility-error/) — library not compatible
