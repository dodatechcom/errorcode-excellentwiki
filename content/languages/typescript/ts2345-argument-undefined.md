---
title: "[Solution] TypeScript TS2345 — Argument of type 'undefined' not assignable"
description: "TS2345 occurs when passing undefined to a non-optional parameter."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Provide a valid value or make the parameter optional."
---

The error "[Solution] TypeScript TS2345 — Argument of type 'undefined' not assignable" occurs when ts2345 occurs when passing undefined to a non-optional parameter.

## Solution

Provide a valid value or make the parameter optional.

## Code Example

```typescript
function process(data: string) {}
process(undefined); // TS2345
```
