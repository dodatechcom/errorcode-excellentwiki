---
title: "[Solution] TypeScript TS2707 — X is a type but not a module"
description: "Fix TypeScript TS2707: X is a type but not a module. Use import type for type-only imports."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2707", "type-not-module", "import-type", "type-only", "module"]
weight: 5
---

# TS2707 — Generic type 'X' from module '"Y"' cannot be used without an import

TS2707 occurs when you try to import a type from a file that is not a module (does not have any top-level import/export statements).

## Common Causes

```typescript
// Cause 1: File is not a module
// file: types.ts (no export statements)
interface User {
  name: string;
}

// file: app.ts
import { User } from "./types"; // TS2707

// Cause 2: Wrong file extension
import { helper } from "./utils.js"; // TS2707 if utils.ts has no exports

// Cause 3: Missing exports
// file: helpers.ts
function helper() {} // not exported
import { helper } from "./helpers"; // TS2707
```

## How to Fix

### Fix 1: Add export to the file

```typescript
// file: types.ts
export interface User {
  name: string;
}
```

### Fix 2: Use triple-slash reference

```typescript
/// <reference path="./types.d.ts" />
```

### Fix 3: Use ambient module declaration

```typescript
// In a .d.ts file
declare module "./types" {
  export interface User {
    name: string;
  }
}
```

## Related Errors

- [TS2306: File is not a module]({{< relref "/languages/typescript/ts2306-X-is-not-a-module" >}}) — similar error.
- [TS2307: Cannot find module]({{< relref "/languages/typescript/ts2307-cannot-find-module" >}}) — module not found.
- [TS2503: Cannot find namespace]({{< relref "/languages/typescript/ts2503-cannot-find-namespace" >}}) — namespace not found.
