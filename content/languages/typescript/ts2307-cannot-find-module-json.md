---
title: "[Solution] TypeScript TS2307 — Cannot find module (JSON import)"
description: "TS2307 occurs when importing JSON files without proper config."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Enable resolveJsonModule in tsconfig.json."
---

The error "[Solution] TypeScript TS2307 — Cannot find module (JSON import)" occurs when ts2307 occurs when importing json files without proper config.

## Solution

Enable resolveJsonModule in tsconfig.json.

## Code Example

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "resolveJsonModule": true
  }
}
```
