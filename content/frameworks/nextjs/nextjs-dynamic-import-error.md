---
title: "Dynamic Import Error in Next.js"
description: "Next.js dynamic import errors occur when components fail to load asynchronously or SSR configuration is incorrect"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Dynamic import errors occur when `next/dynamic` fails to load a component, the component throws during loading, or the loading/fallback state is misconfigured. These errors prevent the dynamically loaded component from rendering.

## Common Causes

- Component file path is incorrect
- Component throws an error during lazy loading
- `ssr: false` used with server-side rendering requirements
- Missing or incorrect `loading` component
- Circular dependencies in dynamic imports

## How to Fix

Use `next/dynamic` correctly:

```tsx
import dynamic from 'next/dynamic';

const DynamicComponent = dynamic(() => import('./HeavyComponent'), {
  loading: () => <p>Loading...</p>,
  ssr: false,
});

export default function Page() {
  return (
    <div>
      <h1>My Page</h1>
      <DynamicComponent />
    </div>
  );
}
```

Dynamic import with named exports:

```tsx
import dynamic from 'next/dynamic';

const DynamicChart = dynamic(
  () => import('./Chart').then(mod => mod.Chart),
  { loading: () => <div>Loading chart...</div> }
);
```

Use dynamic imports for large dependencies:

```tsx
import dynamic from 'next/dynamic';

const MonacoEditor = dynamic(() => import('@monaco-editor/react'), {
  ssr: false,
  loading: () => <div>Loading editor...</div>,
});
```

Handle loading errors:

```tsx
'use client';
import dynamic from 'next/dynamic';

const DynamicComponent = dynamic(() => import('./Component'), {
  loading: () => <p>Loading...</p>,
  ssr: false,
});
```

## Examples

```tsx
import dynamic from 'next/dynamic';

const Chart = dynamic(() => import('./NonExistentComponent'));
// Error: Module not found
```

```text
Error: Failed to load module "./NonExistentComponent"
```

## Related Errors

- [Build error]({{< relref "/frameworks/nextjs/build-error" >}})
- [Client component error]({{< relref "/frameworks/nextjs/nextjs-client-component-error" >}})
