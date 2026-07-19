---
title: "[Solution] TypeScript TS2872 — 'X' can only be defaulted in parameter position"
description: "TS2872 occurs when using default value in wrong position."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use default values only in function parameters."
---

The error "[Solution] TypeScript TS2872 — 'X' can only be defaulted in parameter position" occurs when ts2872 occurs when using default value in wrong position.

## Solution

Use default values only in function parameters.

## Code Example

```typescript
type Options = { timeout?: number };
const default: Options = { timeout: 1000 }; // TS2872
```
