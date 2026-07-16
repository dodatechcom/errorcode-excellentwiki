---
title: "[Solution] TypeScript Intersection Type Error — Conflicting Property Types Fix"
description: "Fix TypeScript intersection type errors when combining types with incompatible properties. Understand intersection semantics and resolve conflicts."
languages: ["typescript"]
severities: ["error"]
error-types: ["type-error"]
tags: ["intersection-type", "type-conflict", "combining-types", "type-error", "intersection"]
weight: 5
---

# TypeScript: Intersection type error

An intersection type error occurs when combining two types with `&` produces a type with conflicting property types — for example, `string & number` becomes `never` for that property. This often happens when merging interfaces, combining third-party types, or accidentally creating impossible types.

## Common Causes

- **Conflicting property types** — `A & B` where `A.x: string` and `B.x: number` produces `x: never`
- **Merging incompatible interfaces** — two interfaces with the same property but different types
- **Library type conflicts** — combining types from two libraries that define the same property differently
- **Incorrect mapped type** — a mapped type produces an intersection with conflicting types

## How to Fix

```typescript
// Cause 1: Conflicting property types
interface A {
  value: string;
}

interface B {
  value: number;
}

type C = A & B;  // value is never — string & number = never

// Fix: use a union or choose one type
type C = A | B;  // value is string | number

// Cause 2: Method signature conflicts
interface Logger {
  log(msg: string): void;
}

interface VerboseLogger {
  log(msg: string, level: number): void;
}

type Combined = Logger & VerboseLogger;
// log is (msg: string) => void & (msg: string, level: number) => void = never

// Fix: make the method signatures compatible
interface Logger {
  log(msg: string, level?: number): void;
}

// Cause 3: Third-party type conflict
interface React.CSSProperties {
  display: string;
}

interface TailwindProps {
  display: "flex" | "block" | "none";
}

// Fix: use declaration merging or override
```

## Examples

```typescript
// Example 1: Intersection of primitives is never
type Impossible = string & number;  // never
type AlsoImpossible = boolean & string;  // never

// Example 2: Function type intersection
type Fn1 = (x: number) => string;
type Fn2 = (x: string) => number;
type Combined = Fn1 & Fn2;
// Combined requires x to be both number AND string → x: never

// Example 3: Correct intersection usage
interface Person {
  name: string;
}

interface Employee {
  employeeId: number;
}

type PersonEmployee = Person & Employee;  // { name: string; employeeId: number }
// This works because there are no conflicting properties

const pe: PersonEmployee = { name: "Alice", employeeId: 123 };

// Example 4: Resolving conflicts with Pick/Omit
interface ConfigA {
  port: number;
  host: string;
}

interface ConfigB {
  port: string;  // conflicts with ConfigA.port
}

// Fix: override the conflicting property
type MergedConfig = Omit<ConfigA, "port"> & ConfigB;
// port is string (from ConfigB), host is string (from ConfigA)
```

## Related Errors

- [TS2322: Type not assignable]({{< relref "/languages/typescript/type-assignment" >}}) — resulting type can't be assigned
- [TS2345: Argument type not assignable]({{< relref "/languages/typescript/ts2345" >}}) — intersection passed as argument
- [TS2589: Type instantiation is excessively deep]({{< relref "/languages/typescript/ts2588" >}}) — recursive intersection types
