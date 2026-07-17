---
title: "[Solution] TypeScript TS2459 — Type 'X' has no property 'Y'"
description: "Fix TypeScript TS2459: Type 'X' has no property 'Y'. Resolve property access on incompatible types."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2459 — Type 'X' has no property 'Y' and no string index signature

TS2459 occurs when you try to access a property on a type that doesn't have it and doesn't have an index signature that would allow arbitrary property access.

## Common Causes

```typescript
// Cause 1: Accessing property on wrong type
type StringOrNumber = string | number;
const val: StringOrNumber = "hello";
val.toFixed(2); // TS2459: 'string | number' has no property 'toFixed'

// Cause 2: Missing index signature
interface User {
  name: string;
}
const user: User = { name: "Alice" };
user["email"] = "test"; // TS2459: no string index signature

// Cause 3: Union type property access
type A = { x: number };
type B = { y: number };
const val: A | B = { x: 1 };
val.x; // TS2459: 'y' is not common
```

## How to Fix

### Fix 1: Narrow the type first

```typescript
if (typeof val === "number") {
  val.toFixed(2); // OK
}
```

### Fix 2: Add index signature

```typescript
interface User {
  name: string;
  [key: string]: string;
}
```

### Fix 3: Use discriminated union

```typescript
type A = { kind: "a"; x: number };
type B = { kind: "b"; y: number };
function handle(val: A | B) {
  if (val.kind === "a") {
    console.log(val.x);
  }
}
```

## Related Errors

- [TS2339: Property does not exist]({{< relref "/languages/typescript/ts2339-property" >}}) — property access errors.
- [TS2345: Argument not assignable]({{< relref "/languages/typescript/ts2345-argument" >}}) — type mismatch in call.
- [TS2322: Type not assignable]({{< relref "/languages/typescript/ts2322-type" >}}) — assignment type mismatch.
