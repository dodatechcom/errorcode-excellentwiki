---
title: "[Solution] TypeScript TS2683 — Implicitly has type 'any'"
description: "Fix TypeScript TS2683: Implicitly has type 'any'. Fix 'this' context typing in TypeScript."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2683 — Implicitly has type 'any'

TS2683 occurs when `noImplicitThis` is enabled and TypeScript cannot determine the type of `this` in a function. Without explicit typing, `this` defaults to `any`.

## Common Causes

```typescript
// Cause 1: Regular function without this type
function logName() {
  console.log(this.name); // TS2683: 'this' implicitly has type 'any'
}

// Cause 2: Callback losing context
class Person {
  name = "Alice";
  greet() {
    setTimeout(function() {
      console.log(this.name); // TS2683
    }, 100);
  }
}

// Cause 3: Object method without explicit this
const obj = {
  value: 42,
  getValue() {
    return this.value; // TS2683
  }
};
```

## How to Fix

### Fix 1: Use arrow functions

```typescript
class Person {
  name = "Alice";
  greet() {
    setTimeout(() => {
      console.log(this.name); // OK — arrow function inherits this
    }, 100);
  }
}
```

### Fix 2: Annotate 'this' parameter

```typescript
function logName(this: { name: string }) {
  console.log(this.name);
}
```

### Fix 3: Use explicitly typed this

```typescript
interface Loggable {
  name: string;
}
function logName(this: Loggable) {
  console.log(this.name);
}
```

## Related Errors

- [TS7006: Parameter implicitly has 'any' type]({{< relref "/languages/typescript/ts7006-parameter" >}}) — parameter implicit any.
- [TS2684: The 'this' context of type is not assignable]({{< relref "/languages/typescript/ts2684" >}}) — this type mismatch.
- [TS18046: Variable is of type 'unknown']({{< relref "/languages/typescript/ts18046-unknown" >}}) — unknown type.
