---
title: "[Solution] TypeScript TS2304 — Cannot find name (global scope)"
description: "TS2304 occurs when TypeScript cannot resolve an identifier in global scope."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Ensure the variable is declared or imported before use."
---

The error "[Solution] TypeScript TS2304 — Cannot find name (global scope)" occurs when ts2304 occurs when typescript cannot resolve an identifier in global scope.

## Solution

Ensure the variable is declared or imported before use.

## Code Example

```typescript
console.log(myVar); // TS2304
let myVar = 10;
```
