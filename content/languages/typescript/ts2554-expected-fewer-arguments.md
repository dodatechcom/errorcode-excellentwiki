---
title: "[Solution] TypeScript TS2554 — Expected fewer arguments"
description: "TS2554 occurs when too many arguments are passed to a function."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Pass only the arguments the function expects."
---

The error "[Solution] TypeScript TS2554 — Expected fewer arguments" occurs when ts2554 occurs when too many arguments are passed to a function.

## Solution

Pass only the arguments the function expects.

## Code Example

```typescript
function add(a: number, b: number) { return a + b; }
add(1, 2, 3); // TS2554
```
