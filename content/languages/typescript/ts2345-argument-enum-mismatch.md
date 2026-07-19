---
title: "[Solution] TypeScript TS2345 — Argument enum type mismatch"
description: "TS2345 occurs when passing wrong enum type as argument."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use the correct enum type."
---

The error "[Solution] TypeScript TS2345 — Argument enum type mismatch" occurs when ts2345 occurs when passing wrong enum type as argument.

## Solution

Use the correct enum type.

## Code Example

```typescript
enum Color { Red, Green, Blue }
enum Size { Small, Medium, Large }
function paint(color: Color) {}
paint(Size.Small); // TS2345
```
