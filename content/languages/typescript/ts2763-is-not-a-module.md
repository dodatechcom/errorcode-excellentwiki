---
title: "[Solution] TypeScript TS2763 — 'X' is not a module"
description: "TS2763 occurs when trying to import from something that isn't a module."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use the correct import syntax or ensure the file exports."
---

The error "[Solution] TypeScript TS2763 — 'X' is not a module" occurs when ts2763 occurs when trying to import from something that isn't a module.

## Solution

Use the correct import syntax or ensure the file exports.

## Code Example

```typescript
// config.ts (plain object, not a module)
const config = {};
// app.ts
import config from './config'; // TS2763
```
