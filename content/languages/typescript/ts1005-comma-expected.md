---
title: "[Solution] TypeScript TS1005 — ',' expected"
description: "TS1005 occurs when a comma is expected in a syntax construct."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "syntax-error"]]
severity: "error"
solution: "Add the missing comma in the correct position."
---

The error "[Solution] TypeScript TS1005 — ',' expected" occurs when ts1005 occurs when a comma is expected in a syntax construct.

## Solution

Add the missing comma in the correct position.

## Code Example

```typescript
const obj = {
  name: 'Alice'
  age: 30  // TS1005 - missing comma
};
```
