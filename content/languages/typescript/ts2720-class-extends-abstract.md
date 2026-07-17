---
title: "[Solution] TypeScript TS2720 — Class 'X' defines instance member 'Y'"
description: "Fix TypeScript TS2720: Class defines instance member but abstract class expects static. Implement abstract members correctly."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2720 — Class 'X' defines instance member 'Y' but previously required static member

TS2720 occurs when a class extends an abstract class but implements a member with the wrong static/instance modifier.

## Common Causes

```typescript
// Cause 1: Instance vs static mismatch
abstract class Base {
  abstract static create(): Base;
}

class Derived extends Base {
  create(): Base { // TS2720: instance member, expected static
    return new Derived();
  }
}

// Cause 2: Wrong modifier
abstract class Logger {
  abstract log(msg: string): void;
}

class ConsoleLogger extends Logger {
  static log(msg: string) {} // TS2720: static, expected instance
}
```

## How to Fix

### Fix 1: Match the static/instance modifier

```typescript
abstract class Base {
  static create(): Base;
}

class Derived extends Base {
  static create(): Base {
    return new Derived();
  }
}
```

### Fix 2: Use correct instance method

```typescript
class ConsoleLogger extends Logger {
  log(msg: string) {
    console.log(msg);
  }
}
```

## Related Errors

- [TS2717: Non-abstract class does not implement]({{< relref "/languages/typescript/ts2717-non-abstract" >}}) — missing implementation.
- [TS2420: Class incorrectly implements]({{< relref "/languages/typescript/ts2420-correctly-implemented" >}}) — interface mismatch.
- [TS2304: Cannot find name]({{< relref "/languages/typescript/ts2304-cannot-find" >}}) — undefined member.
