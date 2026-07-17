---
title: "[Solution] TypeScript TS1109 — Expression expected"
description: "Fix TypeScript TS1109: Expression expected. Resolve syntax errors where an expression is required but not found."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS1109 — Expression expected

TS1109 is a syntax error indicating TypeScript expected an expression at a position where none was found. This typically happens with malformed function calls, object literals, or template literals.

## Common Causes

```typescript
// Cause 1: Missing argument in function call
doSomething();  // if function expects args and comma is missing
doSomething(, "hello"); // TS1109: expression expected before comma

// Cause 2: Empty template literal issue
const msg = `Hello, ${}`; // TS1109: expression expected inside ${}

// Cause 3: Invalid object syntax
const obj = {
  name: "Alice"
  age: 30  // TS1109 if comma missing
};

// Cause 4: Malformed ternary
const x = true ? ; // TS1109: expression expected after ?
```

## How to Fix

### Fix 1: Check for missing expressions

```typescript
// Remove extra commas
doSomething("hello");

// Fill in template literal
const msg = `Hello, ${name}`;
```

### Fix 2: Add missing commas in objects

```typescript
const obj = {
  name: "Alice",
  age: 30
};
```

### Fix 3: Complete ternary expressions

```typescript
const x = true ? "yes" : "no";
```

## Related Errors

- [TS1005: ';' expected]({{< relref "/languages/typescript/ts1005-semicolon" >}}) — missing semicolon.
- [TS1128: Declaration or statement expected]({{< relref "/languages/typescript/ts1128-declaration" >}}) — missing declaration.
- [TS1136: Expected block of statements]({{< relref "/languages/typescript/ts1136-block" >}}) — missing block.
