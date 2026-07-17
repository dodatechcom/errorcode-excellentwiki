---
title: "Next.js Build Error - Module Not Found"
description: "Next.js build fails with ModuleNotFoundError when a required module cannot be resolved"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["build", "module", "import", "compilation", "nextjs"]
weight: 5
---

## What This Error Means

A Next.js build error occurs when the build process cannot find or resolve a required module. This happens during `next build` or `next dev` and prevents the application from starting.

## Common Causes

- Module not installed (`node_modules` missing or incomplete)
- Typo in import path
- Circular dependencies
- Incorrect module resolution configuration
- `node_modules` cache corruption

## How to Fix

Reinstall dependencies:

```bash
rm -rf node_modules package-lock.json
npm install
```

Verify the import path:

```tsx
// Wrong
import { Button } from '../components/Button';

// Correct (assuming file exists)
import { Button } from '../components/Button';
```

Check for circular dependencies:

```bash
npx madge --circular src/
```

Clear Next.js cache:

```bash
rm -rf .next
npm run build
```

Use absolute imports with `tsconfig.json`:

```json
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

```tsx
import { Auth } from '@/lib/auth';
// Error: Module not found: Can't resolve '@/lib/auth'
```

```text
Module not found: Can't resolve './components/Header'
```

## Related Errors

- [Build error]({{< relref "/frameworks/nextjs/build-error" >}})
- [Server component error]({{< relref "/frameworks/nextjs/nextjs-server-component-error" >}})
