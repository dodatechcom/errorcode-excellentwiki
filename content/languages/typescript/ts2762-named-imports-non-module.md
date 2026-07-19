---
title: "[Solution] TypeScript TS2762 — Named imports from non-module"
description: "TS2762 occurs when importing named exports from a non-module file."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Ensure the file uses export syntax."
---

The error "[Solution] TypeScript TS2762 — Named imports from non-module" occurs when ts2762 occurs when importing named exports from a non-module file.

## Solution

Ensure the file uses export syntax.

## Code Example

```typescript
// config.js
const config = {};
export default config; // Add export
// app.ts
import config from './config';
```
