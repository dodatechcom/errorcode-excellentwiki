---
title: "[Solution] TypeScript TS2351 — This expression is not constructable (interface)"
description: "TS2351 occurs when trying to new an interface type."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use a class instead of an interface for construction."
---

The error "[Solution] TypeScript TS2351 — This expression is not constructable (interface)" occurs when ts2351 occurs when trying to new an interface type.

## Solution

Use a class instead of an interface for construction.

## Code Example

```typescript
interface User { name: string; }
const user = new User(); // TS2351
class User { name = 'Alice'; }
const user = new User(); // Fix
```
