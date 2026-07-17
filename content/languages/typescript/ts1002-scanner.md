---
title: "[Solution] TypeScript TS1002 — Unterminated string literal"
description: "Fix TypeScript TS1002: Unterminated string literal. Resolve unclosed string syntax errors."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["ts1002", "string", "unterminated", "syntax-error", "scanner"]
weight: 5
---

# TS1002 — Unterminated string literal

TS1002 occurs when a string literal is not properly closed with a matching quote. This prevents TypeScript from parsing the rest of the file.

## Common Causes

```typescript
// Cause 1: Missing closing quote
const msg = "Hello, world;  // TS1002

// Cause 2: Unescaped quote inside string
const quote = "She said "hello"";  // TS1002

// Cause 3: String spanning lines without template literal
const multi = "Line 1
Line 2";  // TS1002
```

## How to Fix

### Fix 1: Add closing quote

```typescript
const msg = "Hello, world";
```

### Fix 2: Escape inner quotes

```typescript
const quote = "She said \"hello\"";
// or use single quotes
const quote = 'She said "hello"';
```

### Fix 3: Use template literals for multiline

```typescript
const multi = `Line 1
Line 2`;
```

## Related Errors

- [TS1361: Unterminated template literal]({{< relref "/languages/typescript/ts1361-unclosed-template" >}}) — template literal variant.
- [TS1005: ';' expected]({{< relref "/languages/typescript/ts1005-semicolon" >}}) — semicolon issues.
- [TS1128: Declaration or statement expected]({{< relref "/languages/typescript/ts1128-declaration" >}}) — broader syntax error.
