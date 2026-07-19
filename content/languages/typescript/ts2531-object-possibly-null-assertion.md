---
title: "[Solution] TypeScript TS2531 — Object is possibly null (use assertion)"
description: "TS2531 occurs when using a possibly null value without checking."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use non-null assertion operator if you're certain the value exists."
---

The error "[Solution] TypeScript TS2531 — Object is possibly null (use assertion)" occurs when ts2531 occurs when using a possibly null value without checking.

## Solution

Use non-null assertion operator if you're certain the value exists.

## Code Example

```typescript
const el = document.getElementById('app')!;
el.innerHTML = 'Hello'; // Using ! assertion
```
