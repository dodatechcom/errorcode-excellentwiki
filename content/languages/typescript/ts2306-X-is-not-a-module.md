---
title: "[Solution] TypeScript TS2306 — File 'X' is not a module"
description: "Fix TypeScript TS2306: File 'X' is not a module. Add exports to make files importable."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2306", "not-a-module", "import", "export", "file"]
weight: 5
---

# TS2306 — File 'X' is not a module

TS2306 occurs when you try to import from a file that does not have any top-level `export` or `import` statements. Without these, TypeScript treats the file as a script rather than a module.

## Common Causes

```typescript
// Cause 1: File has no exports
// file: utils.ts
function helper() {
  return 42;
}
// no 'export' keyword

// file: app.ts
import { helper } from "./utils"; // TS2306

// Cause 2: Using CommonJS without module flag
// file: old.js
module.exports = { helper };
// TypeScript may not recognize this as module

// Cause 3: Empty file
// file: empty.ts
// file: app.ts
import "./empty"; // TS2306
```

## How to Fix

### Fix 1: Add export statements

```typescript
// file: utils.ts
export function helper() {
  return 42;
}
```

### Fix 2: Add a re-export

```typescript
// file: utils.ts
const helper = () => 42;
export { helper };
```

### Fix 3: Use export default

```typescript
// file: utils.ts
export default function helper() {
  return 42;
}
```

## Related Errors

- [TS2707: X is a type but not a module]({{< relref "/languages/typescript/ts2707-X-is-a-type-but-not-a-module" >}}) — type-only file.
- [TS2307: Cannot find module]({{< relref "/languages/typescript/ts2307-cannot-find-module" >}}) — module not found.
- [TS2693: 'X' only refers to a type]({{< relref "/languages/typescript/ts2693-X-only-referenced" >}}) — type-only usage.
