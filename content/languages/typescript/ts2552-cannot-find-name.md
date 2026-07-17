---
title: "[Solution] TypeScript TS2552 — Cannot find name 'X'. Did you mean 'Y'?"
description: "Fix TypeScript TS2552: Cannot find name 'X'. Did you mean 'Y'? Use TypeScript's suggestions to fix typos."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2552 — Cannot find name 'X'. Did you mean 'Y'?

TS2552 is an enhanced version of TS2304 where TypeScript detects an undefined identifier and suggests a similar name that does exist in the current scope.

## Common Causes

```typescript
// Cause 1: Typo in variable name
const userName = "Alice";
console.log(userNme); // TS2552: Did you mean 'userName'?

// Cause 2: Wrong import name
import { procesor } from "./cpu"; // TS2552: Did you mean 'processor'?

// Cause 3: Similar name exists in scope
const myFunction = () => {};
myFuntion(); // TS2552: Did you mean 'myFunction'?
```

## How to Fix

### Fix 1: Use the suggested name

```typescript
console.log(userName); // correct spelling
```

### Fix 2: Accept IDE suggestions

TypeScript language servers provide quick fixes for typos — accept the suggestion to auto-correct.

### Fix 3: Declare the missing name

```typescript
const userNme = "Bob"; // if this was intentional
```

## Related Errors

- [TS2304: Cannot find name]({{< relref "/languages/typescript/ts2304-cannot-find" >}}) — no suggestions available.
- [TS2551: Property does not exist - did you mean]({{< relref "/languages/typescript/ts2551-property" >}}) — property variant.
- [TS2307: Cannot find module]({{< relref "/languages/typescript/ts2307-cannot-find-module" >}}) — module not found.
