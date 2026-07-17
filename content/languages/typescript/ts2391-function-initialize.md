---
title: "[Solution] TypeScript TS2391 — Function with qualified name"
description: "Fix TypeScript TS2391: Function with qualified name. Resolve function initialization and declaration errors."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2391 — Function with qualified name

TS2391 occurs when you try to redeclare or reinitialize a function that already has a qualified name in the current scope. This typically happens with duplicate function declarations or incorrect namespace usage.

## Common Causes

```typescript
// Cause 1: Duplicate function declaration with different signature
function greet(name: string): void;
function greet(name: string, greeting: string): void;
function greet(name: string, greeting?: string): void {
  console.log(greeting || "Hello", name);
}
// Redeclaring causes TS2391
function greet(name: string) {} // TS2391

// Cause 2: Trying to reassign a function in namespace
namespace Utils {
  export function helper() {}
}
Utils.helper = function() {}; // TS2391
```

## How to Fix

### Fix 1: Use function overloads properly

```typescript
function greet(name: string): void;
function greet(name: string, greeting: string): void;
function greet(name: string, greeting?: string): void {
  console.log(greeting || "Hello", name);
}
```

### Fix 2: Use const for function reassignment

```typescript
let greet = (name: string) => `Hello, ${name}`;
greet = (name: string) => `Hi, ${name}`; // OK with let
```

### Fix 3: Avoid duplicate declarations

```typescript
// Only one declaration per scope
function helper() {}
```

## Related Errors

- [TS2300: Duplicate identifier]({{< relref "/languages/typescript/ts2300-duplicate-identifier" >}}) — duplicate names.
- [TS2391: Function redeclaration]({{< relref "/languages/typescript/ts2391-function-initialize" >}}) — function already declared.
- [TS2769: No overload matches this call]({{< relref "/languages/typescript/ts2769-no-overload" >}}) — overload issues.
