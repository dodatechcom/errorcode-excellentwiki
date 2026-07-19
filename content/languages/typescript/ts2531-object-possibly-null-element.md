---
title: "[Solution] TypeScript TS2531 — Object is possibly null (element)"
description: "TS2531 occurs when getElementById may return null."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Check for null before using the element."
---

The error "[Solution] TypeScript TS2531 — Object is possibly null (element)" occurs when ts2531 occurs when getelementbyid may return null.

## Solution

Check for null before using the element.

## Code Example

```typescript
const el = document.getElementById('app');
el.innerHTML = 'Hello'; // TS2531
```
