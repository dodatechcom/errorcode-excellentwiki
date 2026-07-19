---
title: "[Solution] TypeScript TS2304 — Cannot find name (enum)"
description: "TS2304 occurs when using an enum that hasn't been declared."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Import or declare the enum."
---

The error "[Solution] TypeScript TS2304 — Cannot find name (enum)" occurs when ts2304 occurs when using an enum that hasn't been declared.

## Solution

Import or declare the enum.

## Code Example

```typescript
const color = Color.Red; // TS2304
enum Color { Red, Green, Blue }
```
