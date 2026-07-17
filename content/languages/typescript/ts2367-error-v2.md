---
title: "[Solution] TypeScript TS2367 v2 — Comparison Appears Unintentional Fix"
description: "Fix TypeScript TS2367 when comparing values that can never be equal due to their types. Handle type narrowing, enum comparisons, and literal types."
languages: ["typescript"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# TS2367 — Comparison Appears Unintentional (v2)

This variant of TS2367 covers comparisons between types that are provably unequal, including literal type comparisons, boolean checks against non-boolean values, and exhaustive switch statements.

## What This Error Means

Common error messages:

- `TS2367: This comparison appears to be unintentional because the types '"admin"' and '"user"' have no overlap.`
- `TS2367: This comparison appears to be unintentional because the types 'boolean' and 'number' have no overlap.`
- `TS2367: This comparison appears to be unintentional because the types 'string' and 'number' have no overlap.`

TypeScript detects when a comparison can never be true based on the types of the operands. This often means the comparison is redundant or there's a bug in the logic.

## Common Causes

```typescript
// Cause 1: Comparing literal types
type Status = 'active' | 'inactive';
const status: Status = 'active';

if (status === 'deleted') { // TS2367: 'deleted' not in Status
  // ...
}

// Cause 2: Boolean compared to non-boolean
const value: boolean = true;
if (value === 1) { // TS2367
  // ...
}

// Cause 3: Exhaustive switch missing case
type Shape = 'circle' | 'square';

function area(shape: Shape) {
  switch (shape) {
    case 'circle': return Math.PI;
    case 'square': return 1;
    case 'triangle': return 0.5; // TS2367: 'triangle' not in Shape
  }
}

// Cause 4: Comparing enum with wrong value
enum Color { Red, Green, Blue }
const c: Color = Color.Red;
if (c === 3) { // TS2367: 3 not in Color
  // ...
}

// Cause 5: Null comparison after narrowing
function process(value: string | null) {
  if (value !== null) {
    if (value === null) { // TS2367: already narrowed to string
      // ...
    }
  }
}
```

## How to Fix

### Fix 1: Expand the union type

```typescript
type Status = 'active' | 'inactive' | 'deleted';

if (status === 'deleted') { // now valid
  // ...
}
```

### Fix 2: Use type coercion for intentional comparison

```typescript
const value: boolean = true;
if (value === (true as unknown as number)) { // not recommended
  // ...
}
// Better: just check truthiness
if (value) { ... }
```

### Fix 3: Remove dead code branches

```typescript
type Shape = 'circle' | 'square';

function area(shape: Shape) {
  switch (shape) {
    case 'circle': return Math.PI;
    case 'square': return 1;
    // Remove the 'triangle' case — it's unreachable
  }
}
```

### Fix 4: Use `never` type for exhaustiveness checking

```typescript
function assertNever(x: never): never {
  throw new Error(`Unexpected value: ${x}`);
}

function area(shape: Shape) {
  switch (shape) {
    case 'circle': return Math.PI;
    case 'square': return 1;
    default:
      return assertNever(shape); // compile error if new case added
  }
}
```

### Fix 5: Use if-else for narrowing comparisons

```typescript
function process(value: string | null) {
  if (value === null) {
    return 'empty';
  }
  // value is string here
  return value.toUpperCase();
}
```

## Examples

```typescript
type Method = 'GET' | 'POST' | 'PUT' | 'DELETE';

function handle(method: Method) {
  if (method === 'PATCH') { // TS2367
    // 'PATCH' not in Method
  }
}

// Fix: add PATCH to the union
type Method = 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';
```

## Related Errors

- [TS2367]({{< relref "/languages/typescript/ts2367" >}}) — basic TS2367
- [TS2367 Condition]({{< relref "/languages/typescript/ts2367-condition" >}}) — condition variant
- [TS2683]({{< relref "/languages/typescript/ts2683" >}}) — 'this' implicitly has type any
