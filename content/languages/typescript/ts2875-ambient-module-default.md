---
title: "[Solution] TypeScript TS2875 — Augmented module cannot have export default"
description: "TS2875 occurs when adding default export to an augmented module."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use named exports in ambient module declarations."
---

The error "[Solution] TypeScript TS2875 — Augmented module cannot have export default" occurs when ts2875 occurs when adding default export to an augmented module.

## Solution

Use named exports in ambient module declarations.

## Code Example

```typescript
declare module 'my-lib' {
  export default class MyClass {} // TS2875
  export class MyClass {} // Fix
```
