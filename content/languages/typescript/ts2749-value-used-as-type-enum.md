---
title: "[Solution] TypeScript TS2749 — Value used as type (enum)"
description: "TS2749 occurs when using an enum value where a type is expected."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use typeof or the enum as a type."
---

The error "[Solution] TypeScript TS2749 — Value used as type (enum)" occurs when ts2749 occurs when using an enum value where a type is expected.

## Solution

Use typeof or the enum as a type.

## Code Example

```typescript
enum Color { Red, Green, Blue }
const c: Color = Color.Red;
type ColorType = Color; // TS2749 if using value
```
