---
title: "[Solution] TypeScript TS2321 — Function type not assignable"
description: "TS2321 occurs when a function type doesn't match the expected signature."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Ensure the function matches the expected signature."
---

The error "[Solution] TypeScript TS2321 — Function type not assignable" occurs when ts2321 occurs when a function type doesn't match the expected signature.

## Solution

Ensure the function matches the expected signature.

## Code Example

```typescript
type Callback = (data: string) => void;
const cb: Callback = (data: number) => {}; // TS2321
```
