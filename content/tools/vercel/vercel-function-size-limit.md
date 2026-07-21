---
title: "[Solution] Vercel Function Size Limit Error"
description: "Fix Vercel function size limit errors when serverless functions exceed the maximum bundle size."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel Function Size Limit Error

Vercel rejects deployment because function bundle exceeds size limit.

```
Error: Function exceeded the maximum size of 50MB
```

## Common Causes

- Large dependencies included in bundle
- Node modules not properly bundled
- Unused dependencies in package.json
- Large static files included in function
- Multiple large functions in one deploy

## How to Fix

### Analyze Bundle Size

```bash
# Check function sizes
ls -la .vercel/output/functions/

# Use vercel build analysis
vercel build --analyze
```

### Use External Dependencies

```json
// vercel.json
{
  "functions": {
    "api/**/*.js": {
      "includeFiles": "lib/**"
    }
  }
}
```

### Remove Unused Dependencies

```bash
# Find unused dependencies
npx depcheck

# Remove unused
npm uninstall unused-package
```

### Split Large Functions

```javascript
// Instead of one large function
// api/big-handler.js

// Create separate functions
// api/users.js
// api/products.js
// api/orders.js
```

### Use Shared Libraries

```javascript
// lib/shared.js
export const helper = () => { /* ... */ };

// api/handler.js
import { helper } from '../lib/shared.js';
```

### Enable Tree Shaking

```json
{
  "build": {
    "env": {
      "NODE_OPTIONS": "--experimental-tree-shaking"
    }
  }
}
```

## Examples

```bash
# Check what's in the bundle
find .vercel -name "*.js" -exec du -h {} \; | sort -rh | head -10

# Use vercel's bundle analyzer
npx vercel build --analyze 2>&1
```
