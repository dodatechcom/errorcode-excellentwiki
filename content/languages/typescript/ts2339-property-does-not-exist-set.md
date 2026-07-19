---
title: "[Solution] TypeScript TS2339 — Property does not exist on Set"
description: "TS2339 occurs when using invalid Set methods."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use correct Set methods."
---

The error "[Solution] TypeScript TS2339 — Property does not exist on Set" occurs when ts2339 occurs when using invalid set methods.

## Solution

Use correct Set methods.

## Code Example

```typescript
const set = new Set<string>();
set.push('item'); // TS2339 - Set doesn't have push
set.add('item'); // Fix
```
