---
title: "[Solution] TypeScript TS2551 — Property 'X' does not exist - did you mean 'Y'?"
description: "Fix TypeScript TS2551: Property 'X' does not exist - did you mean 'Y'? Fix typos and use suggested property names."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2551", "property-access", "typo", "did-you-mean", "suggestion"]
weight: 5
---

# TS2551 — Property 'X' does not exist - did you mean 'Y'?

TS2551 is an enhanced version of TS2339 where TypeScript detects a property access that looks like a typo and suggests a similar property name that does exist on the type.

## Common Causes

```typescript
// Cause 1: Typo in property name
interface User {
  firstName: string;
  lastName: string;
}
const user: User = { firstName: "Alice", lastName: "Smith" };
console.log(user.firsName); // TS2551: Did you mean 'firstName'?

// Cause 2: Wrong casing
const el = document.getElementById("myId");
el.innerHtml = "hello"; // TS2551: Did you mean 'innerHTML'?

// Cause 3: Missing import from destructured object
const { namee } = { name: "Alice" }; // TS2551: Did you mean 'name'?
```

## How to Fix

### Fix 1: Use the suggested property name

```typescript
console.log(user.firstName); // correct spelling
```

### Fix 2: Use the IDE suggestion

TypeScript language servers show quick fixes — accept the suggestion to rename automatically.

### Fix 3: Check the type definition

```typescript
// If the property should exist, add it to the interface
interface User {
  firstName: string;
  lastName: string;
  email?: string; // add missing property
}
```

## Related Errors

- [TS2339: Property does not exist on type]({{< relref "/languages/typescript/ts2339-property" >}}) — without typo suggestions.
- [TS2552: Cannot find name - did you mean]({{< relref "/languages/typescript/ts2552-X-cannot-find-name" >}}) — similar for identifiers.
- [TS2304: Cannot find name]({{< relref "/languages/typescript/ts2304-cannot-find" >}}) — no suggestions available.
