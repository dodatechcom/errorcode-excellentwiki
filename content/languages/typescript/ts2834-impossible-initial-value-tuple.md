---
title: "[Solution] TypeScript TS2834 — Impossible initial value (tuple)"
description: "TS2834 occurs when tuple initialization doesn't match types."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Provide values in the correct order and types."
---

The error "[Solution] TypeScript TS2834 — Impossible initial value (tuple)" occurs when ts2834 occurs when tuple initialization doesn't match types.

## Solution

Provide values in the correct order and types.

## Code Example

```typescript
const tuple: [string, number] = [42, 'hello']; // TS2834
const tuple: [string, number] = ['hello', 42]; // Fix
```
