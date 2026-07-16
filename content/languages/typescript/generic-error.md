---
title: "[Solution] TypeScript Generic Type Assignment Error — Generic Constraint Violation Fix"
description: "Fix TypeScript 'Type X is not assignable to generic type parameter' errors. Understand generic constraints, type parameters, and variance."
languages: ["typescript"]
severities: ["error"]
error-types: ["type-error"]
tags: ["generic-error", "type-parameter", "generic-constraint", "variance", "type-error"]
weight: 5
---

# TypeScript: Type 'X' is not assignable to generic type parameter

This error occurs when you pass a type to a generic function or class that doesn't satisfy the generic's constraints. Unlike simple type assignment errors, generic errors involve type parameters that may have `extends` clauses, default values, or complex variance rules.

## Common Causes

- **Generic constraint violated** — passing a type that doesn't extend the constraint type
- **Covariance/contravariance issues** — passing a derived type where a base type is expected in a callback position
- **Default type mismatch** — the inferred type doesn't match the generic's default
- **Complex mapped/conditional type** — the resulting type from a mapped type doesn't match the target

## How to Fix

```typescript
// Cause 1: Generic constraint violation
function first<T extends { length: number }>(arr: T): T {
  return arr;
}

first(42);  // TS2345: number not assignable to { length: number }

// Fix: pass a type that satisfies the constraint
first([1, 2, 3]);  // OK — arrays have .length

// Cause 2: Generic with interface constraint
interface HasId {
  id: number;
}

function findById<T extends HasId>(items: T[], id: number): T | undefined {
  return items.find(item => item.id === id);
}

const users = [{ name: "Alice" }];  // missing 'id'
findById(users, 1);  // TS2345: { name: string } not assignable to HasId

// Fix: ensure items have the required property
const users = [{ id: 1, name: "Alice" }];
findById(users, 1);  // OK

// Cause 3: Returning wrong type from generic function
function identity<T>(x: T): T {
  return x;
}

function broken<T>(x: T): T {
  return "hello" as T;  // TS2322: string not assignable to T
}

// Fix: return the actual parameter
function correct<T>(x: T): T {
  return x;
}
```

## Examples

```typescript
// Example 1: Generic class with constraint
class Container<T extends object> {
  constructor(public value: T) {}
}

new Container(42);  // TS2344: number doesn't satisfy 'object'

// Fix
new Container({ data: 42 });

// Example 2: Generic function with multiple constraints
function merge<T extends object, U extends object>(a: T, b: U): T & U {
  return { ...a, ...b };
}

merge({ x: 1 }, { y: "hello" });  // OK
merge({ x: 1 }, [1, 2, 3]);  // TS2345: array not assignable to object

// Example 3: Conditional type result doesn't match
type Unwrap<T> = T extends Promise<infer U> ? U : T;

function process<T>(val: Unwrap<T>): void {}

process<string>("hello");  // OK — Unwrap<string> is string
process<Promise<number>>(42);  // TS2345: number not assignable to Unwrap<Promise<number>>
```

## Related Errors

- [TS2322: Type not assignable]({{< relref "/languages/typescript/type-assignment" >}}) — non-generic type assignment
- [TS2345: Argument type not assignable]({{< relref "/languages/typescript/ts2345" >}}) — argument in generic context
- [TS2749: Referenced value is not a class]({{< relref "/languages/typescript/ts2749" >}}) — using non-class in generic context
