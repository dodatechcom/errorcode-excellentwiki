---
title: "[Solution] TypeScript TS2531 — Object possibly null (prototype)"
description: "TS2531 occurs when Object.getPrototypeOf may return null."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Check for null before using the prototype."
---

The error "[Solution] TypeScript TS2531 — Object possibly null (prototype)" occurs when ts2531 occurs when object.getprototypeof may return null.

## Solution

Check for null before using the prototype.

## Code Example

```typescript
const proto = Object.getPrototypeOf(obj);
console.log(proto.constructor.name); // TS2531
```
