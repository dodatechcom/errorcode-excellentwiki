---
title: "[Solution] TypeScript TS2894 — 'export =' is not allowed in ambient module declaration"
description: "TS2894 occurs when using export = syntax in an ambient module."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use export default or named exports."
---

The error "[Solution] TypeScript TS2894 — 'export =' is not allowed in ambient module declaration" occurs when ts2894 occurs when using export = syntax in an ambient module.

## Solution

Use export default or named exports.

## Code Example

```typescript
declare module 'my-lib' {
  export = something; // TS2894
  export default something; // Fix
```
