---
title: "[Solution] TypeScript TS2783 — Unused variable (prefix with underscore)"
description: "TS2783 can be resolved by prefixing unused variables with underscore."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Prefix unused variables with underscore."
---

The error "[Solution] TypeScript TS2783 — Unused variable (prefix with underscore)" occurs when ts2783 can be resolved by prefixing unused variables with underscore.

## Solution

Prefix unused variables with underscore.

## Code Example

```typescript
const unused = 10; // TS2783
const _unused = 10; // OK - prefixed with underscore
```
