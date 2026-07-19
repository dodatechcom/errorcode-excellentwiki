---
title: "[Solution] TypeScript TS2531 — Object is possibly null (array find)"
description: "TS2531 occurs when array find() may return null/undefined."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Check the result before using it."
---

The error "[Solution] TypeScript TS2531 — Object is possibly null (array find)" occurs when ts2531 occurs when array find() may return null/undefined.

## Solution

Check the result before using it.

## Code Example

```typescript
const users = [{ id: 1, name: 'Alice' }];
const user = users.find(u => u.id === 1);
console.log(user.name); // TS2531
```
