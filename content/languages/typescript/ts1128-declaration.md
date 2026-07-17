---
title: "[Solution] TypeScript TS1128 — Declaration or statement expected"
description: "Fix TypeScript TS1128: Declaration or statement expected. Resolve syntax errors at the statement level."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS1128 — Declaration or statement expected

TS1128 occurs when TypeScript encounters an unexpected token at a position where a declaration or statement is expected. This is a broad syntax error that can appear in many contexts.

## Common Causes

```typescript
// Cause 1: Stray characters outside functions
const x = 5;
}  // TS1128: stray closing brace

// Cause 2: Extra closing parenthesis
const arr = [1, 2, 3]);  // TS1128

// Cause 3: Invalid top-level expression
5 + 3;  // OK in some contexts, but in type file...

// Cause 4: Missing body after declaration
function foo();  // TS1128 if not in ambient declaration
```

## How to Fix

### Fix 1: Remove stray characters

```typescript
const x = 5;
// no stray braces
```

### Fix 2: Check bracket matching

```typescript
const arr = [1, 2, 3];  // correct brackets
```

### Fix 3: Use declare for ambient declarations

```typescript
declare function foo(): void;  // OK
```

## Related Errors

- [TS1005: ';' expected]({{< relref "/languages/typescript/ts1005-semicolon" >}}) — semicolon expected.
- [TS1109: Expression expected]({{< relref "/languages/typescript/ts1109-expression" >}}) — expression expected.
- [TS1136: Expected block of statements]({{< relref "/languages/typescript/ts1136-block" >}}) — block expected.
