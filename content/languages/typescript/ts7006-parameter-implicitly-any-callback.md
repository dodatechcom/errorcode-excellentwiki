---
title: "[Solution] TypeScript TS7006 — Parameter implicitly has 'any' type (callback)"
description: "TS7006 occurs when a callback parameter lacks a type annotation."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Add type annotations to all callback parameters."
---

The error "[Solution] TypeScript TS7006 — Parameter implicitly has 'any' type (callback)" occurs when ts7006 occurs when a callback parameter lacks a type annotation.

## Solution

Add type annotations to all callback parameters.

## Code Example

```typescript
arr.forEach((item) => { // TS7006
  console.log(item.name);
});
// Fix:
arr.forEach((item: User) => { ... });
```
