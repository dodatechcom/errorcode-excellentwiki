---
title: "[Solution] TypeScript TS7053 — Element implicitly has 'any' type (index)"
description: "TS7053 occurs when using bracket notation on an object without an index signature."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Add an index signature to the type or use a type assertion."
---

The error "[Solution] TypeScript TS7053 — Element implicitly has 'any' type (index)" occurs when ts7053 occurs when using bracket notation on an object without an index signature.

## Solution

Add an index signature to the type or use a type assertion.

## Code Example

```typescript
const obj: { name: string } = { name: 'Alice' };
const val = obj['age']; // TS7053
```
