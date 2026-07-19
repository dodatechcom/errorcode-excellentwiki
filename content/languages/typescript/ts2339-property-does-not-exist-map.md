---
title: "[Solution] TypeScript TS2339 — Property does not exist on Map"
description: "TS2339 occurs when using object syntax on a Map."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use Map methods instead of object syntax."
---

The error "[Solution] TypeScript TS2339 — Property does not exist on Map" occurs when ts2339 occurs when using object syntax on a map.

## Solution

Use Map methods instead of object syntax.

## Code Example

```typescript
const map = new Map<string, number>();
map['key'] = 1; // TS2339
map.set('key', 1); // Fix
```
