---
title: "[Solution] TypeScript TS2551 — Method does not exist (did you mean)"
description: "TS2551 occurs when a method name is close to but not the same as an existing one."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use the suggested method name."
---

The error "[Solution] TypeScript TS2551 — Method does not exist (did you mean)" occurs when ts2551 occurs when a method name is close to but not the same as an existing one.

## Solution

Use the suggested method name.

## Code Example

```typescript
const arr = [1, 2, 3];
arr.forEech(x => console.log(x)); // TS2551 - forEach
```
