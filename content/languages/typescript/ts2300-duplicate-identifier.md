---
title: "[Solution] TypeScript TS2300 — Duplicate identifier"
description: "Fix TypeScript TS2300: Duplicate identifier. Resolve duplicate variable, function, or type declarations."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2300 — Duplicate identifier

TS2300 occurs when two declarations in the same scope have the same name. This can happen with variables, functions, classes, or type declarations.

## Common Causes

```typescript
// Cause 1: Duplicate variable declaration
let x = 5;
let x = 10; // TS2300: Duplicate identifier 'x'

// Cause 2: Duplicate function declaration
function greet() {}
function greet() {} // TS2300

// Cause 3: Conflicting type declarations
interface Config {
  port: number;
}
interface Config {
  host: string; // TS2300: duplicate identifier
}

// Cause 4: Conflicting with global type
let Array = [1, 2, 3]; // TS2300: 'Array' already defined
```

## How to Fix

### Fix 1: Rename one of the declarations

```typescript
let x1 = 5;
let x2 = 10;
```

### Fix 2: Use unique names or modules

```typescript
// In separate modules
// file1.ts
export const config1 = {};

// file2.ts
export const config2 = {};
```

### Fix 3: Merge interface declarations

```typescript
interface Config {
  port: number;
  host: string;
}
```

### Fix 4: Avoid shadowing globals

```typescript
const myArray = [1, 2, 3]; // use different name
```

## Related Errors

- [TS2309: Variable is declared but never read]({{< relref "/languages/typescript/ts2309-variable-const" >}}) — unused declaration.
- [TS2391: Function redeclaration]({{< relref "/languages/typescript/ts2391-function-initialize" >}}) — function redeclaration.
- [TS2464: Circular definition of import alias]({{< relref "/languages/typescript/ts2464-cyclic" >}}) — circular imports.
