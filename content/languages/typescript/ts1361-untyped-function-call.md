---
title: "[Solution] TypeScript TS1361 — Untyped function call"
description: "TS1361 occurs when calling a function that has no type declarations."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Add type declarations or install @types package."
---

The error "[Solution] TypeScript TS1361 — Untyped function call" occurs when ts1361 occurs when calling a function that has no type declarations.

## Solution

Add type declarations or install @types package.

## Code Example

```typescript
// Missing type declarations
myLibrary.doSomething(); // TS1361
// Fix: npm install @types/my-library
```
