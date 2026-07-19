---
title: "[Solution] TypeScript TS2367 — Condition will always return false"
description: "TS2367 occurs when a comparison condition can never be true."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Review the condition logic and types."
---

The error "[Solution] TypeScript TS2367 — Condition will always return false" occurs when ts2367 occurs when a comparison condition can never be true.

## Solution

Review the condition logic and types.

## Code Example

```typescript
let x: string = 'hello';
if (x === 42) {} // TS2367 - string never equals number
```
