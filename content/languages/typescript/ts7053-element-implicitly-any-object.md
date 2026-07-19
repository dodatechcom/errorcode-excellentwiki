---
title: "[Solution] TypeScript TS7053 — Element implicitly 'any' (object access)"
description: "TS7053 occurs when accessing object properties dynamically."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Add an index signature or use type assertion."
---

The error "[Solution] TypeScript TS7053 — Element implicitly 'any' (object access)" occurs when ts7053 occurs when accessing object properties dynamically.

## Solution

Add an index signature or use type assertion.

## Code Example

```typescript
const obj: { [key: string]: number } = { a: 1 };
const val = obj['b']; // TS7053
```
