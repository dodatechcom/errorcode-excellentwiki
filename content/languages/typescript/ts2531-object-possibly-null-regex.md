---
title: "[Solution] TypeScript TS2531 — Object is possibly null (regex match)"
description: "TS2531 occurs when using regex match result without null check."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Check if the match result is not null."
---

The error "[Solution] TypeScript TS2531 — Object is possibly null (regex match)" occurs when ts2531 occurs when using regex match result without null check.

## Solution

Check if the match result is not null.

## Code Example

```typescript
const match = str.match(/pattern/);
console.log(match[0]); // TS2531
if (match) console.log(match[0]); // Fix
```
