---
title: "[Solution] Vite Failed to Resolve Import"
description: "Fix Vite import resolution errors. Resolve module not found and alias issues in Vite projects."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["vite", "import", "resolve", "module", "alias"]
weight: 5
---

# Vite Failed to Resolve Import

Vite uses native ESM-based module resolution, which is stricter than webpack. This error occurs when an import path cannot be resolved to a file or package.

## Common Causes

- The import path has a typo or incorrect casing
- A path alias is not configured in `vite.config`
- The package is not installed or is missing a `main` field
- Bare imports without `node_modules` are not resolved

## How to Fix

### Configure Path Aliases

```typescript
// vite.config.ts
import path from 'path';
import { defineConfig } from 'vite';

export default defineConfig({
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
});
```

### Install Missing Packages

```bash
npm install <package-name>
```

### Fix Import Paths

```typescript
// WRONG
import { helper } from './Helper';  // file is helper.ts (lowercase)

// CORRECT
import { helper } from './helper';
```

### Add TypeScript Path Mapping

```json
// tsconfig.json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  }
}
```

## Examples

```typescript
// Missing alias configuration
import { Button } from '@/components/Button';
// ERROR: Failed to resolve '@/components/Button'
// Fix: add resolve.alias in vite.config

// Package not installed
import moment from 'moment';
// ERROR: Failed to resolve import 'moment'
// Fix: npm install moment
```

## Related Errors

- [Import Error]({{< relref "/tools/webpack/module-not-found" >}}) — webpack module resolution
- [CSS Error]({{< relref "/tools/vite/css-error" >}}) — CSS processing failure
