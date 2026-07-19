---
title: "[Solution] TypeScript TS2322 — Type 'Promise' not assignable to value"
description: "TS2322 occurs when assigning a Promise where a value is expected."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Await the Promise before assignment."
---

The error "[Solution] TypeScript TS2322 — Type 'Promise' not assignable to value" occurs when ts2322 occurs when assigning a promise where a value is expected.

## Solution

Await the Promise before assignment.

## Code Example

```typescript
async function getData() { return 'data'; }
const data: string = getData(); // TS2322
const data: string = await getData(); // Fix
```
