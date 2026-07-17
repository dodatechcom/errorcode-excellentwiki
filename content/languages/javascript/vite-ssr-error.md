---
title: "[Solution] Vite SSR Error: server-side rendering failed Fix"
description: "Fix Vite SSR (Server-Side Rendering) errors. Handle SSR module failures, hydration mismatches, and Node.js compatibility issues."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Vite SSR Error — server-side rendering failed

This error occurs when Vite's SSR module fails to render on the server side. It typically involves Node.js/browser API mismatches, missing SSR-compatible modules, or hydration failures.

## What This Error Means

Common error messages:

- `[vite] SSR error: ...`
- `SSR module failed: ...`
- `Error: Not supported: window is not defined`

SSR renders your application on the server using Node.js. Code that uses browser APIs (window, document) will fail on the server.

## Common Causes

```javascript
// Cause 1: Using window/document in SSR
import { useState } from 'react';
const isMobile = window.innerWidth < 768; // SSR error

// Cause 2: Browser-only library
import moment from 'moment';
const locale = navigator.language; // SSR error

// Cause 3: Circular dependencies in SSR entry
// server.js → app.js → server.js

// Cause 4: Missing SSR-compatible import
import { Chart } from 'chart.js'; // needs SSR adapter
```

## How to Fix

### Fix 1: Guard browser APIs

```javascript
// Use dynamic imports with ssr: false
const Chart = await import('chart.js', { ssr: false });

// Or check for server environment
if (typeof window !== 'undefined') {
  // Client-only code
}
```

### Fix 2: Configure SSR externals

```javascript
// vite.config.js
export default defineConfig({
  ssr: {
    // Packages that shouldn't be bundled for SSR
    external: ['moment', 'chart.js'],
    noExternal: ['my-local-package'],
  },
});
```

### Fix 3: Use SSR-compatible alternatives

```javascript
// Instead of
import { Chart } from 'chart.js';

// Use
const Chart = await import('chart.js/auto');
// Or use a server-compatible chart library
```

### Fix 4: Mark client-only components

```javascript
// React example
import { lazy, Suspense } from 'react';

const ClientOnly = lazy(() => import('./ClientComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <ClientOnly />
    </Suspense>
  );
}
```

### Fix 5: Check SSR entry point

```javascript
// server.js (SSR entry)
import { renderToString } from 'react-dom/server';
import App from './App';

export function render(url) {
  return renderToString(<App url={url} />);
}
```

## Examples

```javascript
// This triggers SSR error
// component.js
export const isDesktop = window.matchMedia('(min-width: 768px)').matches;
// ReferenceError: window is not defined

// Fix: guard with typeof
export const isDesktop = typeof window !== 'undefined'
  ? window.matchMedia('(min-width: 768px)').matches
  : false;
```

## Related Errors

- [Vite Build Error]({{< relref "/languages/javascript/vite-build-error" >}}) — build failed
- [Vite HMR Error]({{< relref "/languages/javascript/vite-hmr-error" >}}) — HMR update failed
- [Next.js Hydration]({{< relref "/languages/javascript/nextjs-hydration" >}}) — hydration mismatch
