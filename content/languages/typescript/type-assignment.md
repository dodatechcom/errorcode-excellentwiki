---
title: "[Solution] TypeScript Type Assignment Error — Type Not Assignable to Type Fix"
description: "Fix TypeScript 'Type X is not assignable to type Y' errors. Understand structural typing, type narrowing, and proper type assertions."
languages: ["typescript"]
severities: ["error"]
error-types: ["type-error"]
weight: 5
---

# TypeScript: Type 'X' is not assignable to type 'Y'

This error occurs when you assign a value of one type to a variable, parameter, or return position that expects a different, incompatible type. TypeScript's structural type system checks that the source type satisfies all requirements of the target type.

## Common Causes

- **Primitive type mismatch** — assigning a `string` to a `number` variable
- **Missing required properties** — an object literal is missing fields required by the target interface
- **Strict null violations** — assigning `null` or `undefined` to a non-nullable type (with `strictNullChecks`)
- **Enum or literal type mismatch** — using a value from one enum where another is expected

## How to Fix

```typescript
// Cause 1: Primitive mismatch
let age: number = "twenty-five";  // TS2322

// Fix: use the correct type
let age: number = 25;

// Cause 2: Missing properties
interface User {
  name: string;
  age: number;
}
const user: User = { name: "Alice" };  // TS2322

// Fix: provide all required fields
const user: User = { name: "Alice", age: 30 };

// Cause 3: Null assigned to non-nullable
let name: string = null;  // TS2322

// Fix: use union type
let name: string | null = null;

// Cause 4: Wrong function return type
function getLength(): number {
  return "hello";  // TS2322
}

// Fix: return the correct type
function getLength(): string {
  return "hello";
}
```

## Examples

```typescript
// Enum mismatch
enum Color { Red, Green, Blue }
enum Direction { Up, Down }
let c: Color = Color.Red;
let d: Direction = c;  // TS2322: Color not assignable to Direction

// Excess properties in object literal
interface Config {
  host: string;
  port: number;
}
const config: Config = { host: "localhost", port: 3000, debug: true };  // TS2322

// Function argument mismatch
function greet(name: string) {}
greet(42);  // TS2322: number not assignable to string
```

## Related Errors

- [TS2345: Argument of type not assignable]({{< relref "/languages/typescript/ts2345" >}}) — similar but for function arguments
- [TS2741: Property is missing in type]({{< relref "/languages/typescript/ts2741" >}}) — missing required properties
- [TS2352: Conversion may be a mistake]({{< relref "/languages/typescript/ts2352" >}}) — type assertion issues
