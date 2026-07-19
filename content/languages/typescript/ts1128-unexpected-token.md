---
title: "[Solution] TypeScript TS1128 — Declaration or statement expected (unexpected token)"
description: "TS1128 occurs when the parser encounters an invalid token."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "syntax-error"]]
severity: "error"
solution: "Remove or fix the unexpected token."
---

The error "[Solution] TypeScript TS1128 — Declaration or statement expected (unexpected token)" occurs when ts1128 occurs when the parser encounters an invalid token.

## Solution

Remove or fix the unexpected token.

## Code Example

```typescript
const x = 10
const y = 20; // TS1128 if semicolon missing after const
```
