---
title: "[Solution] TypeScript TS2554 — Expected X arguments but got Y"
description: "Fix TypeScript TS2554: Expected X arguments but got Y. Resolve function argument count mismatches."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2554", "argument-count", "function-call", "expected-arguments"]
weight: 5
---

# TS2554 — Expected X arguments but got Y

TS2554 occurs when you call a function with a different number of arguments than its signature expects. This can mean too many or too few arguments.

## Common Causes

```typescript
// Cause 1: Missing required arguments
function greet(name: string, greeting: string) {
  return `${greeting}, ${name}`;
}
greet("Alice"); // TS2554: Expected 2 arguments, but got 1

// Cause 2: Too many arguments
function add(a: number, b: number) {
  return a + b;
}
add(1, 2, 3); // TS2554: Expected 2 arguments, but got 3

// Cause 3: Calling constructor with wrong count
class Point {
  constructor(x: number, y: number) {}
}
new Point(1); // TS2554
```

## How to Fix

### Fix 1: Provide the correct number of arguments

```typescript
greet("Alice", "Hello");
```

### Fix 2: Make parameters optional

```typescript
function greet(name: string, greeting: string = "Hello") {
  return `${greeting}, ${name}`;
}
greet("Alice"); // OK
```

### Fix 3: Use rest parameters for variadic functions

```typescript
function log(...args: string[]) {
  args.forEach(a => console.log(a));
}
log("a", "b", "c"); // OK
```

## Related Errors

- [TS2345: Argument not assignable]({{< relref "/languages/typescript/ts2345-argument" >}}) — argument type mismatch.
- [TS2794: Expected 1 arguments but got 0]({{< relref "/languages/typescript/ts2794-increment" >}}) — zero-argument variant.
- [TS2769: No overload matches this call]({{< relref "/languages/typescript/ts2769-no-overload" >}}) — overload resolution failure.
