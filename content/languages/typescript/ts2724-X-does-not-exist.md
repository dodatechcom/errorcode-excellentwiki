---
title: "[Solution] TypeScript TS2724 — X does not exist in the scope"
description: "Fix TypeScript TS2724: Module has no exported member. Ensure proper imports and exports."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2724", "does-not-exist", "scope", "export", "import"]
weight: 5
---

# TS2724 — Module has no exported member 'X' or it was removed

TS2724 occurs when you import a member that was removed from a module or never existed. This often happens after package updates.

## Common Causes

```typescript
// Cause 1: Member removed in package update
import { oldFunction } from "some-package"; // TS2724 if removed

// Cause 2: Wrong export name
import { procesor } from "./cpu"; // TS2724

// Cause 3: Breaking change in major version
import { Component } from "old-framework"; // TS2724 after migration
```

## How to Fix

### Fix 1: Check package changelog

```bash
npm info some-package --json
# Check what was renamed or removed
```

### Fix 2: Fix the import name

```typescript
import { processor } from "./cpu";
```

### Fix 3: Use replacement API

```typescript
import { newFunction } from "some-package"; // use the replacement
```

## Related Errors

- [TS2305: Module has no exported member]({{< relref "/languages/typescript/ts2305-module-has-no-exported" >}}) — similar error.
- [TS2307: Cannot find module]({{< relref "/languages/typescript/ts2307-cannot-find-module" >}}) — module not found.
- [TS2694: Namespace has no exported member]({{< relref "/languages/typescript/ts2694-namespace" >}}) — namespace variant.
