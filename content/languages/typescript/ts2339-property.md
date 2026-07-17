---
title: "[Solution] TypeScript TS2339 — Property 'X' does not exist on type 'Y'"
description: "Fix TypeScript TS2339: Property 'X' does not exist on type 'Y'. Resolve property access errors in TypeScript."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2339", "property-access", "type-error", "missing-property"]
weight: 5
---

# TS2339 — Property 'X' does not exist on type 'Y'

TS2339 occurs when you try to access a property on a type that does not define it. TypeScript's type system enforces that you can only access properties that exist on the declared type.

## Common Causes

```typescript
// Cause 1: Accessing non-existent property
interface User {
  name: string;
  age: number;
}
const user: User = { name: "Alice", age: 30 };
console.log(user.email); // TS2339

// Cause 2: Wrong type annotation
const data: string = "hello";
data.length; // OK
data.toFixed(2); // TS2339: string has no toFixed

// Cause 3: Using API response without type definition
const response = fetch("/api/user");
const data = await response.json();
console.log(data.user.name); // TS2339: 'user' does not exist
```

## How to Fix

### Fix 1: Add missing property to interface

```typescript
interface User {
  name: string;
  age: number;
  email: string;
}
```

### Fix 2: Use optional chaining

```typescript
console.log(user?.email);
```

### Fix 3: Type the API response

```typescript
interface ApiResponse {
  user: { name: string; age: number };
}
const data: ApiResponse = await response.json();
console.log(data.user.name);
```

### Fix 4: Use type assertion or index signature

```typescript
interface StringMap {
  [key: string]: string;
}
const map: StringMap = { name: "Alice" };
console.log(map["name"]);
```

## Related Errors

- [TS2339: Property is type-only import]({{< relref "/languages/typescript/ts2339-property-access" >}}) — type-only import access.
- [TS2551: Property does not exist - did you mean]({{< relref "/languages/typescript/ts2551-property" >}}) — typo suggestions.
- [TS2741: Property is missing in type]({{< relref "/languages/typescript/ts2741-property" >}}) — missing required property.
