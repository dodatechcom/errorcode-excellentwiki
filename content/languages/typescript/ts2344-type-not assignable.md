---
title: "[Solution] TypeScript TS2344 — Type 'X' does not satisfy constraint 'Y'"
description: "Fix TypeScript TS2344: Type 'X' does not satisfy constraint 'Y'. Satisfy generic type constraints."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2344 — Type 'X' does not satisfy constraint 'Y'

TS2344 occurs when a type argument passed to a generic does not satisfy the declared `extends` constraint.

## Common Causes

```typescript
// Cause 1: Type doesn't satisfy constraint
interface HasLength {
  length: number;
}

function logLength<T extends HasLength>(arg: T) {
  console.log(arg.length);
}
logLength(42); // TS2344: 'number' does not satisfy 'HasLength'

// Cause 2: Wrong type argument
class Container<T extends string> {}
const c: Container<number> = new Container(); // TS2344

// Cause 3: Partial constraint satisfaction
interface Serializable {
  serialize(): string;
}
class MyClass {
  name = "test";
}
function serialize<T extends Serializable>(obj: T) {}
serialize(new MyClass()); // TS2344: MyClass missing serialize()
```

## How to Fix

### Fix 1: Pass a satisfying type

```typescript
logLength("hello"); // string has length
logLength([1, 2]); // array has length
```

### Fix 2: Implement the constraint

```typescript
class MyClass implements Serializable {
  name = "test";
  serialize() { return this.name; }
}
```

### Fix 3: Relax the constraint

```typescript
function logLength<T>(arg: T) {
  if (typeof arg === "string" || Array.isArray(arg)) {
    console.log(arg.length);
  }
}
```

## Related Errors

- [TS2414: Type argument not assignable]({{< relref "/languages/typescript/ts2414-type-argument" >}}) — similar generic constraint.
- [TS2420: Class incorrectly implements]({{< relref "/languages/typescript/ts2420-correctly-implemented" >}}) — interface constraint.
- [TS2322: Type not assignable]({{< relref "/languages/typescript/ts2322-type" >}}) — general type mismatch.
