---
title: "[Solution] TypeScript TS2531 — Object is possibly 'null'"
description: "Fix TypeScript TS2531: Object is possibly 'null'. Handle nullable references safely in TypeScript."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2531 — Object is possibly 'null'

TS2531 occurs when you access a property or call a method on a value that TypeScript knows might be `null`. This is enforced when `strictNullChecks` is enabled.

## Common Causes

```typescript
// Cause 1: getElementById can return null
const el = document.getElementById("myId");
el.style.color = "red"; // TS2531: Object is possibly 'null'

// Cause 2: Array.find can return undefined
const arr = [1, 2, 3];
const found = arr.find(x => x > 5);
found.toFixed(); // TS2531: Object is possibly 'undefined'

// Cause 3: Nullable function parameter
function process(el: HTMLElement | null) {
  el.innerHTML = "hello"; // TS2531
}
```

## How to Fix

### Fix 1: Use non-null assertion (when you're sure)

```typescript
const el = document.getElementById("myId")!;
el.style.color = "red";
```

### Fix 2: Use optional chaining

```typescript
el?.style.color = "red";
```

### Fix 3: Add null check

```typescript
const el = document.getElementById("myId");
if (el) {
  el.style.color = "red";
}
```

### Fix 4: Use a guard clause

```typescript
function process(el: HTMLElement | null) {
  if (!el) return;
  el.innerHTML = "hello";
}
```

## Related Errors

- [TS2532: Object is possibly 'undefined']({{< relref "/languages/typescript/ts2532-object" >}}) — undefined variant.
- [TS18047: X is possibly 'null']({{< relref "/languages/typescript/ts18047-X-is-possibly-null" >}}) — variable-level null check.
- [TS18048: X is possibly 'undefined']({{< relref "/languages/typescript/ts18048-X-is-possibly-undefined" >}}) — variable-level undefined check.
