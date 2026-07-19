---
title: "[Solution] TypeScript TS2367 — Condition will never be true"
description: "TS2367 occurs when comparing incompatible types."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Fix the comparison logic."
---

The error "[Solution] TypeScript TS2367 — Condition will never be true" occurs when ts2367 occurs when comparing incompatible types.

## Solution

Fix the comparison logic.

## Code Example

```typescript
const x: string = 'hello';
if (x instanceof Number) {} // TS2367 - string is never Number
```
