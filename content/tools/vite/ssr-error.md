---
title: "SSR Server Component Error"
description: "Vite's server-side rendering encountered an error while executing a server component or rendering on the server."
tools: ["vite"]
error-types: ["build-error"]
severities: ["error"]
tags: ["vite", "ssr", "server", "rendering"]
weight: 5
---

This error means Vite's SSR module runner failed while executing code on the server. It typically surfaces when a component or module throws during server-side rendering.

## Common Causes

- A browser-only API (like `window` or `document`) is used in server-rendered code
- A dependency is not compatible with SSR environments
- Import path issues when Vite resolves server and client bundles separately
- Circular dependencies in server-side modules

## How to Fix

Guard browser-only code with environment checks:

```javascript
if (typeof window !== 'undefined') {
  // browser-only code
}
```

Mark browser-only modules as external in your Vite config:

```javascript
// vite.config.js
export default defineConfig({
  ssr: {
    noExternal: ['some-package'],
    external: ['browser-only-package'],
  },
});
```

Ensure your SSR entry point does not import client-only code at the top level:

```javascript
// server entry
export async function render() {
  const { default: ClientApp } = await import('./App');
  return ClientApp.renderToString();
}
```

## Examples

```
[SSR ERROR] src/components/Widget.tsx
ReferenceError: window is not defined
    at Object.<anonymous> (src/components/Widget.tsx:5:14)
```

## Related Errors

- [Pre-transform Error]({{< relref "/tools/vite/pre-transform-error" >}})
