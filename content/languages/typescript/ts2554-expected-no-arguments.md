---
title: "[Solution] TypeScript TS2554 — Expected no arguments"
description: "TS2554 occurs when passing arguments to a function that takes none."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Don't pass arguments to functions that don't accept them."
---

The error "[Solution] TypeScript TS2554 — Expected no arguments" occurs when ts2554 occurs when passing arguments to a function that takes none.

## Solution

Don't pass arguments to functions that don't accept them.

## Code Example

```typescript
function init() {}
init('data'); // TS2554 - expected no arguments
```
