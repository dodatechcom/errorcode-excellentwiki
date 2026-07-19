---
title: "[Solution] TypeScript TS2304 — Cannot find name (const)"
description: "TS2304 occurs when using a const value that hasn't been declared."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Declare the const before using it."
---

The error "[Solution] TypeScript TS2304 — Cannot find name (const)" occurs when ts2304 occurs when using a const value that hasn't been declared.

## Solution

Declare the const before using it.

## Code Example

```typescript
console.log(API_URL); // TS2304
const API_URL = 'https://api.example.com';
```
