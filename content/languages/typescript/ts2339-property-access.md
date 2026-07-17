---
title: "[Solution] TypeScript TS2339 — Property 'X' is a type-only import"
description: "Fix TypeScript TS2339: Property 'X' is a type-only import. Use import type for type-only imports."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2339 — Property 'X' is a type-only import

TS2339 can occur when you try to use a type-only import as a value. With `verbatimModuleSyntax` or `isolatedModules`, TypeScript enforces that type-only imports cannot be used at runtime.

## Common Causes

```typescript
// Cause 1: Using type import as value
import type { User } from "./types";
const u: User = { name: "Alice" }; // OK as type annotation
const u2 = new User(); // TS2339: User is type-only

// Cause 2: Re-exporting type as value
import type { Config } from "./config";
export { Config }; // TS2339: Config is type-only

// Cause 3: Import without 'type' used as type-only
import { Logger } from "./logger";
// Logger is only used as type, but imported as value
```

## How to Fix

### Fix 1: Use import type correctly

```typescript
import type { User } from "./types";
// Can only use User as a type
const u: User = { name: "Alice" };
```

### Fix 2: Separate value and type imports

```typescript
import { helper } from "./utils";
import type { Config } from "./config";
```

### Fix 3: Use inline type import

```typescript
import { helper, type Config } from "./module";
```

## Related Errors

- [TS2339: Property does not exist on type]({{< relref "/languages/typescript/ts2339-property" >}}) — regular property access.
- [TS2693: 'X' only refers to a type]({{< relref "/languages/typescript/ts2693-X-only-referenced" >}}) — type used as value.
- [TS2307: Cannot find module]({{< relref "/languages/typescript/ts2307-cannot-find-module" >}}) — module not found.
