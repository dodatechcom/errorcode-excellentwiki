---
title: "[Solution] TypeScript TS2761 — X can only be declared as optional property"
description: "Fix TypeScript TS2761: X can only be declared as optional property. Use optional modifiers correctly."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2761 — 'X' can only be declared as optional property

TS2761 occurs when a property in an intersection type is required in one type but optional in another, creating a conflict.

## Common Causes

```typescript
// Cause 1: Conflicting optional/required in intersection
interface A {
  name: string;
}
interface B {
  name?: string;
}
type C = A & B; // TS2761: 'name' can only be optional

// Cause 2: Partial & required conflict
type Strict = { id: number };
type Loose = { id?: string };
type Both = Strict & Loose; // TS2761

// Cause 3: Merged interfaces with different optionality
interface Base {
  value: string;
}
interface Extended {
  value?: number;
}
type Merged = Base & Extended; // TS2761
```

## How to Fix

### Fix 1: Make properties consistent

```typescript
interface A {
  name?: string;
}
interface B {
  name?: string;
}
type C = A & B; // OK — both optional
```

### Fix 2: Use union type instead

```typescript
type Result = A | B; // union, not intersection
```

### Fix 3: Separate conflicting properties

```typescript
interface Combined {
  name: string;
  altName?: string;
}
```

## Related Errors

- [TS2322: Type not assignable]({{< relref "/languages/typescript/ts2322-type" >}}) — general type mismatch.
- [TS2741: Property is missing in type]({{< relref "/languages/typescript/ts2741-property" >}}) — missing property.
- [TS2356: Type has no properties in common]({{< relref "/languages/typescript/ts2356-destructuring" >}}) — incompatible types.
