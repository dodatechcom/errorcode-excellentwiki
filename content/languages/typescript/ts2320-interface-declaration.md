---
title: "[Solution] TypeScript TS2320 — Interface 'X' cannot extend 'Y'"
description: "Fix TypeScript TS2320: Interface 'X' cannot extend 'Y'. Fix interface extension errors."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2320", "interface", "extends", "cannot-extend", "declaration"]
weight: 5
---

# TS2320 — Interface 'X' cannot extend 'Y'

TS2320 occurs when an interface tries to extend a type that cannot be extended, such as a primitive type, a class with private members, or an incompatible type.

## Common Causes

```typescript
// Cause 1: Extending a primitive type
interface MyString extends string { // TS2320
  toUpperCase(): string;
}

// Cause 2: Extending a class with private members
class Secret {
  private data: string;
  constructor() { this.data = "secret"; }
}

interface Exposed extends Secret { // TS2320: cannot extend sealed type
  data: string;
}

// Cause 3: Extending incompatible interfaces
interface A {
  x: number;
}
interface B {
  x: string;
}
interface C extends A, B {} // TS2320: incompatible 'x'
```

## How to Fix

### Fix 1: Use composition instead of extension

```typescript
interface MyString {
  value: string;
  toUpperCase(): string;
}
```

### Fix 2: Use type alias for extension

```typescript
type MyType = Secret & { data: string };
```

### Fix 3: Make properties compatible

```typescript
interface A {
  x: number;
}
interface B extends A {
  // inherit x from A, don't redefine
}
```

## Related Errors

- [TS2461: Interface incorrectly extends]({{< relref "/languages/typescript/ts2461-interface-extends" >}}) — type conflict.
- [TS2414: Type argument not assignable]({{< relref "/languages/typescript/ts2414-type-argument" >}}) — generic constraint.
- [TS2322: Type not assignable]({{< relref "/languages/typescript/ts2322-type" >}}) — general type mismatch.
