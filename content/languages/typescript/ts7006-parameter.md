---
title: "[Solution] TypeScript TS7006 — Parameter 'X' implicitly has 'any' type"
description: "Fix TypeScript TS7006: Parameter 'X' implicitly has 'any' type. Enable explicit typing and disable implicit any."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS7006 — Parameter 'X' implicitly has 'any' type

TS7006 occurs when `noImplicitAny` is enabled and TypeScript cannot infer a parameter's type, defaulting it to `any`. This is a code quality flag — explicit types make code safer and more maintainable.

## Common Causes

```typescript
// Cause 1: Callback without type annotation
[1, 2, 3].map(x => x * 2); // TS7006 if noImplicitAny is on

// Cause 2: Event handler without type
element.addEventListener("click", event => {
  console.log(event.target); // TS7006
});

// Cause 3: Unannotated function parameter
function add(a, b) {
  return a + b; // TS7006 for both a and b
}
```

## How to Fix

### Fix 1: Add explicit type annotations

```typescript
[1, 2, 3].map((x: number) => x * 2);

element.addEventListener("click", (event: MouseEvent) => {
  console.log(event.target);
});

function add(a: number, b: number): number {
  return a + b;
}
```

### Fix 2: Use type inference from context

```typescript
// TypeScript infers 'e' from addEventListener
element.addEventListener("click", (e) => {
  console.log(e.clientX); // OK — 'e' is inferred as MouseEvent
});
```

### Fix 3: Disable noImplicitAny (not recommended)

```json
{
  "compilerOptions": {
    "noImplicitAny": false
  }
}
```

## Related Errors

- [TS2683: Implicitly has type 'any']({{< relref "/languages/typescript/ts2683-implicitly-any" >}}) — `this` context implicit any.
- [TS18046: Variable is of type 'unknown']({{< relref "/languages/typescript/ts18046-unknown" >}}) — unknown type usage.
- [TS7031: Binding element implicitly has 'any' type]({{< relref "/languages/typescript/ts7006-parameter" >}}) — destructuring variant.
