---
title: "[Solution] TypeScript TS2531 — Index signature in type 'X' requires property 'Y'"
description: "Fix TypeScript TS2531: Index signature in type 'X' requires property 'Y'. Ensure all properties match index signature."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2531", "index-signature", "requires-property", "string-index"]
weight: 5
---

# TS2531 — Index signature in type 'X' requires property 'Y'

TS2531 can occur when an index signature requires all properties of the type to match the index signature's value type, but a specific property doesn't comply.

## Common Causes

```typescript
// Cause 1: Property type doesn't match index signature
interface StringMap {
  [key: string]: string;
  count: number; // TS2531: 'number' is not assignable to 'string'
}

// Cause 2: Mixed types with index signature
interface Mixed {
  name: string;
  [key: string]: string | number;
  age: boolean; // TS2531: 'boolean' not in union
}

// Cause 3: Property incompatible with index
interface Dict {
  [key: string]: string;
  length: number; // TS2531
}
```

## How to Fix

### Fix 1: Make property match index signature

```typescript
interface StringMap {
  [key: string]: string;
  count: string; // now matches
}
```

### Fix 2: Widen index signature type

```typescript
interface StringMap {
  [key: string]: string | number;
  count: number;
}
```

### Fix 3: Remove index signature

```typescript
interface Config {
  name: string;
  count: number;
}
```

## Related Errors

- [TS2339: Property does not exist]({{< relref "/languages/typescript/ts2339-property" >}}) — property access errors.
- [TS2322: Type not assignable]({{< relref "/languages/typescript/ts2322-type" >}}) — general type mismatch.
- [TS2459: Type has no property]({{< relref "/languages/typescript/ts2459-type-mismatch" >}}) — missing property.
