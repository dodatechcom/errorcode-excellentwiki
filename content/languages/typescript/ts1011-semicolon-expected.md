---
title: "[Solution] TypeScript TS1011 — ';' expected"
description: "TS1011 occurs when a semicolon is expected in a declaration."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "syntax-error"]]
severity: "error"
solution: "Add the missing semicolon at the indicated position."
---

The error "[Solution] TypeScript TS1011 — ';' expected" occurs when ts1011 occurs when a semicolon is expected in a declaration.

## Solution

Add the missing semicolon at the indicated position.

## Code Example

```typescript
declare module 'my-lib' {
  export function doSomething(): void
} // TS1011 - missing semicolon
```
