---
title: "[Solution] TypeScript TS2769 — No overload matches this call (method)"
description: "TS2769 occurs when no method overload matches the arguments."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Review the method signature and provide correct arguments."
---

The error "[Solution] TypeScript TS2769 — No overload matches this call (method)" occurs when ts2769 occurs when no method overload matches the arguments.

## Solution

Review the method signature and provide correct arguments.

## Code Example

```typescript
arr.map((x: number) => x.toString());
arr.map((x: string) => x.length); // TS2769 if types mismatch
```
