---
title: "[Solution] TypeScript TS2532 — Object is possibly undefined (parameter)"
description: "TS2532 occurs when a parameter might be undefined."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Add a default value or check for undefined."
---

The error "[Solution] TypeScript TS2532 — Object is possibly undefined (parameter)" occurs when ts2532 occurs when a parameter might be undefined.

## Solution

Add a default value or check for undefined.

## Code Example

```typescript
function greet(name?: string) {
  console.log(name.length); // TS2532
```
