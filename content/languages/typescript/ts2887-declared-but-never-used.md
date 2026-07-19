---
title: "[Solution] TypeScript TS2887 — 'X' is declared but never used"
description: "TS2887 occurs with noUnusedLocals when a declaration is unused."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use the declaration or remove it."
---

The error "[Solution] TypeScript TS2887 — 'X' is declared but never used" occurs when ts2887 occurs with nounusedlocals when a declaration is unused.

## Solution

Use the declaration or remove it.

## Code Example

```typescript
function unused() {} // TS2887
function _unusedWithUnderscore() {} // OK if configured
```
