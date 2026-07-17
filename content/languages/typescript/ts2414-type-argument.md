---
title: "[Solution] TypeScript TS2414 — Type argument not assignable"
description: "Fix TypeScript TS2414: Type argument not assignable. Fix generic type argument constraint errors."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2414", "type-argument", "generic", "constraint", "not-assignable"]
weight: 5
---

# TS2414 — Type argument not assignable

TS2414 occurs when a type argument passed to a generic type or function does not satisfy the declared constraints.

## Common Causes

```typescript
// Cause 1: Type doesn't satisfy constraint
interface HasLength {
  length: number;
}

function logLength<T extends HasLength>(arg: T) {
  console.log(arg.length);
}
logLength(42); // TS2414: 'number' does not satisfy 'HasLength'

// Cause 2: Wrong type argument to generic class
class Container<T extends string> {
  value: T;
}
const c: Container<number> = { value: 42 }; // TS2414

// Cause 3: Interface extending with wrong type
interface StringMap<T extends string> {
  [key: string]: T;
}
const m: StringMap<number> = {}; // TS2414
```

## How to Fix

### Fix 1: Pass a type that satisfies the constraint

```typescript
logLength("hello"); // string has length
logLength([1, 2, 3]); // array has length
```

### Fix 2: Relax or change the constraint

```typescript
class Container<T> {
  value: T;
}
const c: Container<number> = { value: 42 }; // OK
```

### Fix 3: Ensure interface extension is valid

```typescript
interface NumberMap<T extends number> {
  [key: string]: T;
}
```

## Related Errors

- [TS2344: Type does not satisfy constraint]({{< relref "/languages/typescript/ts2344-type-not assignable" >}}) — constraint failure.
- [TS2420: Class incorrectly implements]({{< relref "/languages/typescript/ts2420-correctly-implemented" >}}) — interface implementation.
- [TS2461: Interface incorrectly extends]({{< relref "/languages/typescript/ts2461-interface-extends" >}}) — interface extension.
