---
title: "[Solution] TypeScript TS2412 — Property accessors can only be used with qualified names"
description: "Fix TypeScript TS2412: Property accessors can only be used with qualified names. Fix property accessor syntax."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2412", "property-accessor", "qualified-name", "syntax"]
weight: 5
---

# TS2412 — Property accessors can only be used with qualified names

TS2412 occurs when you use a property accessor on an expression that is not a qualified name (i.e., not a namespace or module reference).

## Common Causes

```typescript
// Cause 1: Wrong property accessor syntax
type Foo = { bar: string };
const foo: Foo = { bar: "hello" };
Foo.bar; // TS2412: cannot use accessor on type

// Cause 2: Accessing static member incorrectly
class MyClass {
  static value = 42;
}
MyClass.value; // OK
```

## How to Fix

### Fix 1: Use instance access

```typescript
const foo: Foo = { bar: "hello" };
foo.bar; // OK
```

### Fix 2: Use correct static access

```typescript
MyClass.value; // correct for static
```

### Fix 3: Use namespace access correctly

```typescript
namespace MyNamespace {
  export const value = 42;
}
MyNamespace.value; // OK
```

## Related Errors

- [TS2339: Property does not exist]({{< relref "/languages/typescript/ts2339-property" >}}) — property access errors.
- [TS2571: Object is of type 'unknown']({{< relref "/languages/typescript/ts2571-unknown" >}}) — unknown type access.
- [TS2304: Cannot find name]({{< relref "/languages/typescript/ts2304-cannot-find" >}}) — undefined identifier.
