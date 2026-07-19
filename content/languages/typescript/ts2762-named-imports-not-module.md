---
title: "[Solution] TypeScript TS2762 — Named imports from module only allowed on module"
description: "TS2762 occurs when trying to use named imports from a non-module file."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Ensure the file has proper exports."
---

The error "[Solution] TypeScript TS2762 — Named imports from module only allowed on module" occurs when ts2762 occurs when trying to use named imports from a non-module file.

## Solution

Ensure the file has proper exports.

## Code Example

```typescript
// utils.js (no exports)
const helper = 'hello';
// app.ts
import { helper } from './utils'; // TS2762
```
