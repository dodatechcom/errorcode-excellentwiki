---
title: "[Solution] TypeScript TS2321 — Type not assignable (strict mode)"
description: "TS2321 occurs with strict type checking when types are incompatible."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Ensure strict type compatibility."
---

The error "[Solution] TypeScript TS2321 — Type not assignable (strict mode)" occurs when ts2321 occurs with strict type checking when types are incompatible.

## Solution

Ensure strict type compatibility.

## Code Example

```typescript
const config: { port: number } = { port: '3000' }; // TS2321
const config: { port: number } = { port: 3000 }; // Fix
```
