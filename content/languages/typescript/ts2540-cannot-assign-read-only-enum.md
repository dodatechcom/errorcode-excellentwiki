---
title: "[Solution] TypeScript TS2540 — Cannot assign to read-only (enum)"
description: "TS2540 occurs when trying to modify a const enum member."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Enums are read-only. Use a different approach."
---

The error "[Solution] TypeScript TS2540 — Cannot assign to read-only (enum)" occurs when ts2540 occurs when trying to modify a const enum member.

## Solution

Enums are read-only. Use a different approach.

## Code Example

```typescript
const enum Direction { Up, Down }
Direction.Up = 5; // TS2540 - enum members are read-only
```
