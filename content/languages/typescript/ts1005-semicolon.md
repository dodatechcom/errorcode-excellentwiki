---
title: "[Solution] TypeScript TS1005 — ';' expected"
description: "Fix TypeScript TS1005: ';' expected. Resolve missing semicolon syntax errors in TypeScript."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS1005 — ';' expected

TS1005 is a syntax error indicating TypeScript expected a semicolon at the specified position. Missing semicolons, malformed statements, or incorrect syntax trigger this error.

## Common Causes

```typescript
// Cause 1: Missing semicolon after statement
let x = 5
let y = 10  // TS1005: ';' expected before 'let'

// Cause 2: Missing semicolon in for loop
for (let i = 0; i < 10; i++)
  console.log(i)  // missing semicolon in some contexts

// Cause 3: Wrong syntax in import
import { name } from "./module"
import { other } from "./other"  // may trigger TS1005

// Cause 4: Missing semicolon in type definition
interface User {
  name: string
  age: number  // TS1005
}
```

## How to Fix

### Fix 1: Add missing semicolons

```typescript
let x = 5;
let y = 10;
```

### Fix 2: Check semicolon context

```typescript
// Semicolons required after:
let x = 5;
const y = "hello";
function foo() { return 1; }
```

### Fix 3: Enable auto-semicolons in editor

Configure your editor to insert semicolons automatically.

## Related Errors

- [TS1109: Expression expected]({{< relref "/languages/typescript/ts1109-expression" >}}) — broader syntax error.
- [TS1128: Declaration or statement expected]({{< relref "/languages/typescript/ts1128-declaration" >}}) — missing declaration.
- [TS1002: Unterminated string literal]({{< relref "/languages/typescript/ts1002-scanner" >}}) — string syntax error.
