---
title: "[Solution] TypeScript Object Possibly Undefined — Null Check Required Fix"
description: "Fix TypeScript 'Object is possibly undefined' errors. Add null checks, use optional chaining, and handle undefined values properly."
languages: ["typescript"]
severities: ["error"]
error-types: ["type-error"]
weight: 5
---

# TypeScript: Object is possibly 'undefined'

This error occurs when you access a property or method on a value that TypeScript knows could be `undefined`. It is triggered by `strictNullChecks` and tells you the variable might not have been assigned a value yet.

## Common Causes

- **Uninitialized optional property** — accessing a property on an optional type without checking
- **Array access without bounds check** — `arr[index]` returns `T | undefined`
- **Map or object lookup** — `obj[key]` may return `undefined` if the key doesn't exist
- **Async data not yet loaded** — variable is `undefined` until a promise resolves

## How to Fix

```typescript
interface User {
  name: string;
  address?: {
    street?: string;
    city: string;
  };
}

// Cause 1: Accessing optional property without check
function getCity(user: User): string {
  return user.address.city;  // TS2532: Object is possibly 'undefined'
}

// Fix: optional chaining
function getCity(user: User): string {
  return user.address?.city ?? "Unknown";
}

// Cause 2: Array access
const items = [1, 2, 3];
const first = items[10];  // type is number | undefined

// Fix: check before use
if (items[10] !== undefined) {
  console.log(items[10]);
}

// Cause 3: Promise result not awaited
let user: User | undefined;
fetchUser().then(u => user = u);
console.log(user.name);  // user is undefined here

// Fix: await or check
const user = await fetchUser();
console.log(user.name);
```

## Examples

```typescript
// Deeply nested optional access
interface Company {
  ceo?: {
    name?: string;
  };
}

function getCEOName(company: Company): string {
  return company.ceo.name;  // TS2532
}

// Fix with optional chaining
function getCEOName(company: Company): string {
  return company.ceo?.name ?? "Unknown CEO";
}

// Map lookup
const map = new Map<string, number>();
const value = map.get("key");  // number | undefined
console.log(value + 1);  // TS2532

// Fix
const value = map.get("key") ?? 0;
console.log(value + 1);
```

## Related Errors

- [TS2339: Property does not exist on type]({{< relref "/languages/typescript/ts2339" >}}) — accessing a property that doesn't exist at all
- [TS2531: Object is possibly null]({{< relref "/languages/typescript/ts2531" >}}) — similar but for `null`
- [TS18046: Variable is of type unknown]({{< relref "/languages/typescript/ts18046" >}}) — accessing properties on `unknown`
