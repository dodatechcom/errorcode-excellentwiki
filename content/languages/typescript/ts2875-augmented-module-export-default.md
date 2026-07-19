---
title: "[Solution] TypeScript TS2875 — Augmented module cannot have export default"
description: "TS2875 occurs when an ambient module declaration uses export default."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use named exports instead of default export in ambient modules."
---

The error "[Solution] TypeScript TS2875 — Augmented module cannot have export default" occurs when ts2875 occurs when an ambient module declaration uses export default.

## Solution

Use named exports instead of default export in ambient modules.

## Code Example

```typescript
declare module 'my-lib' {
  export default function(): void; // TS2875
  export function doSomething(): void; // Fix
```
