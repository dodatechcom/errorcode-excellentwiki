---
title: "[Solution] TypeScript TS2339 — Property does not exist on type (array)"
description: "TS2339 occurs when calling array methods that don't exist."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use the correct array method."
---

The error "[Solution] TypeScript TS2339 — Property does not exist on type (array)" occurs when ts2339 occurs when calling array methods that don't exist.

## Solution

Use the correct array method.

## Code Example

```typescript
const arr = [1, 2, 3];
arr.pushh(4); // TS2339 - pushh doesn't exist
```
