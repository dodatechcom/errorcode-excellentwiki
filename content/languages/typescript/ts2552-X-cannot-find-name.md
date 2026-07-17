---
title: "[Solution] TypeScript TS2552 — Cannot find name 'X'. Did you mean 'Y'?"
description: "Fix TypeScript TS2552: Cannot find name 'X'. Did you mean 'Y'? Fix undefined identifiers with suggestions."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2552 — Cannot find name 'X'. Did you mean 'Y'?

TS2552 is an enhanced version of TS2304 that provides suggestions when an undefined identifier resembles an existing name.

## Common Causes

```typescript
// Cause 1: Typo in function name
function myFunction() {}
myFuntion(); // TS2552: Did you mean 'myFunction'?

// Cause 2: Wrong import name
import { procesor } from "./cpu"; // TS2552: Did you mean 'processor'?

// Cause 3: Similar variable exists
const userNme = "Alice"; // typo in declaration
```

## How to Fix

### Fix 1: Use the suggested name

```typescript
myFunction(); // correct spelling
```

### Fix 2: Fix the import

```typescript
import { processor } from "./cpu";
```

### Fix 3: Rename the declaration

```typescript
const userName = "Alice";
```

## Related Errors

- [TS2304: Cannot find name]({{< relref "/languages/typescript/ts2304-cannot-find" >}}) — no suggestions available.
- [TS2551: Property does not exist - did you mean]({{< relref "/languages/typescript/ts2551-property" >}}) — property variant.
- [TS2307: Cannot find module]({{< relref "/languages/typescript/ts2307-cannot-find-module" >}}) — module not found.
