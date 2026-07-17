---
title: "[Solution] TypeScript TS1009 — Declaration or statement expected"
description: "Fix TypeScript TS1009: Declaration or statement expected. Resolve parser-level syntax errors."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts1009", "declaration", "statement", "syntax-error", "parser"]
weight: 5
---

# TS1009 — Declaration or statement expected

TS1009 is a parser-level syntax error indicating TypeScript expected a declaration or statement at a position where it found something else. This is typically caused by malformed code structure.

## Common Causes

```typescript
// Cause 1: Extra comma in declaration list
let x, y, , z;  // TS1009

// Cause 2: Invalid token after import
import from "module";  // TS1009: missing import specifiers

// Cause 3: Unexpected token in interface
interface User {
  name: string,
  ,  // TS1009
}
```

## How to Fix

### Fix 1: Remove extra commas

```typescript
let x, y, z;
```

### Fix 2: Fix import syntax

```typescript
import { something } from "module";
// or
import defaultExport from "module";
```

### Fix 3: Fix interface declaration

```typescript
interface User {
  name: string;
  age: number;
}
```

## Related Errors

- [TS1128: Declaration or statement expected]({{< relref "/languages/typescript/ts1128-declaration" >}}) — similar parser error.
- [TS1005: ';' expected]({{< relref "/languages/typescript/ts1005-semicolon" >}}) — semicolon expected.
- [TS1109: Expression expected]({{< relref "/languages/typescript/ts1109-expression" >}}) — expression expected.
