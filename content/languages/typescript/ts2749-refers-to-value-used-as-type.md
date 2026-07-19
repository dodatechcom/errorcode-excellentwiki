---
title: "[Solution] TypeScript TS2749 — 'X' refers to a value, but is used as a type"
description: "TS2749 occurs when using a value where a type is expected."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use 'typeof' to get the type from the value."
---

The error "[Solution] TypeScript TS2749 — 'X' refers to a value, but is used as a type" occurs when ts2749 occurs when using a value where a type is expected.

## Solution

Use 'typeof' to get the type from the value.

## Code Example

```typescript
const config = { port: 3000 };
type ConfigType = config; // TS2749
type ConfigType = typeof config; // Fix
```
