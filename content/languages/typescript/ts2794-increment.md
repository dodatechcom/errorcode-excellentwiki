---
title: "[Solution] TypeScript TS2794 — Expected 1 arguments but got 0"
description: "Fix TypeScript TS2794: Expected 1 arguments but got 0. Resolve function call argument count errors."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2794", "arguments", "function-call", "increment", "argument-count"]
weight: 5
---

# TS2794 — Expected 1 arguments but got 0

TS2794 occurs when you call a function that requires arguments but provide none. In the context of incrementing, this often happens when trying to increment a value using a function that expects an argument.

## Common Causes

```typescript
// Cause 1: Function requires an argument
function increment(value: number) {
  return value + 1;
}
increment(); // TS2794: Expected 1 arguments, but got 0

// Cause 2: Calling method without required parameter
const arr = [1, 2, 3];
arr.indexOf(); // TS2794: Expected 1 arguments, but got 0

// Cause 3: Constructor expecting arguments
class Counter {
  constructor(initial: number) {}
}
new Counter(); // TS2794
```

## How to Fix

### Fix 1: Provide the required argument

```typescript
increment(5);
```

### Fix 2: Use optional parameters

```typescript
function increment(value: number = 0) {
  return value + 1;
}
increment(); // OK — uses default
```

### Fix 3: Use default parameter in constructor

```typescript
class Counter {
  constructor(initial: number = 0) {}
}
new Counter(); // OK
```

## Related Errors

- [TS2554: Expected X arguments but got Y]({{< relref "/languages/typescript/ts2554-expected" >}}) — general argument count mismatch.
- [TS2345: Argument not assignable]({{< relref "/languages/typescript/ts2345-argument" >}}) — argument type issues.
- [TS2488: Type must have Symbol.iterator method]({{< relref "/languages/typescript/ts2794-increment" >}}) — iterator errors.
