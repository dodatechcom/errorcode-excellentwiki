---
title: "[Solution] TypeScript TS1136 — Expected block of statements"
description: "Fix TypeScript TS1136: Expected block of statements. Add braces around statement blocks."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts1136", "block", "statements", "braces", "syntax-error"]
weight: 5
---

# TS1136 — Expected block of statements

TS1136 occurs when TypeScript expects a block of statements (wrapped in `{}`) but finds something else instead. This typically happens with control structures missing their body braces.

## Common Causes

```typescript
// Cause 1: Missing braces after if
if (condition)
  doSomething();  // TS1136 in some parser contexts

// Cause 2: Empty block
if (condition) {
  // TS1136 if body is expected but empty
}

// Cause 3: Wrong syntax for function body
function foo()  // TS1136: expected block
```

## How to Fix

### Fix 1: Always use braces for blocks

```typescript
if (condition) {
  doSomething();
}
```

### Fix 2: Provide function body

```typescript
function foo() {
  return 42;
}
```

### Fix 3: Use empty block explicitly

```typescript
if (condition) {
  // intentionally empty
}
```

## Related Errors

- [TS1005: ';' expected]({{< relref "/languages/typescript/ts1005-semicolon" >}}) — semicolon issues.
- [TS1109: Expression expected]({{< relref "/languages/typescript/ts1109-expression" >}}) — expression expected.
- [TS1128: Declaration or statement expected]({{< relref "/languages/typescript/ts1128-declaration" >}}) — declaration expected.
