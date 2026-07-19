---
title: "[Solution] TypeScript TS7053 — Element implicitly has 'any' type (map iteration)"
description: "TS7053 occurs when iterating over a Map without proper typing."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Provide generic type parameters to the Map."
---

The error "[Solution] TypeScript TS7053 — Element implicitly has 'any' type (map iteration)" occurs when ts7053 occurs when iterating over a map without proper typing.

## Solution

Provide generic type parameters to the Map.

## Code Example

```typescript
const map = new Map();
map.set('key', 123);
for (const [k, v] of map) {} // TS7053
```
