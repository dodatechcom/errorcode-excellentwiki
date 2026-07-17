---
title: "[Solution] Next.js Build Error: Module not found Fix"
description: "Fix Next.js build errors when modules cannot be found. Resolve import paths, missing dependencies, and webpack configuration issues."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nextjs", "build", "module-not-found", "webpack", "import"]
weight: 5
---

# Next.js Build Error — module not found

This error occurs during `next build` when webpack cannot resolve an import. It is similar to Vite/Webpack build errors but specific to the Next.js build pipeline.

## What This Error Means

Common error messages:

- `Module not found: Can't resolve './components/Button'`
- `Module not found: Can't resolve 'missing-package'`
- `Error: Cannot find module '...'`

Next.js uses webpack under the hood. Build-time resolution is stricter than dev mode.

## Common Causes

```javascript
// Cause 1: Wrong import path
import Button from '../components/Button'; // wrong relative path

// Cause 2: Case sensitivity
import { Card } from './card'; // file is Card.js

// Cause 3: Missing package
import { debounce } from 'lodash-es'; // not installed

// Cause 4: App Router vs Pages Router confusion
// Using pages/ import in app/ directory

// Cause 5: Barrel file re-export issues
```

## How to Fix

### Fix 1: Check file structure

```bash
# List project structure
ls -la src/components/

# Verify import path matches actual file location
```

### Fix 2: Use absolute imports with jsconfig/tsconfig

```json
// jsconfig.json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@/components/*": ["src/components/*"]
    }
  }
}
```

```javascript
// Now works
import Button from '@/components/Button';
```

### Fix 3: Install missing dependencies

```bash
npm install lodash-es
# or
yarn add lodash-es
```

### Fix 4: Configure webpack aliases in next.config.js

```javascript
// next.config.js
const path = require('path');

module.exports = {
  webpack: (config) => {
    config.resolve.alias['@components'] = path.join(__dirname, 'src/components');
    return config;
  },
};
```

## Examples

```bash
$ next build

Error: Cannot find module './utils/formatDate'
Import trace:
  app/page.js

# Fix: check file exists
ls src/utils/formatDate.js
# File doesn't exist, create it or fix the import
```

## Related Errors

- [Next.js App Router]({{< relref "/languages/javascript/nextjs-app-router" >}}) — App Router error
- [Next.js Data Fetching]({{< relref "/languages/javascript/nextjs-data-fetching" >}}) — getServerSideProps error
- [Webpack Error]({{< relref "/languages/javascript/webpack-error" >}}) — webpack compilation error
