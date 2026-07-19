---
title: "[Solution] TypeScript TS2551 — Enum member does not exist (did you mean)"
description: "TS2551 occurs when accessing a misspelled enum member."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use the correct enum member name."
---

The error "[Solution] TypeScript TS2551 — Enum member does not exist (did you mean)" occurs when ts2551 occurs when accessing a misspelled enum member.

## Solution

Use the correct enum member name.

## Code Example

```typescript
enum Direction { Up, Down, Left, Right }
const dir = Direction.Upp; // TS2551 - did you mean Up?
```
