---
title: "[Solution] TypeScript TS2532 — Object is possibly 'undefined'"
description: "Fix TypeScript TS2532: Object is possibly 'undefined'. Handle undefined values safely in TypeScript."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2532", "undefined", "strictNullChecks", "possibly-undefined"]
weight: 5
---

# TS2532 — Object is possibly 'undefined'

TS2532 occurs when you access a property or call a method on a value that TypeScript knows might be `undefined`. This is enforced when `strictNullChecks` is enabled.

## Common Causes

```typescript
// Cause 1: Array.find can return undefined
const users = [{ name: "Alice" }, { name: "Bob" }];
const found = users.find(u => u.name === "Charlie");
console.log(found.name); // TS2532

// Cause 2: Object property access on possibly undefined
interface Config {
  db?: { host: string };
}
const config: Config = {};
console.log(config.db.host); // TS2532

// Cause 3: Map.get returns undefined
const map = new Map<string, number>();
const val = map.get("key");
val.toFixed(); // TS2532
```

## How to Fix

### Fix 1: Add undefined check

```typescript
const found = users.find(u => u.name === "Charlie");
if (found) {
  console.log(found.name);
}
```

### Fix 2: Use optional chaining

```typescript
console.log(config.db?.host);
```

### Fix 3: Use default value with nullish coalescing

```typescript
const val = map.get("key") ?? 0;
val.toFixed();
```

### Fix 4: Use non-null assertion

```typescript
const found = users.find(u => u.name === "Alice")!;
console.log(found.name);
```

## Related Errors

- [TS2531: Object is possibly 'null']({{< relref "/languages/typescript/ts2531-object" >}}) — null variant.
- [TS18048: X is possibly 'undefined']({{< relref "/languages/typescript/ts18048-X-is-possibly-undefined" >}}) — variable-level check.
- [TS2571: Object is of type 'unknown']({{< relref "/languages/typescript/ts2571-unknown" >}}) — unknown type variant.
