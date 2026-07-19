---
title: "[Solution] TypeScript TS2540 — Cannot assign to read-only (const)"
description: "TS2540 occurs when trying to reassign a const variable."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use let instead of const for mutable variables."
---

The error "[Solution] TypeScript TS2540 — Cannot assign to read-only (const)" occurs when ts2540 occurs when trying to reassign a const variable.

## Solution

Use let instead of const for mutable variables.

## Code Example

```typescript
const x = 10;
x = 20; // TS2540 - const cannot be reassigned
let x = 10; // Fix - use let
```
