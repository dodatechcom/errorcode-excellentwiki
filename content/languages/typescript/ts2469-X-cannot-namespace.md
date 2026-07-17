---
title: "[Solution] TypeScript TS2469 — X cannot be used as a namespace"
description: "Fix TypeScript TS2469: X cannot be used as a namespace. Use proper namespace or module syntax."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2469", "cannot-be-used", "namespace", "module", "import"]
weight: 5
---

# TS2469 — 'X' cannot be used as a namespace

TS2469 occurs when you try to use a module or class as a namespace. Only namespace declarations can be used with dot notation for sub-members.

## Common Causes

```typescript
// Cause 1: Using module as namespace
import React from "react";
React.createElement("div"); // OK if React has this export

// Cause 2: Trying to access sub-members of class
class MyClass {
  static value = 42;
}
MyClass.Nested; // TS2469: MyClass cannot be used as namespace

// Cause 3: Wrong namespace access
import * as utils from "./utils";
utils.sub.value; // TS2469 if 'sub' is not a namespace
```

## How to Fix

### Fix 1: Use proper import/require

```typescript
import { something } from "./module";
// or
const { something } = require("./module");
```

### Fix 2: Use static members correctly

```typescript
MyClass.value; // access static property directly
```

### Fix 3: Create a proper namespace

```typescript
namespace Utils {
  export const sub = {
    value: 42,
  };
}
Utils.sub.value; // OK
```

## Related Errors

- [TS2503: Cannot find namespace]({{< relref "/languages/typescript/ts2503-cannot-find-namespace" >}}) — namespace not found.
- [TS2304: Cannot find name]({{< relref "/languages/typescript/ts2304-cannot-find" >}}) — undefined identifier.
- [TS2307: Cannot find module]({{< relref "/languages/typescript/ts2307-cannot-find-module" >}}) — module not found.
