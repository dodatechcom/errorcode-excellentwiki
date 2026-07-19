---
title: "[Solution] TypeScript TS2877 — Accessing a UMD module with import 'X' is not supported"
description: "TS2877 occurs when using ES import syntax on a UMD module."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use require() or the global variable name."
---

The error "[Solution] TypeScript TS2877 — Accessing a UMD module with import 'X' is not supported" occurs when ts2877 occurs when using es import syntax on a umd module.

## Solution

Use require() or the global variable name.

## Code Example

```typescript
// UMD module
import $ from 'jquery'; // TS2877
const $ = require('jquery'); // Fix, or use global $
```
