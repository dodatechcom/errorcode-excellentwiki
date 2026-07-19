---
title: "[Solution] TypeScript TS2349 — This expression is not callable (Promise)"
description: "TS2349 occurs when calling a Promise as a function."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use await or .then() on the Promise."
---

The error "[Solution] TypeScript TS2349 — This expression is not callable (Promise)" occurs when ts2349 occurs when calling a promise as a function.

## Solution

Use await or .then() on the Promise.

## Code Example

```typescript
const getData = fetch('/api');
const data = getData(); // TS2349
const data = await getData; // Fix
```
