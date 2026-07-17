---
title: "Vite Invalid Configuration Option"
description: "Vite rejects the configuration due to invalid options."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["vite", "config", "configuration", "option", "validation"]
weight: 5
---

# Vite Invalid Configuration Option

This error occurs when Vite detects invalid configuration options. Unknown properties, wrong types, or deprecated options cause Vite to reject the configuration.

## Common Causes

- Misspelled configuration properties
- Wrong value types for options
- Deprecated configuration options
- Unknown top-level properties
- Conflicting options

## How to Fix

### Check Configuration Syntax

```javascript
// vite.config.js
import { defineConfig } from 'vite';

export default defineConfig({
  root: './src',
  base: '/',
  mode: 'production',
  server: {
    port: 3000,
    host: 'localhost',
  },
});
```

### Fix Option Types

```javascript
// Wrong
export default defineConfig({
  server: {
    port: '3000',  // must be number
  },
});

// Correct
export default defineConfig({
  server: {
    port: 3000,
  },
});
```

### Remove Deprecated Options

```javascript
// Wrong (deprecated)
export default defineConfig({
  ssr: {
    format: 'cjs',  // deprecated
  },
});

// Correct
export default defineConfig({
  ssr: {
    format: 'esm',
  },
});
```

### Check for Typos

```javascript
// Wrong
export default defineConfig({
  servr: { port: 3000 },  // typo
});

// Correct
export default defineConfig({
  server: { port: 3000 },
});
```

### Validate Config in TypeScript

```typescript
import { defineConfig } from 'vite';

export default defineConfig({
  // TypeScript will catch type errors
});
```

## Examples

```text
[vite] invalid options in vite.config.js:
  Unknown option: servr
  Did you mean "server"?
```

## Related Errors

- [Vite Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — general build failure
- [Vite Plugin Error]({{< relref "/tools/vite/vite-plugin-error" >}}) — plugin errors
- [Vite Dev Server Error]({{< relref "/tools/vite/vite-dev-server-error" >}}) — dev server issues
