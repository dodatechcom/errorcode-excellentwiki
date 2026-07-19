---
title: "[Solution] TypeScript TS2885 — 'import =' is not allowed in ambient module declaration"
description: "TS2885 occurs when using import = syntax in an ambient module."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use import * as syntax instead."
---

The error "[Solution] TypeScript TS2885 — 'import =' is not allowed in ambient module declaration" occurs when ts2885 occurs when using import = syntax in an ambient module.

## Solution

Use import * as syntax instead.

## Code Example

```typescript
declare module 'my-lib' {
  import x = require('other'); // TS2885
  import * as x from 'other'; // Fix
```
