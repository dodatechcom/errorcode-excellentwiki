---
title: "[Solution] TypeScript TS2783 — 'X' is defined but never used"
description: "TS2783 occurs with noUnusedLocals when a variable is declared but unused."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use the variable or prefix with underscore."
---

The error "[Solution] TypeScript TS2783 — 'X' is defined but never used" occurs when ts2783 occurs with nounusedlocals when a variable is declared but unused.

## Solution

Use the variable or prefix with underscore.

## Code Example

```typescript
const unusedVar = 10; // TS2783
const _tempVar = 10; // Fix - prefix with underscore
```
