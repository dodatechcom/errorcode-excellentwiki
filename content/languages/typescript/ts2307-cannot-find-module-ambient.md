---
title: "[Solution] TypeScript TS2307 — Cannot find module (ambient)"
description: "TS2307 occurs when importing a module without ambient declarations."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Create an ambient module declaration."
---

The error "[Solution] TypeScript TS2307 — Cannot find module (ambient)" occurs when ts2307 occurs when importing a module without ambient declarations.

## Solution

Create an ambient module declaration.

## Code Example

```typescript
// my-lib.d.ts
declare module 'my-lib' {
  export function doSomething(): void;
}
```
