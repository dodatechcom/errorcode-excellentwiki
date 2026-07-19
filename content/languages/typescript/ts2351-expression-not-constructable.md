---
title: "[Solution] TypeScript TS2351 — This expression is not constructable"
description: "TS2351 occurs when trying to use 'new' on something that can't be constructed."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use a constructor function or class."
---

The error "[Solution] TypeScript TS2351 — This expression is not constructable" occurs when ts2351 occurs when trying to use 'new' on something that can't be constructed.

## Solution

Use a constructor function or class.

## Code Example

```typescript
const factory = () => {};
const obj = new factory(); // TS2351
// Fix:
class Factory { create() {} }
const obj = new Factory();
```
