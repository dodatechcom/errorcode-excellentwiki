---
title: "[Solution] TypeScript TS2349 — This expression is not callable"
description: "Fix TypeScript TS2349: This expression is not callable. Resolve function call errors on non-callable expressions."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2349 — This expression is not callable

TS2349 occurs when you try to call an expression as a function, but its type does not include a call signature. The expression is not a function or callable object.

## Common Causes

```typescript
// Cause 1: Calling a non-function variable
const name: string = "Alice";
name(); // TS2349: This expression is not callable

// Cause 2: Importing a module but calling the wrong thing
import config from "./config";
config(); // TS230 if config is an object, not a function

// Cause 3: Calling a class as a function
class Foo {}
Foo(); // TS2349 — must use 'new'

// Cause 4: Overloaded function not callable as expected
function create(): string;
function create(n: number): number[];
function create(n?: number): string | number[] {
  return n ? [] : "";
}
create; // TS2349 if accessed without calling
```

## How to Fix

### Fix 1: Verify the variable is a function

```typescript
const greet = (name: string) => `Hello, ${name}`;
greet("Alice"); // OK
```

### Fix 2: Use 'new' for class instantiation

```typescript
const instance = new Foo();
```

### Fix 3: Check import name

```typescript
import { createConfig } from "./config";
createConfig(); // call the actual function
```

## Related Errors

- [TS2693: 'X' only refers to a type]({{< relref "/languages/typescript/ts2693-X-only-referenced" >}}) — calling a type as a value.
- [TS2304: Cannot find name]({{< relref "/languages/typescript/ts2304-cannot-find" >}}) — undefined identifier.
- [TS2554: Expected X arguments but got Y]({{< relref "/languages/typescript/ts2554-expected" >}}) — argument count mismatch.
