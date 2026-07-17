---
title: "[Solution] TypeScript TS2345 — Argument of type 'X' is not assignable to parameter"
description: "Fix TypeScript TS2345: Argument of type 'X' is not assignable to parameter of type 'Y'. Resolve function argument type mismatches."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2345", "argument", "parameter", "type-mismatch", "function-call"]
weight: 5
---

# TS2345 — Argument of type 'X' is not assignable to parameter of type 'Y'

TS2345 occurs when you pass an argument to a function that does not match the expected parameter type. This is one of the most common TypeScript errors and usually indicates a type mismatch at a call site.

## Common Causes

```typescript
// Cause 1: Passing wrong type to function
function greet(name: string) {
  console.log(`Hello, ${name}`);
}
greet(42); // TS2345: Argument of type 'number' is not assignable to parameter of type 'string'

// Cause 2: Nullable argument to non-nullable parameter
function process(value: number) {
  return value * 2;
}
process(null); // TS2345 if strictNullChecks is on

// Cause 3: Array type mismatch
function logItems(items: string[]) {
  items.forEach(item => console.log(item));
}
logItems([1, 2, 3]); // TS2345
```

## How to Fix

### Fix 1: Pass the correct type

```typescript
greet("Alice");
```

### Fix 2: Handle null with union type

```typescript
function process(value: number | null) {
  if (value === null) return 0;
  return value * 2;
}
```

### Fix 3: Map array to correct type

```typescript
logItems([1, 2, 3].map(String));
```

### Fix 4: Use overloads for flexible signatures

```typescript
function format(input: string): string;
function format(input: number): string;
function format(input: string | number): string {
  return String(input);
}
format("hello");
format(42);
```

## Related Errors

- [TS2322: Type not assignable]({{< relref "/languages/typescript/ts2322-type" >}}) — assignment rather than call site.
- [TS2554: Expected X arguments but got Y]({{< relref "/languages/typescript/ts2554-expected" >}}) — wrong argument count.
- [TS2769: No overload matches this call]({{< relref "/languages/typescript/ts2769-no-overload" >}}) — no overload accepts the arguments.
