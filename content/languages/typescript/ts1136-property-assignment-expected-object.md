---
title: "[Solution] TypeScript TS1136 — Property assignment expected (object)"
description: "TS1136 occurs when property syntax is incorrect in an object."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "syntax-error"]]
severity: "error"
solution: "Use colon (:) between property name and value."
---

The error "[Solution] TypeScript TS1136 — Property assignment expected (object)" occurs when ts1136 occurs when property syntax is incorrect in an object.

## Solution

Use colon (:) between property name and value.

## Code Example

```typescript
const obj = {
  name = 'Alice' // TS1136 - use : instead of =
}
```
