---
title: "[Solution] TypeScript TS2362 — The left-hand side of arithmetic must be"
description: "Fix TypeScript TS2362: The left-hand side of arithmetic must be a 'number', 'bigint', or 'any' type."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2362", "arithmetic", "left-hand-side", "number", "bigint"]
weight: 5
---

# TS2362 — The left-hand side of arithmetic must be a 'number', 'bigint', or 'any' type

TS2362 occurs when you use arithmetic operators on a value that is not a numeric type. The left-hand operand must be `number`, `bigint`, or `any`.

## Common Causes

```typescript
// Cause 1: Arithmetic on string
const result = "5" + 3; // TS2362 or implicit conversion

// Cause 2: Arithmetic on boolean
const val = true + 1; // TS2362

// Cause 3: Arithmetic on object
const obj = { value: 5 };
const sum = obj + 1; // TS2362
```

## How to Fix

### Fix 1: Convert to number

```typescript
const result = Number("5") + 3;
// or
const result = parseInt("5") + 3;
```

### Fix 2: Use proper types

```typescript
const val = true ? 1 : 0;
const sum = val + 1;
```

### Fix 3: Extract numeric value

```typescript
const obj = { value: 5 };
const sum = obj.value + 1;
```

## Related Errors

- [TS2363: Right-hand side of arithmetic must be]({{< relref "/languages/typescript/ts2363-right-hand" >}}) — right-hand side variant.
- [TS2322: Type not assignable]({{< relref "/languages/typescript/ts2322-type" >}}) — general type mismatch.
- [TS2345: Argument not assignable]({{< relref "/languages/typescript/ts2345-argument" >}}) — argument type mismatch.
