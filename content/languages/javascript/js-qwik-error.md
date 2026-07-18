---
title: "[Solution] JavaScript Qwik Resumability Error — How to Fix"
description: "Fix JavaScript Qwik resumability errors. Resolve serialization, hydration, and component issues."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 5
---

# JavaScript Qwik Resumability Error

A `QwikError` or `SerializationError` occurs when Qwik fails to serialize state, encounters hydration mismatches, or when components are not properly lazy-loaded.

## Why It Happens

Qwik uses resumability for instant loading. Errors arise when state cannot be serialized, when components access browser APIs on server, when serialization format is invalid, or when the manifest is incorrect.

## Common Error Messages

- `QwikError: Cannot serialize function`
- `SerializationError: State serialization failed`
- `HydrationError: Client/server mismatch`
- `Error: Component not found in manifest`

## How to Fix It

### Fix 1: Use correct serialization

```tsx
import { component$, useSignal } from '@builder.io/qwik';

// Wrong — serializing function
// component$(() => {
//   const handler = () => console.log('click');
//   return <button onClick$={handler}>Click</button>;
// });

// Correct — use inline handlers
export default component$(() => {
  const count = useSignal(0);
  
  return (
    <button onClick$={() => count.value++}>
      Count: {count.value}
    </button>
  );
});
```

### Fix 2: Handle server-side rendering

```tsx
import { component$, useSignal, useTask$ } from '@builder.io/qwik';

export default component$(() => {
  const data = useSignal(null);
  
  useTask$(() => {
    // Wrong — accessing window on server
    // data.value = window.innerWidth;

    // Correct — check for browser
    if (typeof window !== 'undefined') {
      data.value = window.innerWidth;
    }
  });

  return <div>Width: {data.value}</div>;
});
```

### Fix 3: Use lazy loading

```tsx
import { component$, lazy } from '@builder.io/qwik';

const HeavyComponent = lazy(() => import('./heavy'));

export default component$(() => {
  return (
    <div>
      <HeavyComponent />
    </div>
  );
});
```

### Fix 4: Fix manifest issues

```javascript
// vite.config.ts
import { qwikVite } from '@builder.io/qwik/optimizer';

export default defineConfig({
  plugins: [
    qwikVite({
      client: {
        outDir: 'dist/client',
      },
      ssr: {
        outDir: 'dist/server',
      },
    }),
  ],
});
```

## Common Scenarios

- **Serialization error** — Trying to serialize functions or non-serializable state.
- **Hydration mismatch** — Server and client render different content.
- **Manifest missing** — Component not found in build manifest.

## Prevent It

- Always use `$()` suffix for event handlers to enable lazy loading.
- Check `typeof window !== 'undefined'` before accessing browser APIs.
- Run `qwik build` to generate the manifest before deployment.

## Related Errors

- [SerializationError](/javascript/serialization-error/) — state serialization failed
- [HydrationError](/javascript/hydration-error/) — client/server mismatch
- [ManifestError](/javascript/manifest-error/) — component not in manifest
