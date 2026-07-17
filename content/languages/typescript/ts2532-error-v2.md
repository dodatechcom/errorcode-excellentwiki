---
title: "[Solution] TypeScript TS2532 v2 — Object Is Possibly Undefined Fix"
description: "Fix TypeScript TS2532 when accessing properties on values that may be undefined. Handle async results, optional properties, and Promise values."
languages: ["typescript"]
error-types: ["compile-error"]
severities: ["error"]
tags: ["ts2532", "undefined", "strict-null", "optional", "async"]
weight: 5
---

# TS2532 — Object Is Possibly Undefined (v2)

This variant of TS2532 covers scenarios involving async results, optional object properties, and Promise unwrapping where values may be `undefined`.

## What This Error Means

Common error messages:

- `TS2532: Object is possibly 'undefined'`
- `TS2532: 'name' is possibly 'undefined'`
- `TS2532: Cannot access 'property' because value is being used before being assigned`

TypeScript enforces that `undefined` is checked before property access. This prevents `TypeError: Cannot read properties of undefined` at runtime.

## Common Causes

```typescript
// Cause 1: Optional property access
interface Config {
  host: string;
  port?: number; // optional
}
const config: Config = { host: 'localhost' };
console.log(config.port.toFixed()); // TS2532

// Cause 2: Array.find returns T | undefined
const users = [{ id: 1, name: 'Alice' }];
const user = users.find(u => u.id === 999);
console.log(user.name); // TS2532

// Cause 3: Record access without guaranteed key
interface Data { [key: string]: string | undefined; }
const data: Data = {};
console.log(data.missing.length); // TS2532

// Cause 4: Async result not checked
async function getUser(): Promise<User | undefined> {
  const res = await fetch('/api/user');
  if (!res.ok) return undefined;
  return res.json();
}
const user = await getUser();
console.log(user.name); // TS2532

// Cause 5: let variable before assignment
let value: string;
console.log(value.length); // TS2532
```

## How to Fix

### Fix 1: Use optional chaining with defaults

```typescript
const port = config.port ?? 3000;
console.log(port);
// or
console.log(config.port ?? 3000);
```

### Fix 2: Filter before accessing

```typescript
const user = users.find(u => u.id === 999);
if (user) {
  console.log(user.name);
}
```

### Fix 3: Use non-null assertion when certain

```typescript
const value: string = initialize(); // guaranteed to be set
console.log(value.length);
```

### Fix 4: Initialize variables immediately

```typescript
let value: string = '';
console.log(value.length); // safe
```

### Fix 5: Use exhaustive checking pattern

```typescript
function assertDefined<T>(val: T | undefined, name: string): asserts val is T {
  if (val === undefined) {
    throw new Error(`${name} is undefined`);
  }
}

const user = await getUser();
assertDefined(user, 'user');
console.log(user.name); // safe after assertion
```

## Examples

```typescript
interface SearchResult {
  matches?: { title: string; score: number }[];
  total?: number;
}

function printResults(result: SearchResult) {
  console.log(result.matches.length); // TS2532
  console.log(result.total.toFixed()); // TS2532
}

// Fix
function printResults(result: SearchResult) {
  if (result.matches) {
    console.log(result.matches.length);
  }
  if (result.total !== undefined) {
    console.log(result.total.toFixed());
  }
}
```

## Related Errors

- [TS2532]({{< relref "/languages/typescript/ts2532" >}}) — basic TS2532
- [TS2531]({{< relref "/languages/typescript/ts2531" >}}) — object is possibly null
- [TS2339]({{< relref "/languages/typescript/ts2339" >}}) — property does not exist
