---
title: "[Solution] TypeScript TS18048 — X is possibly 'undefined'"
description: "Fix TypeScript TS18048: X is possibly 'undefined'. Handle undefined values with type guards."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts18048", "possibly-undefined", "undefined", "type-guard", "strictNullChecks"]
weight: 5
---

# TS18048 — 'X' is possibly 'undefined'

TS18048 occurs when you access a property or call a method on a variable that TypeScript knows might be `undefined`.

## Common Causes

```typescript
// Cause 1: Variable with undefined union
let name: string | undefined = getName();
console.log(name.length); // TS18048

// Cause 2: Object property that might be undefined
interface Config {
  db?: { host: string };
}
const config: Config = {};
console.log(config.db.host); // TS18048

// Cause 3: Map.get returns undefined
const map = new Map<string, number>();
const val = map.get("key");
val.toFixed(); // TS18048
```

## How to Fix

### Fix 1: Add undefined check

```typescript
if (name !== undefined) {
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
const val = map.get("key") ?? 0;
```

## Related Errors

- [TS18047: X is possibly 'null']({{< relref "/languages/typescript/ts18047-X-is-possibly-null" >}}) — null variant.
- [TS2532: Object is possibly 'undefined']({{< relref "/languages/typescript/ts2532-object" >}}) — property access variant.
- [TS2531: Object is possibly 'null']({{< relref "/languages/typescript/ts2531-object" >}}) — null variant.
