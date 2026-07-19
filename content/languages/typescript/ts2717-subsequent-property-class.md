---
title: "[Solution] TypeScript TS2717 — Subsequent property declaration (class)"
description: "TS2717 occurs when a class property conflicts with parent."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Ensure property types match between parent and child."
---

The error "[Solution] TypeScript TS2717 — Subsequent property declaration (class)" occurs when ts2717 occurs when a class property conflicts with parent.

## Solution

Ensure property types match between parent and child.

## Code Example

```typescript
class Base { value: string = 'hello'; }
class Child extends Base { value: number = 42; } // TS2717
```
