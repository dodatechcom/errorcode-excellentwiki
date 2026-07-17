---
title: "[Solution] TypeScript TS1361 — Unterminated template literal"
description: "Fix TypeScript TS1361: Unterminated template literal. Fix unclosed template literal syntax errors."
languages: ["typescript"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# TS1361 — Unterminated template literal

TS1361 occurs when a template literal (backtick string) is not properly closed with a matching backtick. This is a syntax error that prevents TypeScript from parsing the file.

## Common Causes

```typescript
// Cause 1: Missing closing backtick
const msg = `Hello, world;  // TS1361

// Cause 2: Missing closing backtick after expression
const name = "Alice";
const greeting = `Hello, ${name};  // TS1361

// Cause 3: Unclosed multiline template
const html = `
  <div>
    <h1>Title</h1>
  </div>  // TS1361 if closing backtick missing
`;
```

## How to Fix

### Fix 1: Add closing backtick

```typescript
const msg = `Hello, world`;
```

### Fix 2: Ensure expression blocks are complete

```typescript
const greeting = `Hello, ${name}`;
```

### Fix 3: Check multiline templates

```typescript
const html = `
  <div>
    <h1>Title</h1>
  </div>
`;
```

## Related Errors

- [TS1002: Unterminated string literal]({{< relref "/languages/typescript/ts1002-scanner" >}}) — regular string variant.
- [TS1005: ';' expected]({{< relref "/languages/typescript/ts1005-semicolon" >}}) — semicolon issues.
- [TS1128: Declaration or statement expected]({{< relref "/languages/typescript/ts1128-declaration" >}}) — broader syntax error.
