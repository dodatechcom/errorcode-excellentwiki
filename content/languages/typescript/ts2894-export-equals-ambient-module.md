---
title: "[Solution] TypeScript TS2894 — 'export =' not allowed in ambient module"
description: "TS2894 occurs when using export = in ambient module declarations."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use export default instead."
---

The error "[Solution] TypeScript TS2894 — 'export =' not allowed in ambient module" occurs when ts2894 occurs when using export = in ambient module declarations.

## Solution

Use export default instead.

## Code Example

```typescript
declare module 'my-lib' {
  export = MyClass; // TS2894
  export default MyClass; // Fix
```
