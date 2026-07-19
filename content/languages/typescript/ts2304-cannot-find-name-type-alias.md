---
title: "[Solution] TypeScript TS2304 — Cannot find name (type alias)"
description: "TS2304 occurs when using a type alias that hasn't been declared."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Import or declare the type alias."
---

The error "[Solution] TypeScript TS2304 — Cannot find name (type alias)" occurs when ts2304 occurs when using a type alias that hasn't been declared.

## Solution

Import or declare the type alias.

## Code Example

```typescript
const value: StringOrNumber = 'hello'; // TS2304
type StringOrNumber = string | number;
```
