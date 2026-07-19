---
title: "[Solution] TypeScript TS2300 — Duplicate identifier (parameter)"
description: "TS2300 occurs when a parameter name conflicts with another declaration."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use a different parameter name."
---

The error "[Solution] TypeScript TS2300 — Duplicate identifier (parameter)" occurs when ts2300 occurs when a parameter name conflicts with another declaration.

## Solution

Use a different parameter name.

## Code Example

```typescript
const name = 'Alice';
function greet(name: string) {} // TS2300 if same scope
```
