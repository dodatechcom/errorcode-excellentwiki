---
title: "[Solution] TypeScript TS2309 — Variable 'X' is declared but its value is never read"
description: "Fix TypeScript TS2309: Variable 'X' is declared but its value is never read. Remove or use unused variables."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2309", "unused", "variable", "never-read", "dead-code"]
weight: 5
---

# TS2309 — Variable 'X' is declared but its value is never read

TS2309 occurs when `noUnusedLocals` is enabled and a variable is declared but never used. This is a code quality check to reduce dead code.

## Common Causes

```typescript
// Cause 1: Imported but unused
import { helper } from "./utils"; // TS2309 if helper is never used

// Cause 2: Local variable never read
function process() {
  const temp = calculate(); // TS2309 if temp is never used
  return 42;
}

// Cause 3: Destructured but unused
const { name, age } = user; // TS2309 if age is never used
```

## How to Fix

### Fix 1: Remove the unused import

```typescript
// Remove: import { helper } from "./utils";
```

### Fix 2: Use the variable

```typescript
function process() {
  const temp = calculate();
  console.log(temp); // now used
  return 42;
}
```

### Fix 3: Prefix with underscore

```typescript
const { name, _age } = user; // underscore prefix suppresses warning
```

### Fix 4: Disable the check

```json
{
  "compilerOptions": {
    "noUnusedLocals": false
  }
}
```

## Related Errors

- [TS6133: Variable is declared but never used]({{< relref "/languages/typescript/ts6133-declared-but-never-used" >}}) — parameter variant.
- [TS2769: No overload matches this call]({{< relref "/languages/typescript/ts2769-no-overload" >}}) — overload issues.
- [TS2531: Object is possibly 'null']({{< relref "/languages/typescript/ts2531-object" >}}) — null access.
