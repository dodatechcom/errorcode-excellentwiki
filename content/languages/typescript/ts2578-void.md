---
title: "[Solution] TypeScript TS2578 — Type 'void' is not assignable"
description: "Fix TypeScript TS2578: Type 'void' is not assignable. Handle void return types correctly."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS2578 — Type 'void' is not assignable

TS2578 occurs when you try to use a `void` return value. `void` means the function does not return a meaningful value, and you cannot assign it to a variable expecting a real value.

## Common Causes

```typescript
// Cause 1: Assigning void to variable
function log(msg: string): void {
  console.log(msg);
}
const result = log("hello"); // TS2578: void is not assignable

// Cause 2: Using void in expression
function cleanup(): void {
  // ...
}
const val = cleanup() + 1; // TS2578

// Cause 3: Array of void
const tasks: void[] = [];
tasks.push(log("task")); // TS2578
```

## How to Fix

### Fix 1: Don't use void return value

```typescript
log("hello"); // just call it, don't capture result
```

### Fix 2: Change return type

```typescript
function log(msg: string): string {
  console.log(msg);
  return msg;
}
const result = log("hello"); // OK
```

### Fix 3: Use void for callbacks only

```typescript
const tasks: (() => void)[] = [];
tasks.push(() => log("task")); // OK — void callback
```

## Related Errors

- [TS2322: Type not assignable]({{< relref "/languages/typescript/ts2322-type" >}}) — general type mismatch.
- [TS2345: Argument not assignable]({{< relref "/languages/typescript/ts2345-argument" >}}) — argument type mismatch.
- [TS2769: No overload matches this call]({{< relref "/languages/typescript/ts2769-no-overload" >}}) — overload issues.
