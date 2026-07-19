---
title: "[Solution] TypeScript TS2763 — 'X' is not a module (object)"
description: "TS2763 occurs when importing from a plain object file."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Export the object as a module."
---

The error "[Solution] TypeScript TS2763 — 'X' is not a module (object)" occurs when ts2763 occurs when importing from a plain object file.

## Solution

Export the object as a module.

## Code Example

```typescript
// utils.js
const helper = {};
module.exports = helper; // CommonJS
// app.ts
import helper from './utils'; // Use default import
```
