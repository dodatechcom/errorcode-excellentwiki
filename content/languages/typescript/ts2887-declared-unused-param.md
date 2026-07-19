---
title: "[Solution] TypeScript TS2887 — Parameter declared but never used"
description: "TS2887 occurs when a function parameter is declared but not used."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use the parameter or prefix with underscore."
---

The error "[Solution] TypeScript TS2887 — Parameter declared but never used" occurs when ts2887 occurs when a function parameter is declared but not used.

## Solution

Use the parameter or prefix with underscore.

## Code Example

```typescript
function greet(name: string, age: number) {
  console.log(name); // TS2887 - age unused
}
function greet(name: string, _age: number) {} // Fix
```
