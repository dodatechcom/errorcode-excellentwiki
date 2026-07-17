---
title: "[Solution] React Invalid Element Type — Compiler Error Fix"
description: "Fix React invalid element type errors. Resolve issues with component imports, default exports, and element rendering."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# React Invalid Element Type

The error `Element type is invalid: expected a string (for built-in components) or a class/function (for composite components) but got: X` occurs when you pass something other than a valid React component or HTML tag name to JSX.

## Description

React expects every element type to be either a lowercase string (for DOM elements like `div`, `span`) or an uppercase identifier (for React components). When the value is `undefined`, `null`, a number, or an invalid type, React throws this error during rendering.

This is one of the most common React errors and typically indicates an import/export mistake.

## Common Causes

- **Missing default export** — importing a component that doesn't export default
- **Named vs default import mismatch** — using `import X from` instead of `import { X } from`
- **Circular dependency** — module A imports B which imports A, resulting in undefined
- **Conditional rendering with invalid type** — returning a non-component value

## How to Fix

### Fix 1: Check import/export alignment

```jsx
// File: Button.jsx
export default function Button() {
  return <button>Click</button>;
}

// Correct import
import Button from './Button';

// File: Icon.jsx
export function Icon() {
  return <span>★</span>;
}

// Correct import
import { Icon } from './Icon';
```

### Fix 2: Verify the module exports what you expect

```jsx
// Wrong — Button is not a default export
import Button from './Button'; // Button.jsx has: export function Button()

// Correct
import { Button } from './Button';
```

### Fix 3: Avoid circular dependencies

```jsx
// File: A.jsx
import { B } from './B';
export function A() { return <B />; }

// File: B.jsx
import { A } from './A'; // Circular!
export function B() { return <A />; }

// Fix: extract shared types/interfaces to a separate module
```

### Fix 4: Use conditional rendering safely

```jsx
function App({ Component }) {
  // Wrong — Component might be undefined
  return <Component />;

  // Correct — check before rendering
  if (!Component) return null;
  return <Component />;
}
```

## Examples

```jsx
const MyComponent = null;

function App() {
  return (
    <div>
      <MyComponent /> {/* Error: Element type is invalid */}
    </div>
  );
}
```

Output:
```
Element type is invalid: expected a string (for built-in components)
or a class/function (for composite components) but got: 'null'.
```

## Related Errors

- [react-invariant]({{< relref "/languages/javascript/react-invariant" >}}) — invariant violations in React.
- [react-error-boundary]({{< relref "/languages/javascript/react-error-boundary" >}}) — error boundaries catching render errors.
- [react-lazy-error]({{< relref "/languages/javascript/react-lazy-error" >}}) — lazy loading component failures.
