---
title: "[Solution] TypeScript TS2322 — Type enum mismatch"
description: "TS2322 occurs when assigning a value from a different enum type."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use the correct enum type for the assignment."
---

The error "[Solution] TypeScript TS2322 — Type enum mismatch" occurs when ts2322 occurs when assigning a value from a different enum type.

## Solution

Use the correct enum type for the assignment.

## Code Example

```typescript
enum Color { Red, Green, Blue }
enum Size { Small, Medium, Large }
let c: Color = Color.Red;
let s: Size = c; // TS2322
```
