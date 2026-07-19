---
title: "[Solution] TypeScript TS7006 — Parameter implicitly 'any' (arrow function)"
description: "TS7006 occurs in arrow functions without type annotations."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Add type annotations to arrow function parameters."
---

The error "[Solution] TypeScript TS7006 — Parameter implicitly 'any' (arrow function)" occurs when ts7006 occurs in arrow functions without type annotations.

## Solution

Add type annotations to arrow function parameters.

## Code Example

```typescript
const multiply = (a, b) => a * b; // TS7006
const multiply = (a: number, b: number) => a * b; // Fix
```
