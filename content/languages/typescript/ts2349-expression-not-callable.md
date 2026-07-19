---
title: "[Solution] TypeScript TS2349 — This expression is not callable"
description: "TS2349 occurs when trying to call a value that is not a function."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Ensure the value is a function before calling it."
---

The error "[Solution] TypeScript TS2349 — This expression is not callable" occurs when ts2349 occurs when trying to call a value that is not a function.

## Solution

Ensure the value is a function before calling it.

## Code Example

```typescript
const obj = { method: 'hello' };
obj.method(); // TS2349 - string is not callable
```
