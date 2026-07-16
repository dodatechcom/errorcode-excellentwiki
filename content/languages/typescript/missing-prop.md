---
title: "[Solution] TypeScript Missing Property in Type — Structural Type Error Fix"
description: "Fix TypeScript 'Property X is missing in type' errors. Understand structural typing, optional properties, and how to satisfy interface contracts."
languages: ["typescript"]
severities: ["error"]
error-types: ["type-error"]
tags: ["missing-property", "structural-type", "interface", "optional-property", "type-error"]
weight: 5
---

# TypeScript: Property 'X' is missing in type

This error occurs when an object literal is missing a property that the target type requires. TypeScript's structural type system requires that every required property in the target interface is present in the source type.

## Common Causes

- **Missing required interface properties** — not all fields of an interface are provided
- **Function return type mismatch** — a function returns an object missing required fields
- **Spreading incomplete objects** — spreading an object that doesn't have all required properties
- **API response typing** — typing a response more strictly than the actual data

## How to Fix

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  role: "admin" | "user";
}

// Cause 1: Missing properties in object literal
const user: User = {
  id: 1,
  name: "Alice",
  // TS2741: Property 'email' is missing
};

// Fix: provide all required properties
const user: User = {
  id: 1,
  name: "Alice",
  email: "alice@example.com",
  role: "user",
};

// Cause 2: Partial object from a function
function getUser(): User {
  return { id: 1, name: "Alice" };  // TS2741: missing email and role
}

// Fix: ensure function returns all required fields
function getUser(): User {
  return { id: 1, name: "Alice", email: "alice@example.com", role: "user" };
}

// Cause 3: Make properties optional if they aren't always needed
interface User {
  id: number;
  name: string;
  email?: string;  // optional
  role?: "admin" | "user";  // optional
}
```

## Examples

```typescript
interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
}

// Spread incomplete object
const partial = { id: 1, name: "Widget" };
const product: Product = { ...partial, price: 9.99 };  // TS2741: missing description

// Fix: include all fields
const product: Product = { ...partial, price: 9.99, description: "A widget" };

// Array of objects — one is missing a field
const items: Product[] = [
  { id: 1, name: "A", price: 10, description: "desc" },
  { id: 2, name: "B", price: 20 },  // TS2741: missing description
];
```

## Related Errors

- [TS2322: Type not assignable]({{< relref "/languages/typescript/type-assignment" >}}) — broader assignability issues
- [TS2339: Property does not exist on type]({{< relref "/languages/typescript/ts2339" >}}) — accessing extra/wrong properties
- [TS2740: Type missing properties]({{< relref "/languages/typescript/ts2740" >}}) — related variant for class types
