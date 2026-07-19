---
title: "[Solution] TypeScript TS2345 — Argument of type 'null' not assignable"
description: "TS2345 occurs when passing null to a non-nullable parameter."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Check for null or make the parameter nullable."
---

The error "[Solution] TypeScript TS2345 — Argument of type 'null' not assignable" occurs when ts2345 occurs when passing null to a non-nullable parameter.

## Solution

Check for null or make the parameter nullable.

## Code Example

```typescript
function greet(name: string) {}
greet(null); // TS2345
function greet(name: string | null) {} // Fix
```
