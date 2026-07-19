---
title: "[Solution] TypeScript TS2307 — Cannot find module (CSS import)"
description: "TS2307 occurs when importing CSS files without type declarations."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Add a declaration file for CSS imports."
---

The error "[Solution] TypeScript TS2307 — Cannot find module (CSS import)" occurs when ts2307 occurs when importing css files without type declarations.

## Solution

Add a declaration file for CSS imports.

## Code Example

```typescript
// declarations.d.ts
declare module '*.css';
```
