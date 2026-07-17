---
title: "[Solution] TypeScript TS2503 — Cannot find namespace 'X'"
description: "Fix TypeScript TS2503: Cannot find namespace 'X'. Resolve namespace reference errors."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2503", "namespace", "cannot-find", "reference", "not-found"]
weight: 5
---

# TS2503 — Cannot find namespace 'X'

TS2503 occurs when you reference a namespace that TypeScript cannot find in the current scope. This can happen if the namespace is not declared, imported, or is in a different file without proper reference.

## Common Causes

```typescript
// Cause 1: Referencing undeclared namespace
const val: MyNamespace.Type = {}; // TS2503: Cannot find namespace 'MyNamespace'

// Cause 2: Missing triple-slash reference
// file: types.d.ts declares namespace GlobalTypes
// file: app.ts uses GlobalTypes without reference

// Cause 3: Wrong namespace import
namespace A {
  export type Item = { id: number };
}
const item: B.Item = { id: 1 }; // TS2503
```

## How to Fix

### Fix 1: Add triple-slash reference

```typescript
/// <reference path="./types.d.ts" />
const val: MyNamespace.Type = {};
```

### Fix 2: Import the namespace

```typescript
import { MyNamespace } from "./types";
const val: MyNamespace.Type = {};
```

### Fix 3: Fix the namespace name

```typescript
const item: A.Item = { id: 1 };
```

### Fix 4: Use ambient declaration

```typescript
declare namespace MyNamespace {
  type Type = { /* ... */ };
}
```

## Related Errors

- [TS2304: Cannot find name]({{< relref "/languages/typescript/ts2304-cannot-find" >}}) — undefined identifier.
- [TS2694: Namespace has no exported member]({{< relref "/languages/typescript/ts2694-namespace" >}}) — member not found.
- [TS2307: Cannot find module]({{< relref "/languages/typescript/ts2307-cannot-find-module" >}}) — module not found.
