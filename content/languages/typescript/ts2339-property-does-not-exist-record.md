---
title: "[Solution] TypeScript TS2339 — Property does not exist on Record type"
description: "TS2339 occurs when accessing a non-existent key on a Record."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use bracket notation with type assertion or add the key."
---

The error "[Solution] TypeScript TS2339 — Property does not exist on Record type" occurs when ts2339 occurs when accessing a non-existent key on a record.

## Solution

Use bracket notation with type assertion or add the key.

## Code Example

```typescript
const data: Record<string, number> = { a: 1 };
console.log(data.b); // TS2339
```
