---
title: "[Solution] TypeScript TS2571 — Object is of type 'unknown'"
description: "Fix TypeScript TS2571: Object is of type 'unknown'. Narrow unknown types before use."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2571 — Object is of type 'unknown'

TS2571 occurs when you try to use a value of type `unknown` in a way that requires a more specific type. `unknown` requires explicit narrowing before use.

## Common Causes

```typescript
// Cause 1: Unvalidated API response
async function fetchUser() {
  const res = await fetch("/api/user");
  const data = await res.json(); // data is 'unknown'
  console.log(data.name); // TS2571
}

// Cause 2: Unknown from catch
try {
  throw new Error("fail");
} catch (e) {
  console.log(e.message); // TS2571: e is 'unknown'
}

// Cause 3: Generic without constraint
function process<T>(value: T) {
  value.name; // TS2571 if T has no 'name'
}
```

## How to Fix

### Fix 1: Type guard

```typescript
if (typeof data === "object" && data !== null && "name" in data) {
  console.log((data as { name: string }).name);
}
```

### Fix 2: Type assertion

```typescript
const user = data as { name: string };
console.log(user.name);
```

### Fix 3: Add generic constraint

```typescript
function process<T extends { name: string }>(value: T) {
  console.log(value.name);
}
```

### Fix 4: Use instanceof in catch

```typescript
try {
  throw new Error("fail");
} catch (e) {
  if (e instanceof Error) {
    console.log(e.message);
  }
}
```

## Related Errors

- [TS18046: Variable is of type 'unknown']({{< relref "/languages/typescript/ts18046-unknown" >}}) — variable unknown.
- [TS2531: Object is possibly 'null']({{< relref "/languages/typescript/ts2531-object" >}}) — null access.
- [TS7006: Parameter implicitly has 'any' type]({{< relref "/languages/typescript/ts7006-parameter" >}}) — any type.
