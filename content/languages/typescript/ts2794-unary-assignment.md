---
title: "[Solution] TypeScript TS2794 — Expected a '-breaking assignment (unary)"
description: "TS2794 occurs with incorrect unary operator usage."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use the correct assignment syntax."
---

The error "[Solution] TypeScript TS2794 — Expected a '-breaking assignment (unary)" occurs when ts2794 occurs with incorrect unary operator usage.

## Solution

Use the correct assignment syntax.

## Code Example

```typescript
let x = 10;
const result = ++x; // TS2794 in some contexts
```
