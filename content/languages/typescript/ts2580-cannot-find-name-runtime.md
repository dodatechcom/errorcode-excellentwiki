---
title: "[Solution] TypeScript TS2580 — Cannot find name 'require'. Use import instead"
description: "Fix TypeScript TS2580: Cannot find name 'require'. Switch to ES module imports in TypeScript."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2580", "require", "import", "commonjs", "esm", "module-system"]
weight: 5
---

# TS2580 — Cannot find name 'require'. Use import instead

TS2580 occurs when you use `require()` in a TypeScript project configured for ES modules. TypeScript suggests using `import` statements instead.

## Common Causes

```typescript
// Cause 1: Using CommonJS require in ESM project
const express = require("express"); // TS2580

// Cause 2: require not typed
declare const require: any; // missing @types/node

// Cause 3: Wrong module system
// tsconfig.json has "module": "es2020" but code uses require
```

## How to Fix

### Fix 1: Use ES module import

```typescript
import express from "express";
```

### Fix 2: Install @types/node

```bash
npm install --save-dev @types/node
```

### Fix 3: Use createRequire for dynamic imports

```typescript
import { createRequire } from "module";
const require = createRequire(import.meta.url);
const pkg = require("package-name");
```

### Fix 4: Switch module system

```json
{
  "compilerOptions": {
    "module": "commonjs"
  }
}
```

## Related Errors

- [TS2307: Cannot find module]({{< relref "/languages/typescript/ts2307-cannot-find-module" >}}) — module not found.
- [TS2693: 'X' only refers to a type]({{< relref "/languages/typescript/ts2693-X-only-referenced" >}}) — type-only issues.
- [TS2304: Cannot find name]({{< relref "/languages/typescript/ts2304-cannot-find" >}}) — undefined identifier.
