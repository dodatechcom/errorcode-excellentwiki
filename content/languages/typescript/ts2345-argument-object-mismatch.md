---
title: "[Solution] TypeScript TS2345 — Argument object type mismatch"
description: "TS2345 occurs when passing an object with wrong shape to a function."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Ensure the object matches the expected parameter type."
---

The error "[Solution] TypeScript TS2345 — Argument object type mismatch" occurs when ts2345 occurs when passing an object with wrong shape to a function.

## Solution

Ensure the object matches the expected parameter type.

## Code Example

```typescript
interface Config { host: string; port: number; }
function start(config: Config) {}
start({ host: 'localhost' }); // TS2345 - missing port
```
