---
title: "[Solution] TypeScript TS2307 — Cannot find module (scoped package)"
description: "TS2307 occurs when a scoped npm package is not installed."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Install the scoped package."
---

The error "[Solution] TypeScript TS2307 — Cannot find module (scoped package)" occurs when ts2307 occurs when a scoped npm package is not installed.

## Solution

Install the scoped package.

## Code Example

```typescript
import { helper } from '@myorg/utils'; // TS2307
// Fix: npm install @myorg/utils
```
