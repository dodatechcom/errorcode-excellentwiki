---
title: "[Solution] TypeScript TS2717 — Subsequent property declarations must have same type"
description: "TS2717 occurs when a property is declared with a different type in an extending interface."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Ensure the property type matches the base interface."
---

The error "[Solution] TypeScript TS2717 — Subsequent property declarations must have same type" occurs when ts2717 occurs when a property is declared with a different type in an extending interface.

## Solution

Ensure the property type matches the base interface.

## Code Example

```typescript
interface A { value: string; }
interface B extends A { value: number; } // TS2717
```
