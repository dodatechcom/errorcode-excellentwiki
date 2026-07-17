---
title: "[Solution] TypeScript TS2694 — Namespace 'X' has no exported member 'Y'"
description: "Fix TypeScript TS2694: Namespace 'X' has no exported member 'Y'. Access only exported namespace members."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2694", "namespace", "exported-member", "access", "not-exported"]
weight: 5
---

# TS2694 — Namespace 'X' has no exported member 'Y'

TS2694 occurs when you access a member of a namespace that does not export that name. Only exported members are accessible from outside the namespace.

## Common Causes

```typescript
// Cause 1: Accessing non-exported member
namespace MathUtils {
  const PI = 3.14; // not exported
  export function square(x: number) { return x * x; }
}
console.log(MathUtils.PI); // TS2694

// Cause 2: Typo in member name
namespace Colors {
  export const Red = "red";
}
console.log(Colors.Read); // TS2694: typo

// Cause 3: Wrong namespace
namespace A {
  export const value = 1;
}
namespace B {
  export const value = 2;
}
console.log(A.value); // OK
console.log(B.value); // OK
```

## How to Fix

### Fix 1: Export the member

```typescript
namespace MathUtils {
  export const PI = 3.14; // add export
  export function square(x: number) { return x * x; }
}
```

### Fix 2: Fix the member name

```typescript
console.log(Colors.Red);
```

### Fix 3: Use import in namespace

```typescript
namespace MyNamespace {
  import Utils = OtherNamespace.Utils;
  export function use() { Utils.process(); }
}
```

## Related Errors

- [TS2305: Module has no exported member]({{< relref "/languages/typescript/ts2305-module-has-no-exported" >}}) — module variant.
- [TS2304: Cannot find name]({{< relref "/languages/typescript/ts2304-cannot-find" >}}) — undefined identifier.
- [TS2503: Cannot find namespace]({{< relref "/languages/typescript/ts2503-cannot-find-namespace" >}}) — namespace not found.
