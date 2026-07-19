---
title: "[Solution] TypeScript TS18048 — 'X' is possibly undefined (default value)"
description: "TS18048 can be resolved with default values."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Provide default values for optional properties."
---

The error "[Solution] TypeScript TS18048 — 'X' is possibly undefined (default value)" occurs when ts18048 can be resolved with default values.

## Solution

Provide default values for optional properties.

## Code Example

```typescript
interface Config { host?: string; }
function start(config: Config) {
  const host = config.host ?? 'localhost'; // Fix
}
```
