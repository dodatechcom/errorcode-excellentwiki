---
title: "[Solution] TypeScript TS2307 — Cannot find module 'X'"
description: "Fix TypeScript TS2307: Cannot find module 'X'. Resolve module resolution and import errors in TypeScript."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2307", "module", "import", "cannot-find", "module-resolution"]
weight: 5
---

# TS2307 — Cannot find module 'X'

TS2307 occurs when TypeScript cannot resolve an import to a module. This can happen because the module is not installed, the path is wrong, or type definitions are missing.

## Common Causes

```typescript
// Cause 1: Module not installed
import express from "express"; // TS2307 if express not installed

// Cause 2: Wrong import path
import { helper } from "./utils"; // TS2307 if file is utils.ts in different directory

// Cause 3: Missing type definitions
import lodash from "lodash"; // TS2307 if @types/lodash not installed

// Cause 4: Relative path without extension
import { foo } from "./bar"; // TS2307 if bar.js (not .ts)
```

## How to Fix

### Fix 1: Install the package

```bash
npm install express
```

### Fix 2: Install type definitions

```bash
npm install --save-dev @types/express
```

### Fix 3: Fix the import path

```typescript
import { helper } from "../utils"; // correct relative path
```

### Fix 4: Configure moduleResolution in tsconfig

```json
{
  "compilerOptions": {
    "moduleResolution": "node"
  }
}
```

## Examples

```bash
# Find where TypeScript looks for modules
npx tsc --traceResolution

# Check installed packages
npm ls express
```

## Related Errors

- [TS2304: Cannot find name]({{< relref "/languages/typescript/ts2304-cannot-find" >}}) — undefined identifier.
- [TS2306: File is not a module]({{< relref "/languages/typescript/ts2306-X-is-not-a-module" >}}) — file found but not a module.
- [TS2503: Cannot find namespace]({{< relref "/languages/typescript/ts2503-cannot-find-namespace" >}}) — namespace not found.
