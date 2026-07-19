---
title: "[Solution] TypeScript TS2307 — Cannot find module (path alias)"
description: "TS2307 occurs when a path alias is not configured correctly."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Configure paths in tsconfig.json."
---

The error "TypeScript TS2307 — Cannot find module (path alias)" occurs when a path alias is not configured correctly.

## Solution

Configure paths in tsconfig.json.

## Code Example

```typescript
// tsconfig.json paths config
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": { "@/*": ["src/*"] }
  }
}
```
