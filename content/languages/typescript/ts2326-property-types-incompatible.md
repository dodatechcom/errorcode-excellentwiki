---
title: "[Solution] TypeScript TS2326 — Property types incompatible"
description: "TS2326 occurs when property types between interfaces are incompatible."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Align the property types across interfaces."
---

The error "[Solution] TypeScript TS2326 — Property types incompatible" occurs when ts2326 occurs when property types between interfaces are incompatible.

## Solution

Align the property types across interfaces.

## Code Example

```typescript
interface A { data: string | number; }
interface B { data: string; }
function copy(a: A): B { return a; } // TS2326
```
