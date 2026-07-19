---
title: "[Solution] TypeScript TS2552 — Cannot find name (did you mean)"
description: "TS2552 occurs when a name is not found but a similar name exists."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use the suggested name or import the correct identifier."
---

The error "[Solution] TypeScript TS2552 — Cannot find name (did you mean)" occurs when ts2552 occurs when a name is not found but a similar name exists.

## Solution

Use the suggested name or import the correct identifier.

## Code Example

```typescript
const userName = 'Alice';
console.log(userNamee); // TS2552 - did you mean userName?
```
