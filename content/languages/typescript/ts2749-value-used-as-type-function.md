---
title: "[Solution] TypeScript TS2749 — Value used as type (function)"
description: "TS2749 occurs when using a function value where a type is expected."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use ReturnType or typeof to get the type."
---

The error "[Solution] TypeScript TS2749 — Value used as type (function)" occurs when ts2749 occurs when using a function value where a type is expected.

## Solution

Use ReturnType or typeof to get the type.

## Code Example

```typescript
function create() { return { name: 'Alice' }; }
type Created = create; // TS2749
type Created = ReturnType<typeof create>; // Fix
```
