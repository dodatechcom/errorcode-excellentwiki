---
title: "[Solution] TypeScript TS2618 — A class may only extend another class or null"
description: "Fix TypeScript TS2618: A class may only extend another class or null. Use proper class inheritance."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2618 — A class may only extend another class or null

TS2618 occurs when a class tries to extend something that is not a class (e.g., an interface, type, or object).

## Common Causes

```typescript
// Cause 1: Extending an interface
interface Animal {
  name: string;
}
class Dog extends Animal {} // TS2618

// Cause 2: Extending a type alias
type Base = {
  value: number;
};
class Derived extends Base {} // TS2618

// Cause 3: Extending an expression
const base = { name: "base" };
class Derived extends base {} // TS2618
```

## How to Fix

### Fix 1: Use implements instead

```typescript
interface Animal {
  name: string;
}
class Dog implements Animal {
  name = "Rex";
}
```

### Fix 2: Use class instead of interface

```typescript
class Animal {
  name: string = "";
}
class Dog extends Animal {
  name = "Rex";
}
```

### Fix 3: Use mixin pattern

```typescript
type Constructor<T = {}> = new (...args: any[]) => T;
function Timestamped<TBase extends Constructor>(Base: TBase) {
  return class extends Base {
    createdAt = new Date();
  };
}
```

## Related Errors

- [TS2320: Interface cannot extend]({{< relref "/languages/typescript/ts2320-interface-declaration" >}}) — interface extension.
- [TS2461: Interface incorrectly extends]({{< relref "/languages/typescript/ts2461-interface-extends" >}}) — interface type conflict.
- [TS2420: Class incorrectly implements]({{< relref "/languages/typescript/ts2420-correctly-implemented" >}}) — class implementation.
