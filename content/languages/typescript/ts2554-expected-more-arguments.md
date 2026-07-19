---
title: "[Solution] TypeScript TS2554 — Expected more arguments"
description: "TS2554 occurs when too few arguments are passed to a function."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Provide all required arguments."
---

The error "[Solution] TypeScript TS2554 — Expected more arguments" occurs when ts2554 occurs when too few arguments are passed to a function.

## Solution

Provide all required arguments.

## Code Example

```typescript
function greet(name: string, age: number) {}
greet('Alice'); // TS2554 - missing age
```
