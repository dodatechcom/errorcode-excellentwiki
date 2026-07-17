---
title: "Vite React JSX Transform Error"
description: "Vite fails to transform JSX syntax in React components."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Vite React — JSX Transform Error

This error occurs when Vite fails to transform JSX syntax in React components. The React plugin may not be configured correctly, or the JSX syntax may be invalid.

## Common Causes

- React plugin not installed or configured
- JSX syntax errors
- React version mismatch
- Missing React types

## How to Fix

### Install React Plugin

```bash
npm install -D @vitejs/plugin-react
```

### Configure React Plugin

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
});
```

### Fix JSX Syntax

```jsx
// Wrong - missing return
function App() {
  <div>Hello</div>
}

// Correct
function App() {
  return <div>Hello</div>;
}
```

### Use JSX in .tsx Files

```typescript
// App.tsx
import React from 'react';

interface Props {
  name: string;
}

function App({ name }: Props) {
  return <div>Hello {name}</div>;
}
```

### Fix React Version Mismatch

```bash
npm ls react react-dom
```

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  }
}
```

## Examples

```text
[vite] Internal server error: Failed to resolve JSX
  Unexpected token '<'
  at src/App.jsx:3:2
```

## Related Errors

- [Vite Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — general build failure
- [Vite Plugin Error]({{< relref "/tools/vite/vite-plugin-error" >}}) — plugin errors
- [Vite CSS Error]({{< relref "/tools/vite/vite-css-error" >}}) — CSS processing failure
