---
title: "[Solution] TypeScript TS18046 — 'X' is of type 'unknown' (use assertion)"
description: "TS18046 can be resolved with type assertion when you know the type."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use type assertion if you're certain of the type."
---

The error "[Solution] TypeScript TS18046 — 'X' is of type 'unknown' (use assertion)" occurs when ts18046 can be resolved with type assertion when you know the type.

## Solution

Use type assertion if you're certain of the type.

## Code Example

```typescript
let val: unknown = getData();
const str = (val as string).toUpperCase(); // Assertion
```
