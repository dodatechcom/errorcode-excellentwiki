---
title: "[Solution] TypeScript TS2304 v2 — Cannot Find Name Fix"
description: "Fix TypeScript TS2304 when referencing undeclared identifiers. Handle missing imports, global declarations, and typos."
languages: ["typescript"]
error-types: ["compile-error"]
severities: ["error"]
tags: ["ts2304", "cannot-find-name", "undefined-identifier", "import", "global"]
weight: 5
---

# TS2304 — Cannot Find Name (v2)

This variant covers TS2304 errors involving missing global declarations, environment variables, DOM APIs not in lib, and names from packages without type support.

## What This Error Means

Common error messages:

- `TS2304: Cannot find name 'process'`
- `TS2304: Cannot find name 'require'`
- `TS2304: Cannot find name '__dirname'`
- `TS2304: Cannot find name 'AbortController'`
- `TS2304: Cannot find name 'myGlobal'`

TypeScript cannot find a declaration for the identifier. This means it's not imported, not declared in the current scope, and not available in the global type definitions.

## Common Causes

```typescript
// Cause 1: Node.js globals without types
console.log(process.env.NODE_ENV); // TS2304

// Cause 2: Missing DOM lib for browser APIs
const controller = new AbortController(); // TS2304 if no DOM lib

// Cause 3: Global variable from script tag not declared
console.log(MyLibrary.doSomething()); // TS2304

// Cause 4: Missing import
const result = formatDate(date); // TS2304 — formatDate not imported

// Cause 5: Environment variables without declaration
const apiUrl = import.meta.env.VITE_API_URL; // TS2304
```

## How to Fix

### Fix 1: Install Node.js types

```bash
npm install --save-dev @types/node
```

### Fix 2: Add correct lib to tsconfig.json

```json
{
  "compilerOptions": {
    "lib": ["ES2020", "DOM", "DOM.Iterable"]
  }
}
```

### Fix 3: Declare global variables

```typescript
// src/global.d.ts
declare const MyLibrary: {
  doSomething(): string;
};

declare const API_URL: string;
```

### Fix 4: Add missing import

```typescript
import { formatDate } from './utils';

const result = formatDate(date); // now resolves
```

### Fix 5: Declare environment variables

```typescript
// src/vite-env.d.ts
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_URL: string;
  readonly VITE_APP_TITLE: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
```

## Examples

```
src/server.ts:5:3 - error TS2304: Cannot find name '__dirname'.

5 console.log(__dirname);
    ~~~~~~~~
```

```typescript
// Fix for ESM projects (no __dirname)
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
```

## Related Errors

- [TS2304]({{< relref "/languages/typescript/ts2304" >}}) — basic TS2304
- [TS2307]({{< relref "/languages/typescript/ts2307" >}}) — cannot find module
- [TS2503]({{< relref "/languages/typescript/ts2503-cannot-find-namespace" >}}) — cannot find namespace
