---
title: "[Solution] Vite Build Error: rollup failed to resolve import Fix"
description: "Fix Vite build error when rollup fails to resolve imports. Handle missing dependencies, circular imports, and ESM issues in Vite builds."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Vite Build Error — rollup failed to resolve

This error occurs during `vite build` when Rollup (Vite's bundler) cannot resolve one or more imports. It is common with missing packages, circular dependencies, or ESM misconfigurations.

## What This Error Means

Common error messages:

- `rollup failed to resolve import "..." from "..."`
- `Could not resolve "./utils" from "src/main.js"`
- `[vite]: RollupError: Unresolved imports`

Rollup requires all imports to be resolvable at build time. Unlike dev mode, it doesn't serve files dynamically.

## Common Causes

```javascript
// Cause 1: Missing dependency
import { something } from 'missing-package';

// Cause 2: Case sensitivity issue
import { Button } from './Button'; // file is button.js (lowercase)

// Cause 3: Circular dependencies
// a.js imports b.js, b.js imports a.js

// Cause 4: ESM/CJS mismatch
// Using require() in ESM project

// Cause 5: Alias not configured
import { helper } from '@utils/helper'; // no alias defined
```

## How to Fix

### Fix 1: Install missing dependencies

```bash
npm install missing-package
# or
yarn add missing-package
```

### Fix 2: Configure resolve aliases

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import path from 'path';

export default defineConfig({
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@utils': path.resolve(__dirname, './src/utils'),
    },
  },
});
```

### Fix 3: Fix case sensitivity

```bash
# Check actual file name
ls src/components/

# Rename file to match import
mv src/components/button.js src/components/Button.js
```

### Fix 4: Use external for problematic packages

```javascript
// vite.config.js
export default defineConfig({
  build: {
    rollupOptions: {
      external: ['problematic-native-module'],
    },
  },
});
```

### Fix 5: Check for circular imports

```bash
# Use madge to detect circular dependencies
npx madge --circular src/
```

## Examples

```bash
$ vite build

vite v5.0.0 building for production...
error during build:
rollup failed to resolve import "./utils" from "src/main.js"
```

```javascript
// Fix: ensure correct path
import { helper } from './utils/index.js';
```

## Related Errors

- [Vite HMR Error]({{< relref "/languages/javascript/vite-hmr-error" >}}) — HMR update failed
- [Vite SSR Error]({{< relref "/languages/javascript/vite-ssr-error" >}}) — SSR rendering failed
- [Webpack Compilation Error]({{< relref "/languages/javascript/webpack-error" >}}) — webpack build failed
