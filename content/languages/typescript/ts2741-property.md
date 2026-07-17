---
title: "[Solution] TypeScript TS2741 — Property 'X' is missing in type 'Y'"
description: "Fix TypeScript TS2741: Property 'X' is missing in type 'Y'. Add missing required properties."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2741 — Property 'X' is missing in type 'Y'

TS2741 occurs when you assign an object to a type that expects properties not present in the source object. This is a specific variant of type assignability focused on missing properties.

## Common Causes

```typescript
// Cause 1: Missing required property
interface User {
  name: string;
  age: number;
  email: string;
}

const user: User = { name: "Alice", age: 30 }; // TS2741: 'email' is missing

// Cause 2: Partial return value
function getUser(): User {
  return { name: "Alice", age: 30 }; // TS2741: 'email' is missing
}

// Cause 3: Object literal missing properties
const config: { host: string; port: number } = { host: "localhost" }; // TS2741
```

## How to Fix

### Fix 1: Add the missing property

```typescript
const user: User = { name: "Alice", age: 30, email: "alice@example.com" };
```

### Fix 2: Make the property optional in the interface

```typescript
interface User {
  name: string;
  age: number;
  email?: string; // optional
}
```

### Fix 3: Use Partial for flexible types

```typescript
const user: Partial<User> = { name: "Alice" }; // OK
```

## Related Errors

- [TS2322: Type not assignable]({{< relref "/languages/typescript/ts2322-type" >}}) — general assignability.
- [TS2420: Class incorrectly implements]({{< relref "/languages/typescript/ts2420-correctly-implemented" >}}) — class interface mismatch.
- [TS2339: Property does not exist]({{< relref "/languages/typescript/ts2339-property" >}}) — extra properties.
