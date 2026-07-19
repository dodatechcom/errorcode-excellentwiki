---
title: "[Solution] TypeScript TS2322 — RegExp match type mismatch"
description: "TS2322 occurs when assigning regex match result to wrong type."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Handle the regex match result correctly."
---

The error "[Solution] TypeScript TS2322 — RegExp match type mismatch" occurs when ts2322 occurs when assigning regex match result to wrong type.

## Solution

Handle the regex match result correctly.

## Code Example

```typescript
const match = 'hello'.match(/(h)(ello)/);
const first: string = match; // TS2322
const first: string = match![1]; // Fix
```
