---
title: "[Solution] TypeScript TS2420 — Class incorrectly implements interface"
description: "Fix TypeScript TS2420: Class incorrectly implements interface. Ensure class satisfies interface contract."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts2420", "class", "implements", "interface", "incorrectly-implements"]
weight: 5
---

# TS2420 — Class incorrectly implements interface

TS2420 occurs when a class that `implements` an interface does not provide all required members or provides members with incompatible types.

## Common Causes

```typescript
// Cause 1: Missing required methods
interface Logger {
  log(message: string): void;
  error(message: string): void;
}

class ConsoleLogger implements Logger {
  log(message: string) {
    console.log(message);
  }
  // missing error() — TS2420
}

// Cause 2: Wrong property types
interface Config {
  port: number;
}

class AppConfig implements Config {
  port: string; // TS2420: 'string' is not assignable to 'number'
}
```

## How to Fix

### Fix 1: Implement all required members

```typescript
class ConsoleLogger implements Logger {
  log(message: string) {
    console.log(message);
  }
  error(message: string) {
    console.error(message);
  }
}
```

### Fix 2: Use the correct types

```typescript
class AppConfig implements Config {
  port: number = 3000;
}
```

### Fix 3: Use abstract class for partial implementation

```typescript
abstract class BaseLogger implements Logger {
  abstract log(message: string): void;
  abstract error(message: string): void;
}
```

## Related Errors

- [TS2304: Class is not abstract and does not implement]({{< relref "/languages/typescript/ts2304-cannot-find" >}}) — abstract implementation.
- [TS2717: Non-abstract class does not implement]({{< relref "/languages/typescript/ts2717-non-abstract" >}}) — similar variant.
- [TS2414: Type argument not assignable]({{< relref "/languages/typescript/ts2414-type-argument" >}}) — generic constraint issues.
