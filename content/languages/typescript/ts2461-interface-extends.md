---
title: "[Solution] TypeScript TS2461 — Interface 'X' incorrectly extends 'Y'"
description: "Fix TypeScript TS2461: Interface 'X' incorrectly extends 'Y'. Fix interface inheritance conflicts."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2461", "interface", "extends", "incorrectly-extends", "inheritance"]
weight: 5
---

# TS2461 — Interface 'X' incorrectly extends 'Y'

TS2461 occurs when an interface that extends another interface has incompatible types for inherited properties.

## Common Causes

```typescript
// Cause 1: Conflicting property types
interface Animal {
  name: string;
  age: number;
}

interface Robot extends Animal {
  age: string; // TS2461: 'string' is not assignable to 'number'
}

// Cause 2: Incompatible method signatures
interface Logger {
  log(msg: string): void;
}

interface StrictLogger extends Logger {
  log(msg: number): void; // TS2461: incompatible signature
}

// Cause 3: Incompatible with built-in type
interface MyArray extends Array<string> {
  push(n: number): void; // TS2461
}
```

## How to Fix

### Fix 1: Use compatible types

```typescript
interface Robot extends Animal {
  age: number; // same type as Animal.age
  model: string;
}
```

### Fix 2: Use same method signature

```typescript
interface StrictLogger extends Logger {
  log(msg: string): void; // compatible
}
```

### Fix 3: Use composition instead

```typescript
interface Logger {
  log(msg: string): void;
}

interface StrictLogger {
  log(msg: string, strict: boolean): void;
}
```

## Related Errors

- [TS2320: Interface cannot extend]({{< relref "/languages/typescript/ts2320-interface-declaration" >}}) — interface extension failure.
- [TS2420: Class incorrectly implements]({{< relref "/languages/typescript/ts2420-correctly-implemented" >}}) — class interface mismatch.
- [TS2322: Type not assignable]({{< relref "/languages/typescript/ts2322-type" >}}) — general type mismatch.
