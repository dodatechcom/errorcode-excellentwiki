---
title: "[Solution] TypeScript TS2301 — Duplicate function implementation"
description: "TS2301 occurs when a function is declared more than once in the same scope."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Remove the duplicate function declaration."
---

The error "[Solution] TypeScript TS2301 — Duplicate function implementation" occurs when ts2301 occurs when a function is declared more than once in the same scope.

## Solution

Remove the duplicate function declaration.

## Code Example

```typescript
function greet() { console.log('hi'); }
function greet() { console.log('hello'); } // TS2301
```
