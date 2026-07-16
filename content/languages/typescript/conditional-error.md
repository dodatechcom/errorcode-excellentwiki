---
title: "[Solution] TypeScript Conditional Type Resolution Failed — Conditional Type Error Fix"
description: "Fix TypeScript conditional type resolution errors. Understand conditional type syntax, infer keyword, and distributed conditional types."
languages: ["typescript"]
severities: ["error"]
error-types: ["type-error"]
tags: ["conditional-type", "type-resolution", "infer", "distributed-type", "type-error"]
weight: 5
---

# TypeScript: Conditional type resolution failed

A conditional type error occurs when a conditional type (`T extends U ? X : Y`) cannot be resolved because the type parameter is not narrowed, the `infer` keyword is used incorrectly, or the conditional type creates an infinitely recursive type. These errors appear when working with advanced generic types and type-level programming.

## Common Causes

- **Non-narrowable type parameter** — `T` is `unknown` or a union, and the conditional doesn't distribute
- **Incorrect `infer` usage** — `infer` in a position TypeScript can't resolve
- **Recursive conditional types** — a conditional type refers to itself without a base case
- **Type instantiation too deep** — deeply nested conditional types exceed TypeScript's recursion limit

## How to Fix

```typescript
// Cause 1: Non-distributed conditional type
type IsString<T> = T extends string ? true : false;

type A = IsString<string | number>;  // should be true | false = boolean
// Sometimes this resolves to 'boolean' instead of the expected union

// Fix: use distributive conditional type with naked type parameter
type IsString<T> = T extends string ? true : false;

// Cause 2: Incorrect infer position
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

type X = ReturnType<string>;  // string doesn't extend function → never

// Fix: handle non-function types
type SafeReturnType<T> = T extends (...args: any[]) => infer R ? R : never;
type Y = SafeReturnType<() => string>;  // string

// Cause 3: Recursive conditional type without base case
type DeepReadonly<T> = T extends object
  ? { [K in keyof T]: DeepReadonly<T[K]> }  // infinite if T is circular
  : T;

// Fix: add a base case or limit recursion depth
type DeepReadonly<T> = T extends object
  ? { readonly [K in keyof T]: DeepReadonly<T[K]> }
  : T;
```

## Examples

```typescript
// Example 1: Extracting function return type
type Unwrap<T> = T extends Promise<infer U>
  ? U extends Promise<infer V>
    ? V
    : U
  : T;

type A = Unwrap<Promise<Promise<string>>>;  // string
type B = Unwrap<number>;  // number

// Example 2: Filtering array element types
type FilterStrings<T extends any[]> = T extends [infer Head, ...infer Tail]
  ? Head extends string
    ? [Head, ...FilterStrings<Tail>]
    : FilterStrings<Tail>
  : [];

type C = FilterStrings<[1, "a", 2, "b"]>;  // ["a", "b"]

// Example 3: Pattern matching with conditional types
type ExtractProperty<T, K extends string> = T extends { [P in K]: infer V }
  ? V
  : never;

type D = ExtractProperty<{ name: string; age: number }, "name">;  // string
type E = ExtractProperty<{ name: string }, "missing">;  // never
```

## Related Errors

- [TS2589: Type instantiation is excessively deep]({{< relref "/languages/typescript/ts2588" >}}) — recursion limit hit
- [TS2344: Type does not satisfy constraint]({{< relref "/languages/typescript/generic-error" >}}) — generic constraint violation
- [TS2315: Generic type requires type arguments]({{< relref "/languages/typescript/conditional-error" >}}) — missing generic parameters
