---
title: "[Solution] TypeScript TS2322 — Type missing required properties"
description: "TS2322 occurs when the assigned object is missing required properties."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Include all required properties in the object literal."
---

The error "[Solution] TypeScript TS2322 — Type missing required properties" occurs when ts2322 occurs when the assigned object is missing required properties.

## Solution

Include all required properties in the object literal.

## Code Example

```typescript
interface User { name: string; age: number; }
const user: User = { name: 'Alice' }; // TS2322
```
