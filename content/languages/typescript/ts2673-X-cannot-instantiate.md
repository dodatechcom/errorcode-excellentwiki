---
title: "[Solution] TypeScript TS2673 — X cannot be instantiated"
description: "Fix TypeScript TS2673: X cannot be instantiated with 'new'. Use abstract classes or constructors correctly."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2673 — Member 'X' cannot be instantiated with 'new'

TS2673 occurs when you try to use `new` on an abstract class or a type that does not have a construct signature.

## Common Causes

```typescript
// Cause 1: Instantiating abstract class
abstract class Shape {
  abstract area(): number;
}
const s = new Shape(); // TS2673

// Cause 2: Interface without construct signature
interface Factory {
  create(): void;
}
const f = new Factory(); // TS2673

// Cause 3: Type alias not constructable
type Point = { x: number; y: number };
const p = new Point(); // TS2673
```

## How to Fix

### Fix 1: Instantiate concrete subclass

```typescript
class Circle extends Shape {
  area() { return Math.PI * 4; }
}
const c = new Circle();
```

### Fix 2: Add construct signature

```typescript
interface Factory {
  new (): { create(): void };
}
```

### Fix 3: Use object literal

```typescript
const p: Point = { x: 1, y: 2 };
```

## Related Errors

- [TS2511: Cannot create instance of abstract class]({{< relref "/languages/typescript/ts2673-X-cannot-instantiate" >}}) — abstract instantiation.
- [TS2339: Property does not exist]({{< relref "/languages/typescript/ts2339-property" >}}) — property access errors.
- [TS2349: This expression is not callable]({{< relref "/languages/typescript/ts2349-not-callable" >}}) — non-callable expression.
