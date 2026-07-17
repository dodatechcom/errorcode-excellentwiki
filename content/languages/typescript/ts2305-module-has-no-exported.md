---
title: "[Solution] TypeScript TS2305 — Module 'X' has no exported member 'Y'"
description: "Fix TypeScript TS2305: Module 'X' has no exported member 'Y'. Import only exported members."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2305 — Module '"X"' has no exported member 'Y'

TS2305 occurs when you import a member from a module that does not export that name. The member may not be exported, may not exist, or the module may have changed its API.

## Common Causes

```typescript
// Cause 1: Importing non-exported member
// file: utils.ts
function helper() {} // not exported

// file: app.ts
import { helper } from "./utils"; // TS2305

// Cause 2: Wrong package version
import { newFeature } from "some-package"; // TS2305 if not in installed version

// Cause 3: Typo in member name
import { procesor } from "./cpu"; // TS2305: should be 'processor'
```

## How to Fix

### Fix 1: Export the member

```typescript
// file: utils.ts
export function helper() {}
```

### Fix 2: Check package version

```bash
npm ls some-package
# Update if needed
npm install some-package@latest
```

### Fix 3: Fix the import name

```typescript
import { processor } from "./cpu";
```

### Fix 4: Use default import

```typescript
import utils from "./utils";
utils.helper();
```

## Related Errors

- [TS2614: Module has no exported member]({{< relref "/languages/typescript/ts2614-module-has-no-exported" >}}) — similar variant.
- [TS2307: Cannot find module]({{< relref "/languages/typescript/ts2307-cannot-find-module" >}}) — module not found.
- [TS2694: Namespace has no exported member]({{< relref "/languages/typescript/ts2694-namespace" >}}) — namespace variant.
