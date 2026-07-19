---
title: "[Solution] TypeScript TS2885 — 'import =' not allowed in ambient module"
description: "TS2885 occurs when using import = in ambient declarations."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use import * as syntax."
---

The error "[Solution] TypeScript TS2885 — 'import =' not allowed in ambient module" occurs when ts2885 occurs when using import = in ambient declarations.

## Solution

Use import * as syntax.

## Code Example

```typescript
declare module 'my-lib' {
  import x = require('other'); // TS2885
  import * as x from 'other'; // Fix
```
