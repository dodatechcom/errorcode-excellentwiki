---
title: "[Solution] TypeScript TS2322 — Type 'null' is not assignable to type 'string'"
description: "TS2322 occurs when assigning null to a non-nullable string type."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use string | null or provide a default value."
---

The error "[Solution] TypeScript TS2322 — Type 'null' is not assignable to type 'string'" occurs when ts2322 occurs when assigning null to a non-nullable string type.

## Solution

Use string | null or provide a default value.

## Code Example

```typescript
let name: string = null; // TS2322
let name: string | null = null; // Fix
```
