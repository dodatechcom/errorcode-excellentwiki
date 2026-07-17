---
title: "[Solution] TypeScript TS2693 — 'X' only refers to a type"
description: "Fix TypeScript TS2693: 'X' only refers to a type but is being used as a value. Use typeof or value imports."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2693 — 'X' only refers to a type but is being used as a value here

TS2693 occurs when you try to use a type-only declaration as a runtime value. Types exist only at compile time and cannot be used at runtime.

## Common Causes

```typescript
// Cause 1: Using interface as value
interface User {
  name: string;
}
const u = new User(); // TS2693: 'User' only refers to a type

// Cause 2: Using type alias as value
type Point = { x: number; y: number };
const p = Point(); // TS2693

// Cause 3: Importing type as value
import type { Config } from "./config";
const c = new Config(); // TS2693: Config is type-only
```

## How to Fix

### Fix 1: Use class instead of interface

```typescript
class User {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
}
const u = new User("Alice");
```

### Fix 2: Use typeof for type operations

```typescript
const obj = { x: 1, y: 2 };
type Point = typeof obj; // type from value
```

### Fix 3: Import as value

```typescript
import { Config } from "./config"; // remove 'type'
const c = new Config();
```

## Related Errors

- [TS2339: Property is type-only import]({{< relref "/languages/typescript/ts2339-property-access" >}}) — type-only import access.
- [TS2304: Cannot find name]({{< relref "/languages/typescript/ts2304-cannot-find" >}}) — undefined identifier.
- [TS2349: This expression is not callable]({{< relref "/languages/typescript/ts2349-not-callable" >}}) — non-callable expression.
