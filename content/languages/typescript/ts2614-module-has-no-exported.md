---
title: "[Solution] TypeScript TS2614 — Module has no exported member"
description: "Fix TypeScript TS2614: Module has no exported member. Import only exported members from modules."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2614", "module", "exported-member", "import", "not-exported"]
weight: 5
---

# TS2614 — Module has no exported member 'X'

TS2614 occurs when you import a member from a module that does not export that name. The member may not exist, may not be exported, or may have been renamed.

## Common Causes

```typescript
// Cause 1: Importing non-exported member
// file: utils.ts
function helper() {} // not exported

// file: app.ts
import { helper } from "./utils"; // TS2614

// Cause 2: Wrong export name
// file: utils.ts
export function process() {}

// file: app.ts
import { proces } from "./utils"; // TS2614: typo

// Cause 3: Named vs default export confusion
// file: utils.ts
export default function helper() {}

// file: app.ts
import { helper } from "./utils"; // TS2614: should use default
```

## How to Fix

### Fix 1: Export the member

```typescript
// file: utils.ts
export function helper() {} // add export
```

### Fix 2: Fix the import name

```typescript
import { process } from "./utils"; // correct name
```

### Fix 3: Use correct import style

```typescript
// For default export
import helper from "./utils";

// For named export
import { helper } from "./utils";
```

## Related Errors

- [TS2305: Module has no exported member]({{< relref "/languages/typescript/ts2305-module-has-no-exported" >}}) — similar error.
- [TS2693: 'X' only refers to a type]({{< relref "/languages/typescript/ts2693-X-only-referenced" >}}) — type-only usage.
- [TS2307: Cannot find module]({{< relref "/languages/typescript/ts2307-cannot-find-module" >}}) — module not found.
