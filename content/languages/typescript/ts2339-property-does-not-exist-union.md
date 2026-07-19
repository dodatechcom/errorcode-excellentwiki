---
title: "[Solution] TypeScript TS2339 — Property does not exist on union type"
description: "TS2339 occurs when accessing a property that doesn't exist on all union members."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Narrow the type with type guards before accessing the property."
---

The error "[Solution] TypeScript TS2339 — Property does not exist on union type" occurs when ts2339 occurs when accessing a property that doesn't exist on all union members.

## Solution

Narrow the type with type guards before accessing the property.

## Code Example

```typescript
function process(input: string | number) {
  return input.length; // TS2339 on number
```
