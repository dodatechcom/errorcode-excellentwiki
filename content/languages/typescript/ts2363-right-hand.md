---
title: "[Solution] TypeScript TS2363 — The right-hand side of arithmetic must be"
description: "Fix TypeScript TS2363: The right-hand side of arithmetic must be a 'number', 'bigint', or 'any' type."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2363 — The right-hand side of arithmetic must be a 'number', 'bigint', or 'any' type

TS2363 occurs when the right-hand operand of an arithmetic operation is not a numeric type.

## Common Causes

```typescript
// Cause 1: String on right-hand side
const result = 5 + "hello"; // TS2363

// Cause 2: Boolean on right-hand side
const val = 1 + true; // TS2363

// Cause 3: Object on right-hand side
const obj = { value: 3 };
const sum = 10 + obj; // TS2363
```

## How to Fix

### Fix 1: Convert to number

```typescript
const result = 5 + Number("3");
```

### Fix 2: Use proper types

```typescript
const val = 1 + (true ? 1 : 0);
```

### Fix 3: Extract numeric value

```typescript
const sum = 10 + obj.value;
```

## Related Errors

- [TS2362: Left-hand side of arithmetic must be]({{< relref "/languages/typescript/ts2362-arithmetic" >}}) — left-hand side variant.
- [TS2322: Type not assignable]({{< relref "/languages/typescript/ts2322-type" >}}) — general type mismatch.
- [TS2345: Argument not assignable]({{< relref "/languages/typescript/ts2345-argument" >}}) — argument type mismatch.
