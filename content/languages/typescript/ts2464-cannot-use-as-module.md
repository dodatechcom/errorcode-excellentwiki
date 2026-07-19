---
title: "[Solution] TypeScript TS2464 — 'X' cannot be used as a module"
description: "TS2464 occurs when using a file that doesn't export anything as a module."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Add exports to the module or use import differently."
---

The error "[Solution] TypeScript TS2464 — 'X' cannot be used as a module" occurs when ts2464 occurs when using a file that doesn't export anything as a module.

## Solution

Add exports to the module or use import differently.

## Code Example

```typescript
// utils.ts (no exports)
const helper = 'hello';
// app.ts
import * as utils from './utils'; // TS2464
```
