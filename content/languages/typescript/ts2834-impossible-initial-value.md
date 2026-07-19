---
title: "[Solution] TypeScript TS2834 — Impossible initial value"
description: "TS2834 occurs when an initial value doesn't match the type constraints."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Provide a valid initial value matching the type."
---

The error "[Solution] TypeScript TS2834 — Impossible initial value" occurs when ts2834 occurs when an initial value doesn't match the type constraints.

## Solution

Provide a valid initial value matching the type.

## Code Example

```typescript
const arr: [string, number] = [1, 'hello']; // TS2834 - wrong order
```
