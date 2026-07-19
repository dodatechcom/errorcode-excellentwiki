---
title: "[Solution] TypeScript TS2339 — Property does not exist on Promise"
description: "TS2339 occurs when accessing properties on a Promise instead of its value."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Await the Promise first."
---

The error "[Solution] TypeScript TS2339 — Property does not exist on Promise" occurs when ts2339 occurs when accessing properties on a promise instead of its value.

## Solution

Await the Promise first.

## Code Example

```typescript
const promise = fetch('/api');
console.log(promise.data); // TS2339
const response = await promise;
console.log(response.data); // Fix
```
