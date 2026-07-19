---
title: "[Solution] TypeScript TS2335 — 'abstract' modifier can only appear on class declarations"
description: "TS2335 occurs when 'abstract' is used on something other than a class."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use 'abstract' only on class declarations."
---

The error "[Solution] TypeScript TS2335 — 'abstract' modifier can only appear on class declarations" occurs when ts2335 occurs when 'abstract' is used on something other than a class.

## Solution

Use 'abstract' only on class declarations.

## Code Example

```typescript
abstract function process(); // TS2335
abstract class Processor {
  abstract process(): void;
} // Fix
```
