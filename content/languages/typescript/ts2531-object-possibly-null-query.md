---
title: "[Solution] TypeScript TS2531 — Object is possibly null (querySelector)"
description: "TS2531 occurs when querySelector may return null."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use optional chaining or a null check."
---

The error "[Solution] TypeScript TS2531 — Object is possibly null (querySelector)" occurs when ts2531 occurs when queryselector may return null.

## Solution

Use optional chaining or a null check.

## Code Example

```typescript
const btn = document.querySelector('.btn');
btn.addEventListener('click', handler); // TS2531
```
