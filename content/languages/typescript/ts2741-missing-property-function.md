---
title: "[Solution] TypeScript TS2741 — Property missing in type (function return)"
description: "TS2741 occurs when a function return object is missing properties."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Ensure the return object has all required properties."
---

The error "[Solution] TypeScript TS2741 — Property missing in type (function return)" occurs when ts2741 occurs when a function return object is missing properties.

## Solution

Ensure the return object has all required properties.

## Code Example

```typescript
interface Config { host: string; port: number; }
function getConfig(): Config {
  return { host: 'localhost' }; // TS2741 - missing port
}
```
