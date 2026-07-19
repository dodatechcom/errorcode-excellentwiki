---
title: "[Solution] TypeScript TS2349 — Expression not callable (Promise return)"
description: "TS2349 occurs when calling a function that returns a Promise."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Await the Promise result."
---

The error "[Solution] TypeScript TS2349 — Expression not callable (Promise return)" occurs when ts2349 occurs when calling a function that returns a promise.

## Solution

Await the Promise result.

## Code Example

```typescript
async function getData() { return { name: 'Alice' }; }
const data = getData();
data.name; // TS2349 - need await
```
