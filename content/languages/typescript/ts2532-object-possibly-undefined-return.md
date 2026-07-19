---
title: "[Solution] TypeScript TS2532 — Object is possibly undefined (return value)"
description: "TS2532 occurs when using a potentially undefined return value."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Check the return value before using it."
---

The error "[Solution] TypeScript TS2532 — Object is possibly undefined (return value)" occurs when ts2532 occurs when using a potentially undefined return value.

## Solution

Check the return value before using it.

## Code Example

```typescript
function find(id: number) { return users.find(u => u.id === id); }
const user = find(1);
console.log(user.name); // TS2532
```
