---
title: "[Solution] TypeScript TS2300 — Duplicate identifier (variable)"
description: "TS2300 occurs when the same variable name is declared twice in the same scope."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Remove one of the duplicate declarations."
---

The error "[Solution] TypeScript TS2300 — Duplicate identifier (variable)" occurs when ts2300 occurs when the same variable name is declared twice in the same scope.

## Solution

Remove one of the duplicate declarations.

## Code Example

```typescript
let x = 10;
let x = 20; // TS2300 - duplicate identifier
```
