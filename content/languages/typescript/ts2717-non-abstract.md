---
title: "[Solution] TypeScript TS2717 — Non-abstract class does not implement"
description: "Fix TypeScript TS2717: Non-abstract class 'X' does not implement inherited abstract member. Implement abstract members."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2717 — Non-abstract class 'X' does not implement inherited abstract member

TS2717 occurs when a concrete (non-abstract) class extends an abstract class or implements an interface but fails to provide implementations for all abstract members.

## Common Causes

```typescript
// Cause 1: Missing abstract method implementation
abstract class Shape {
  abstract area(): number;
}

class Circle extends Shape {
  radius: number;
  constructor(r: number) {
    super();
    this.radius = r;
  }
  // missing area() — TS2717
}

// Cause 2: Incomplete interface implementation
interface Repository {
  find(id: number): any;
  save(entity: any): void;
}

class UserRepository implements Repository {
  find(id: number) {
    return null;
  }
  // missing save() — TS2717
}
```

## How to Fix

### Fix 1: Implement all abstract members

```typescript
class Circle extends Shape {
  radius: number;
  constructor(r: number) {
    super();
    this.radius = r;
  }
  area(): number {
    return Math.PI * this.radius ** 2;
  }
}
```

### Fix 2: Use abstract in concrete class

```typescript
abstract class Circle extends Shape {
  radius: number;
  constructor(r: number) {
    super();
    this.radius = r;
  }
  // area() left abstract — subclass must implement
}
```

## Related Errors

- [TS2420: Class incorrectly implements]({{< relref "/languages/typescript/ts2420-correctly-implemented" >}}) — interface implementation.
- [TS2720: Class extends abstract]({{< relref "/languages/typescript/ts2720-class-extends-abstract" >}}) — abstract member conflict.
- [TS2304: Cannot find name]({{< relref "/languages/typescript/ts2304-cannot-find" >}}) — undefined member.
