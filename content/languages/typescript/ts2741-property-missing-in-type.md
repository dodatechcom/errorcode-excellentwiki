---
title: "[Solution] TypeScript TS2741 — Property 'X' is missing in type 'Y'"
description: "TS2741 occurs when an object is missing a required property."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Add the missing property."
---

The error "[Solution] TypeScript TS2741 — Property 'X' is missing in type 'Y'" occurs when ts2741 occurs when an object is missing a required property.

## Solution

Add the missing property.

## Code Example

```typescript
interface User { name: string; age: number; }
const user: User = { name: 'Alice' }; // TS2741 - age is missing
```
