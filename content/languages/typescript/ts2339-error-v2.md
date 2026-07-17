---
title: "[Solution] TypeScript TS2339 v2 — Property Does Not Exist on Type Fix"
description: "Fix TypeScript TS2339 when accessing properties not defined on a type. Handle union types, optional chaining, and type narrowing."
languages: ["typescript"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# TS2339 — Property Does Not Exist on Type (v2)

This variant of TS2339 covers situations where property access fails on union types, generic constraints, or when working with third-party library types that lack proper typings.

## What This Error Means

Common error messages:

- `TS2339: Property 'name' does not exist on type 'User | null'`
- `TS2339: Property 'data' does not exist on type 'unknown'`
- `TS2339: Property 'map' does not exist on type 'T'`
- `TS2339: Property 'toISOString' does not exist on type 'string | Date'`

TypeScript prevents accessing properties that the current type annotation doesn't include. This often happens after narrowing, with union types, or when the type is inferred as `unknown`.

## Common Causes

```typescript
// Cause 1: Property on nullable type
interface User { name: string; email: string; }
function greet(user: User | null) {
  console.log(user.name); // TS2339
}

// Cause 2: Accessing property on unknown
async function fetchData() {
  const res = await fetch('/api');
  const data = await res.json(); // returns 'unknown'
  console.log(data.users); // TS2339
}

// Cause 3: Generic type without constraint
function process<T>(value: T) {
  return value.toString(); // TS2339
}

// Cause 4: Mismatched property name
interface User { username: string; }
const user: User = { username: 'alice' };
console.log(user.userName); // TS2339 — typo

// Cause 5: Index signature mismatch
interface Dict { [key: string]: string; }
const d: Dict = {};
const v: number = d.count; // TS2339: number not assignable to string
```

## How to Fix

### Fix 1: Narrow with optional chaining or null check

```typescript
function greet(user: User | null) {
  if (user) {
    console.log(user.name); // safe
  }
  // or
  console.log(user?.name);
}
```

### Fix 2: Type the fetch response

```typescript
interface ApiResponse {
  users: User[];
}

const res = await fetch('/api');
const data: ApiResponse = await res.json();
console.log(data.users); // safe
```

### Fix 3: Add generic constraint

```typescript
function process<T extends { toString(): string }>(value: T) {
  return value.toString(); // safe
}
```

### Fix 4: Use `in` operator for type narrowing

```typescript
function handleEvent(event: MouseEvent | KeyboardEvent) {
  if ('clientX' in event) {
    console.log(event.clientX); // MouseEvent
  } else {
    console.log(event.key); // KeyboardEvent
  }
}
```

### Fix 5: Use type guards

```typescript
function isUser(obj: unknown): obj is User {
  return typeof obj === 'object' && obj !== null && 'name' in obj && 'email' in obj;
}

const data: unknown = await res.json();
if (isUser(data)) {
  console.log(data.name); // safe
}
```

## Examples

```typescript
interface ApiResponse {
  data: { users: User[] };
  meta: { total: number };
}

const res: ApiResponse | null = await fetchData();
console.log(res.data); // TS2339: Property 'data' does not exist on type 'ApiResponse | null'
```

```typescript
// Fix: narrow before access
if (res) {
  console.log(res.data.users);
}
```

## Related Errors

- [TS2339]({{< relref "/languages/typescript/ts2339" >}}) — basic property not found
- [TS2531]({{< relref "/languages/typescript/ts2531" >}}) — object is possibly null
- [TS2532]({{< relref "/languages/typescript/ts2532" >}}) — object is possibly undefined
