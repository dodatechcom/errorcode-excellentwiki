---
title: "[Solution] TypeScript TS2307 — Cannot find module (wrong extension)"
description: "TS2307 occurs when importing a file with incorrect extension."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use the correct file extension or configure moduleResolution."
---

The error "[Solution] TypeScript TS2307 — Cannot find module (wrong extension)" occurs when ts2307 occurs when importing a file with incorrect extension.

## Solution

Use the correct file extension or configure moduleResolution.

## Code Example

```typescript
import { calc } from './math.ts'; // Try without .ts
import { calc } from './math';
```
