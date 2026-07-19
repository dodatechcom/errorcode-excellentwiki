---
title: "[Solution] TypeScript TS2877 — Accessing UMD module with ES import"
description: "TS2877 occurs when using ES import syntax on UMD modules."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use require() or global variable."
---

The error "[Solution] TypeScript TS2877 — Accessing UMD module with ES import" occurs when ts2877 occurs when using es import syntax on umd modules.

## Solution

Use require() or global variable.

## Code Example

```typescript
import $ from 'jquery'; // TS2877
const $ = require('jquery'); // Fix
```
