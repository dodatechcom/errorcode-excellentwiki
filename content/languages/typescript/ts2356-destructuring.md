---
title: "[Solution] TypeScript TS2356 — Type 'X' has no properties in common with type 'Y'"
description: "Fix TypeScript TS2356: Type 'X' has no properties in common with type 'Y'. Fix incompatible type comparisons."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2356 — Type 'X' has no properties in common with type 'Y'

TS2356 occurs when you compare or assign two types that share no common properties. TypeScript's structural type system finds zero overlap between the types.

## Common Causes

```typescript
// Cause 1: Comparing unrelated types
interface Cat {
  purr(): void;
}
interface Car {
  drive(): void;
}

const cat: Cat = { purr() {} };
const car: Car = { drive() {} };

if (cat === car) { // TS2356
  console.log("same");
}

// Cause 2: Assigning incompatible types
const cat2: Cat = car; // TS2356

// Cause 3: Union with no overlap
type Result = string & number; // TS2356
```

## How to Fix

### Fix 1: Don't compare incompatible types

```typescript
// Remove the comparison or use a common type
interface Pet {
  name: string;
}
interface Cat extends Pet { purr(): void; }
interface Dog extends Pet { bark(): void; }
```

### Fix 2: Use type guard or discriminator

```typescript
function isCat(val: Cat | Car): val is Cat {
  return "purr" in val;
}
```

### Fix 3: Fix the union type

```typescript
type Result = string | number; // use union, not intersection
```

## Related Errors

- [TS2322: Type not assignable]({{< relref "/languages/typescript/ts2322-type" >}}) — general type mismatch.
- [TS2367: Comparison unintentional]({{< relref "/languages/typescript/ts2367-condition" >}}) — impossible comparison.
- [TS2345: Argument not assignable]({{< relref "/languages/typescript/ts2345-argument" >}}) — argument type mismatch.
