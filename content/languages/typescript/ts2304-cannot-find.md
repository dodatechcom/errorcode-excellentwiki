---
title: "[Solution] TypeScript TS2304 — Cannot find name 'X'"
description: "Fix TypeScript TS2304: Cannot find name 'X'. Resolve undefined identifier errors in TypeScript."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2304", "cannot-find-name", "undefined-identifier", "not-defined"]
weight: 5
---

# TS2304 — Cannot find name 'X'

TS2304 occurs when TypeScript encounters a name it cannot resolve. This typically means a variable, function, class, or type is used without being declared or imported.

## Common Causes

```typescript
// Cause 1: Using undeclared variable
console.log(myVar); // TS2304: Cannot find name 'myVar'

// Cause 2: Missing import
// file: app.ts
greet("Alice"); // TS2304 if greet is defined in utils.ts but not imported

// Cause 3: Missing global type definition
console.log(process.env.NODE_ENV); // TS2304 if @types/node not installed

// Cause 4: Typo in name
const userName = "Alice";
console.log(userNme); // TS2304: typo
```

## How to Fix

### Fix 1: Declare the variable

```typescript
const myVar = "hello";
console.log(myVar);
```

### Fix 2: Import the function

```typescript
import { greet } from "./utils";
greet("Alice");
```

### Fix 3: Install type definitions

```bash
npm install --save-dev @types/node
```

### Fix 4: Add global type declaration

```typescript
// global.d.ts
declare const myGlobal: string;
```

## Related Errors

- [TS2307: Cannot find module]({{< relref "/languages/typescript/ts2307-cannot-find-module" >}}) — module not found.
- [TS2552: Cannot find name - did you mean]({{< relref "/languages/typescript/ts2552-cannot-find-name" >}}) — similar name suggestions.
- [TS2503: Cannot find namespace]({{< relref "/languages/typescript/ts2503-cannot-find-namespace" >}}) — namespace not found.
