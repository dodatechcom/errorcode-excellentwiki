---
title: "[Solution] TypeScript TS2345 — Argument type mismatch"
description: "TS2345 occurs when a function argument doesn't match the expected parameter type."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Pass an argument of the correct type."
---

The error "[Solution] TypeScript TS2345 — Argument type mismatch" occurs when ts2345 occurs when a function argument doesn't match the expected parameter type.

## Solution

Pass an argument of the correct type.

## Code Example

```typescript
function greet(name: string) { console.log(name); }
greet(42); // TS2345
```
