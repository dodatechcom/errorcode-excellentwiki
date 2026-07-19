---
title: "[Solution] TypeScript TS1128 — Declaration or statement expected"
description: "TS1128 occurs when the parser encounters an unexpected token."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "syntax-error"]]
severity: "error"
solution: "Remove the unexpected token or add the missing declaration."
---

The error "[Solution] TypeScript TS1128 — Declaration or statement expected" occurs when ts1128 occurs when the parser encounters an unexpected token.

## Solution

Remove the unexpected token or add the missing declaration.

## Code Example

```typescript
function greet() {
  return
  } // TS1128 - unexpected token
```
