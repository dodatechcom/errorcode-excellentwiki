---
title: "[Solution] TypeScript TS2454 — Variable 'X' is used before being assigned"
description: "Fix TypeScript TS2454: Variable 'X' is used before being assigned. Initialize variables before use."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2454", "used-before-assigned", "uninitialized", "definite-assignment"]
weight: 5
---

# TS2454 — Variable 'X' is used before being assigned

TS2454 occurs when `strictPropertyInitialization` or `strictNullChecks` detects that a variable may be used before it has been assigned a value.

## Common Causes

```typescript
// Cause 1: Variable declared but not initialized before use
let name: string;
console.log(name); // TS2454: used before assigned

// Cause 2: Class property not initialized
class User {
  name: string; // TS2454 if not initialized in constructor
  constructor() {
    // forgot to assign name
  }
}

// Cause 3: Conditional assignment not guaranteed
let value: number;
if (Math.random() > 0.5) {
  value = 1;
}
console.log(value); // TS2454: value may not be assigned
```

## How to Fix

### Fix 1: Initialize at declaration

```typescript
let name: string = "Alice";
```

### Fix 2: Initialize in constructor or use definite assignment assertion

```typescript
class User {
  name!: string; // definite assignment assertion
  constructor() {
    this.name = "Alice";
  }
}
```

### Fix 3: Use a default value

```typescript
let value: number = 0;
if (Math.random() > 0.5) {
  value = 1;
}
```

### Fix 4: Use definite assignment assertion (non-null)

```typescript
class Component {
  el!: HTMLElement; // tells TS "I'll initialize this"
  init() {
    this.el = document.getElementById("app")!;
  }
}
```

## Related Errors

- [TS2532: Object is possibly 'undefined']({{< relref "/languages/typescript/ts2532-object" >}}) — undefined access.
- [TS2531: Object is possibly 'null']({{< relref "/languages/typescript/ts2531-object" >}}) — null access.
- [TS2722: Cannot invoke object which is possibly 'callable']({{< relref "/languages/typescript/ts2722-cannot-invoke" >}}) — undefined function call.
