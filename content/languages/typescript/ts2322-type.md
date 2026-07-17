---
title: "[Solution] TypeScript TS2322 — Type 'X' is not assignable to type 'Y'"
description: "Fix TypeScript TS2322: Type 'X' is not assignable to type 'Y'. Learn why type mismatches occur and how to fix them."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2322 — Type 'X' is not assignable to type 'Y'

TS2322 occurs when you assign a value of one type to a variable, parameter, or return position that expects a different, incompatible type. TypeScript's structural type system checks that the source type satisfies all requirements of the target type.

## Common Causes

```typescript
// Cause 1: Assigning a string to a number
let age: number = "twenty-five"; // TS2322

// Cause 2: Missing required properties
interface User {
  name: string;
  age: number;
}
const user: User = { name: "Alice" }; // TS2322: Property 'age' is missing

// Cause 3: Assigning nullable to non-nullable
let name: string = null; // TS2322 if strictNullChecks is on

// Cause 4: Returning wrong type from function
function getLength(): number {
  return "hello"; // TS2322
}
```

## How to Fix

### Fix 1: Use the correct type

```typescript
// Wrong
let age: number = "twenty-five";

// Correct
let age: number = 25;
```

### Fix 2: Provide all required properties

```typescript
const user: User = { name: "Alice", age: 30 };
```

### Fix 3: Handle nullable values properly

```typescript
// Accept null
let name: string | null = null;

// Use a default
let name: string = "unknown";
```

### Fix 4: Use type assertions when you know the type

```typescript
const input = document.getElementById("name") as HTMLInputElement;
input.value = "Alice";
```

## Examples

```typescript
enum Color { Red, Green, Blue }
enum Direction { Up, Down }

let c: Color = Color.Red;
let d: Direction = c; // TS2322

interface Config {
  host: string;
  port: number;
}
const config: Config = { host: "localhost", port: 3000, debug: true }; // TS2322
```

## Related Errors

- [TS2345: Argument not assignable]({{< relref "/languages/typescript/ts2345-argument" >}}) — similar but for function arguments.
- [TS2741: Property is missing in type]({{< relref "/languages/typescript/ts2741-property" >}}) — specific variant for missing properties.
- [TS2352: Type assertion error]({{< relref "/languages/typescript/ts2322" >}}) — type assertion issues.
