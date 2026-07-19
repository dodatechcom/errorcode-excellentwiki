---
title: "[Solution] TypeScript TS2326 — Types of property are incompatible"
description: "TS2326 occurs when a property type in one interface doesn't match another."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Make the property types compatible."
---

The error "[Solution] TypeScript TS2326 — Types of property are incompatible" occurs when ts2326 occurs when a property type in one interface doesn't match another.

## Solution

Make the property types compatible.

## Code Example

```typescript
interface A { data: string; }
interface B { data: number; }
function copy(a: A): B { return a; } // TS2326
```
