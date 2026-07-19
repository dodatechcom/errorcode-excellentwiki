---
title: "[Solution] TypeScript TS2531 — Object possibly null (DOM element)"
description: "TS2531 occurs when DOM methods return nullable types."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Check for null before using DOM elements."
---

The error "[Solution] TypeScript TS2531 — Object possibly null (DOM element)" occurs when ts2531 occurs when dom methods return nullable types.

## Solution

Check for null before using DOM elements.

## Code Example

```typescript
const input = document.querySelector('input');
console.log(input.value); // TS2531
if (input) console.log(input.value); // Fix
```
