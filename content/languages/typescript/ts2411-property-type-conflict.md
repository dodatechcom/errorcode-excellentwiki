---
title: "[Solution] TypeScript TS2411 — Property type conflict"
description: "TS2411 occurs when overriding a property with incompatible type."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Make the overriding property type compatible."
---

The error "[Solution] TypeScript TS2411 — Property type conflict" occurs when ts2411 occurs when overriding a property with incompatible type.

## Solution

Make the overriding property type compatible.

## Code Example

```typescript
interface Animal { name: string; }
interface Dog extends Animal { name: number; } // TS2411
```
