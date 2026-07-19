---
title: "[Solution] TypeScript TS2496 — Acts like a base but is not an instance"
description: "TS2496 occurs when a type acts like a class but isn't an instance type."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use the correct type or instance."
---

The error "[Solution] TypeScript TS2496 — Acts like a base but is not an instance" occurs when ts2496 occurs when a type acts like a class but isn't an instance type.

## Solution

Use the correct type or instance.

## Code Example

```typescript
class Base {}
function process<T extends Base>(item: T) {}
process(Base); // TS2496 - pass an instance, not the class
```
