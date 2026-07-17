---
title: "[Solution] TypeScript TS6133 — Variable 'X' is declared but never used"
description: "Fix TypeScript TS6133: Variable 'X' is declared but never used. Remove unused declarations."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS6133 — Variable 'X' is declared but never used

TS6133 is a diagnostic warning (not a compile error) that occurs when a declared variable is never referenced. It is enabled by `noUnusedLocals` or `noUnusedParameters`.

## Common Causes

```typescript
// Cause 1: Unused function parameter
function greet(name: string, age: number) {
  return `Hello, ${name}`; // TS6133: 'age' is declared but never used
}

// Cause 2: Unused destructured variable
const [first, second] = [1, 2]; // TS6133: 'second' is never used

// Cause 3: Unused import
import { readFile, writeFile } from "fs"; // TS6133: 'readFile' is never used
```

## How to Fix

### Fix 1: Remove the unused parameter

```typescript
function greet(name: string) {
  return `Hello, ${name}`;
}
```

### Fix 2: Prefix with underscore

```typescript
function greet(name: string, _age: number) {
  return `Hello, ${name}`;
}
```

### Fix 3: Use the variable

```typescript
const [first, second] = [1, 2];
console.log(first, second);
```

### Fix 4: Disable the check

```json
{
  "compilerOptions": {
    "noUnusedParameters": false
  }
}
```

## Related Errors

- [TS2309: Variable is declared but never read]({{< relref "/languages/typescript/ts2309-variable-const" >}}) — local variable variant.
- [TS2769: No overload matches this call]({{< relref "/languages/typescript/ts2769-no-overload" >}}) — overload issues.
- [TS2304: Cannot find name]({{< relref "/languages/typescript/ts2304-cannot-find" >}}) — undefined identifier.
