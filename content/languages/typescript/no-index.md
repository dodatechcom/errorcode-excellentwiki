---
title: "[Solution] TypeScript Implicit Any Type — Expression Has No Index Signature Fix"
description: "Fix TypeScript 'Element implicitly has an any type' errors. Add index signatures, use type assertions, or properly type dynamic property access."
languages: ["typescript"]
severities: ["error"]
error-types: ["type-error"]
tags: ["implicit-any", "no-index-signature", "dynamic-access", "type-error", "ts7053"]
weight: 5
---

# TypeScript: Element implicitly has an 'any' type because expression of type 'X' is not of type 'Y'

This error occurs when you access a property on an object using a dynamic key, but the object's type doesn't have an index signature that allows that key. TypeScript cannot guarantee the key exists, so it would implicitly be `any`.

## Common Causes

- **Dynamic property access without index signature** — `obj[dynamicKey]` where `obj` has no index signature
- **Using a variable as a key on a typed object** — `record[key]` where `key` isn't a known literal
- **Enum used as object key** — `obj[enumValue]` where the object type doesn't include the enum
- **Dot notation with dynamic string** — accessing properties that aren't declared in the interface

## How to Fix

```typescript
// Cause 1: Dynamic access on typed object
interface User {
  name: string;
  age: number;
}

const user: User = { name: "Alice", age: 30 };
const field = "name";
console.log(user[field]);  // TS7053: Element implicitly has an 'any' type

// Fix 1a: Add index signature
interface User {
  name: string;
  age: number;
  [key: string]: string | number;
}

// Fix 1b: Use type assertion
console.log(user[field as keyof User]);

// Cause 2: Record access without proper typing
const scores: Record<string, number> = { math: 90, science: 85 };
const key = "math";
console.log(scores[key]);  // this works because Record has an index signature

// Cause 3: Enum as key
enum Color { Red = "red", Blue = "blue" }
const palette: Record<Color, string> = {
  [Color.Red]: "#ff0000",
  [Color.Blue]: "#0000ff",
};

const c = Color.Red;
console.log(palette[c]);  // this works with Record<Color, string>
```

## Examples

```typescript
// Example 1: Object literal without index signature
interface Config {
  host: string;
  port: number;
}

const config: Config = { host: "localhost", port: 3000 };
const keys: string[] = ["host", "port"];

keys.forEach(key => {
  console.log(config[key]);  // TS7053
});

// Fix: use keyof assertion
keys.forEach(key => {
  console.log(config[key as keyof Config]);
});

// Example 2: Nested dynamic access
interface Nested {
  a: { b: { c: number } };
}

const obj: Nested = { a: { b: { c: 42 } } };
const path = ["a", "b", "c"];

// TypeScript can't verify this path is valid
path.reduce((acc, key) => acc[key], obj);  // TS7053

// Fix: use type assertion
path.reduce((acc: any, key) => acc[key], obj) as any;
```

## Related Errors

- [TS7006: Parameter has no type annotation]({{< relref "/languages/typescript/ts7006" >}}) — implicit `any` on parameters
- [TS7031: Binding element has implicit any]({{< relref "/languages/typescript/ts7031" >}}) — destructured parameters without types
- [TS2339: Property does not exist on type]({{< relref "/languages/typescript/ts2339" >}}) — static access to non-existent property
