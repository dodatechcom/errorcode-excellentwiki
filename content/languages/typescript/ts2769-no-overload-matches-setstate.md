---
title: "[Solution] TypeScript TS2769 — No overload matches this call (setState)"
description: "TS2769 occurs when React setState doesn't match any overload."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Check the state type and the setState argument."
---

The error "[Solution] TypeScript TS2769 — No overload matches this call (setState)" occurs when ts2769 occurs when react setstate doesn't match any overload.

## Solution

Check the state type and the setState argument.

## Code Example

```typescript
const [count, setCount] = useState<number>(0);
setCount('hello'); // TS2769
```
