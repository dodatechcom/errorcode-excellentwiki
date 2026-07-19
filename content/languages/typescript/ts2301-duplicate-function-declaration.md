---
title: "[Solution] TypeScript TS2301 — Duplicate function declaration"
description: "TS2301 occurs when a function is declared twice."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Remove the duplicate declaration."
---

The error "[Solution] TypeScript TS2301 — Duplicate function declaration" occurs when ts2301 occurs when a function is declared twice.

## Solution

Remove the duplicate declaration.

## Code Example

```typescript
function calculate(x: number): number { return x; }
function calculate(x: number): number { return x * 2; } // TS2301
```
