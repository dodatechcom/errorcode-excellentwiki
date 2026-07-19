---
title: "[Solution] TypeScript TS2339 — Property does not exist on primitive type"
description: "TS2339 occurs when accessing a property on a primitive type."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Primitives have limited properties. Check the type."
---

The error "[Solution] TypeScript TS2339 — Property does not exist on primitive type" occurs when ts2339 occurs when accessing a property on a primitive type.

## Solution

Primitives have limited properties. Check the type.

## Code Example

```typescript
const str: string = 'hello';
str.push('!'); // TS2339 - strings don't have push
```
