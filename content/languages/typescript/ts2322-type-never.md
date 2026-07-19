---
title: "[Solution] TypeScript TS2322 — Type 'never' is not assignable"
description: "TS2322 occurs when assigning a never type value."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Check the logic that produces the never value."
---

The error "[Solution] TypeScript TS2322 — Type 'never' is not assignable" occurs when ts2322 occurs when assigning a never type value.

## Solution

Check the logic that produces the never value.

## Code Example

```typescript
function throwError(): never { throw new Error(); }
const val: string = throwError(); // TS2322
```
