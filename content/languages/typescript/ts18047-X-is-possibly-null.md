---
title: "[Solution] TypeScript TS18047 — X is possibly 'null'"
description: "Fix TypeScript TS18047: X is possibly 'null'. Handle null values with type guards."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS18047 — 'X' is possibly 'null'

TS18047 occurs when you access a property or call a method on a variable that TypeScript knows might be `null`.

## Common Causes

```typescript
// Cause 1: Nullable variable
let name: string | null = getNullableName();
console.log(name.length); // TS18047

// Cause 2: DOM element might be null
const el = document.getElementById("myId");
el.innerHTML = "hello"; // TS18047

// Cause 3: Function returning null
function find(id: number): User | null {
  return db.users.find(u => u.id === id) ?? null;
}
const user = find(1);
console.log(user.name); // TS18047
```

## How to Fix

### Fix 1: Add null check

```typescript
if (name !== null) {
  console.log(name.length);
}
```

### Fix 2: Use optional chaining

```typescript
console.log(name?.length);
```

### Fix 3: Use non-null assertion

```typescript
console.log(name!.length);
```

### Fix 4: Default value

```typescript
console.log((name ?? "").length);
```

## Related Errors

- [TS18048: X is possibly 'undefined']({{< relref "/languages/typescript/ts18048-X-is-possibly-undefined" >}}) — undefined variant.
- [TS2531: Object is possibly 'null']({{< relref "/languages/typescript/ts2531-object" >}}) — property access variant.
- [TS2532: Object is possibly 'undefined']({{< relref "/languages/typescript/ts2532-object" >}}) — undefined variant.
