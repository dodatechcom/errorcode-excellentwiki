---
title: "[Solution] TypeScript TS7006 — Parameter implicitly has 'any' type (strict mode)"
description: "TS7006 occurs in strict mode when parameter types can't be inferred."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Enable noImplicitAny or add explicit types."
---

The error "[Solution] TypeScript TS7006 — Parameter implicitly has 'any' type (strict mode)" occurs when ts7006 occurs in strict mode when parameter types can't be inferred.

## Solution

Enable noImplicitAny or add explicit types.

## Code Example

```typescript
// tsconfig.json: "noImplicitAny": true
function process(data) {} // TS7006
function process(data: string) {} // Fix
```
