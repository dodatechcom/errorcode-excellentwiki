---
title: "[Solution] TypeScript TS2411 — Property not assignable"
description: "TS2411 occurs when a property type in a derived interface doesn't match the base."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Make the derived property type compatible with the base."
---

The error "[Solution] TypeScript TS2411 — Property not assignable" occurs when ts2411 occurs when a property type in a derived interface doesn't match the base.

## Solution

Make the derived property type compatible with the base.

## Code Example

```typescript
interface Base { value: string; }
interface Derived extends Base { value: number; } // TS2411
```
