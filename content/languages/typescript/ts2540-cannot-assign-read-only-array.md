---
title: "[Solution] TypeScript TS2540 — Cannot assign to read-only (array)"
description: "TS2540 occurs when modifying a readonly array."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use a mutable array or readonly type correctly."
---

The error "[Solution] TypeScript TS2540 — Cannot assign to read-only (array)" occurs when ts2540 occurs when modifying a readonly array.

## Solution

Use a mutable array or readonly type correctly.

## Code Example

```typescript
const arr: readonly number[] = [1, 2, 3];
arr.push(4); // TS2540 - readonly arrays can't be modified
```
