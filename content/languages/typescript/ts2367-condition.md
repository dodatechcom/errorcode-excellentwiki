---
title: "[Solution] TypeScript TS2367 — This comparison appears to be unintentional"
description: "Fix TypeScript TS2367: This comparison appears to be unintentional. Fix impossible type comparisons."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2367 — This comparison appears to be unintentional

TS2367 occurs when you compare two values that TypeScript knows can never be equal due to their types. This is a type safety check to prevent logical errors.

## Common Causes

```typescript
// Cause 1: Comparing unrelated types
let x: string = "hello";
if (x === 42) { // TS2367: this comparison is always false
  console.log("match");
}

// Cause 2: Comparing enum values
enum Color { Red, Green, Blue }
enum Size { Small, Medium, Large }

let c: Color = Color.Red;
if (c === Size.Small) { // TS2367
  console.log("match");
}

// Cause 3: Comparing with wrong type literal
let status: "active" | "inactive";
if (status === "deleted") { // TS2367
  console.log("deleted");
}
```

## How to Fix

### Fix 1: Compare compatible types

```typescript
let x: string = "hello";
if (x === "world") { // OK
  console.log("match");
}
```

### Fix 2: Cast if comparison is intentional

```typescript
if (x as any === 42) {
  console.log("match");
}
```

### Fix 3: Use proper type narrowing

```typescript
let status: "active" | "inactive";
if (status === "active") { // OK
  console.log("active");
}
```

## Related Errors

- [TS2322: Type not assignable]({{< relref "/languages/typescript/ts2322-type" >}}) — type mismatch in assignment.
- [TS2345: Argument not assignable]({{< relref "/languages/typescript/ts2345-argument" >}}) — type mismatch in call.
- [TS2362: Left-hand side of arithmetic must be]({{< relref "/languages/typescript/ts2362-arithmetic" >}}) — arithmetic type errors.
