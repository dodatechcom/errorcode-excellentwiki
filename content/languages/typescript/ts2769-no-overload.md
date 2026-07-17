---
title: "[Solution] TypeScript TS2769 — No overload matches this call"
description: "Fix TypeScript TS2769: No overload matches this call. Resolve overload resolution errors in TypeScript."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2769", "overload", "function-call", "type-mismatch", "signature"]
weight: 5
---

# TS2769 — No overload matches this call

TS2769 occurs when you call a function with overloaded signatures and none of the overloads match the provided arguments. TypeScript cannot find a single overload that accepts your argument types.

## Common Causes

```typescript
// Cause 1: Arguments don't match any overload
function process(input: string): string;
function process(input: number): number;
function process(input: string | number): string | number {
  return input;
}
process(true); // TS2769: no overload matches

// Cause 2: Spread arguments that don't fit
function log(msg: string): void;
function log(msg: string, level: number): void;
function log(...args: any[]): void {}
log("hello", "world"); // TS2769: 'string' not assignable to 'number'

// Cause 3: Generic constraint failure
function wrap<T extends HTMLElement>(el: T): T { return el; }
wrap(document.getElementById("myId")); // TS2769 if null
```

## How to Fix

### Fix 1: Match an existing overload

```typescript
process("hello"); // matches first overload
process(42);      // matches second overload
```

### Fix 2: Add a new overload for your use case

```typescript
function process(input: string): string;
function process(input: number): number;
function process(input: boolean): string; // add boolean overload
function process(input: string | number | boolean): string | number {
  return input;
}
```

### Fix 3: Fix the argument type

```typescript
const el = document.getElementById("myId");
if (el) {
  wrap(el); // el is now HTMLElement, not null
}
```

## Related Errors

- [TS2345: Argument not assignable]({{< relref "/languages/typescript/ts2345-argument" >}}) — single-signature argument mismatch.
- [TS2554: Expected X arguments but got Y]({{< relref "/languages/typescript/ts2554-expected" >}}) — wrong argument count.
- [TS2769: No overload matches]({{< relref "/languages/typescript/ts2769-no-overload" >}}) — complex overload failure.
