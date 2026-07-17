---
title: "[Solution] TypeScript Type 'never' Has No Properties — Exhaustive Check Fix"
description: "Fix TypeScript 'Type never has no properties' errors. Understand the never type, exhaustive checking, and unreachable code detection."
languages: ["typescript"]
severities: ["error"]
error-types: ["type-error"]
weight: 5
---

# TypeScript: Type 'never' has no properties

The `never` type represents values that never occur — a function that always throws, or a variable that can never be assigned a value. When you see "Type 'never' has no properties", you are trying to access properties or call methods on a value that TypeScript has determined is unreachable. This is actually a powerful feature for exhaustive type checking.

## Common Causes

- **Switch statement missing a case** — TypeScript narrows to `never` when all cases are covered, but if you add a new case, the `never` check catches it
- **Dead code after return/throw** — code that TypeScript knows cannot execute
- **Incorrect type narrowing** — a condition that TypeScript determines is impossible
- **Generic default resolving to never** — a type parameter that defaults to `never` is used directly

## How to Fix

```typescript
// Cause 1: Switch statement not exhaustive
type Shape = "circle" | "square" | "triangle";

function area(shape: Shape): number {
  switch (shape) {
    case "circle":
      return 3.14;
    case "square":
      return 1;
    // Missing "triangle" case — no error here but adding it later causes issues
  }
}

// Fix: use exhaustive check
function area(shape: Shape): number {
  switch (shape) {
    case "circle":
      return 3.14;
    case "square":
      return 1;
    case "triangle":
      return 0.5;
    default:
      const _exhaustive: never = shape;  // compile error if case is missing
      return _exhaustive;
  }
}

// Cause 2: Accessing property on narrowed never
function process(value: string | number) {
  if (typeof value === "string" && typeof value === "number") {
    // This condition is impossible — value is 'never' here
    console.log(value.toUpperCase());  // TS2339: 'never' has no property 'toUpperCase'
  }
}

// Cause 3: Return type is never
function throwError(msg: string): never {
  throw new Error(msg);
}

const result = throwError("oops");
result.foo;  // TS2339: 'never' has no property 'foo'
```

## Examples

```typescript
// Example 1: Exhaustive discriminated union check
interface Circle { kind: "circle"; radius: number; }
interface Square { kind: "square"; side: number; }
type Shape = Circle | Square;

function describe(shape: Shape): string {
  switch (shape.kind) {
    case "circle":
      return `Circle with radius ${shape.radius}`;
    case "square":
      return `Square with side ${shape.side}`;
    default:
      const _check: never = shape;
      return _check;  // ensures all cases handled
  }
}

// Example 2: never in conditional types
type NonNullable<T> = T extends null | undefined ? never : T;
type A = NonNullable<string | null>;  // string

// Example 3: Asserting never for impossible paths
function processInput(input: unknown): string {
  if (typeof input === "string") return input;
  if (typeof input === "number") return String(input);
  if (typeof input === "boolean") return input ? "yes" : "no";
  const _impossible: never = input;  // input is never — all cases handled
  return _impossible;
}
```

## Related Errors

- [TS2322: Type not assignable]({{< relref "/languages/typescript/type-assignment" >}}) — type narrowing leads to never
- [TS2345: Argument type not assignable]({{< relref "/languages/typescript/ts2345" >}}) — never passed where concrete type expected
- [TS2578: Unused '@ts-expect-error' directive]({{< relref "/languages/typescript/ts2552" >}}) — related to unreachable code
