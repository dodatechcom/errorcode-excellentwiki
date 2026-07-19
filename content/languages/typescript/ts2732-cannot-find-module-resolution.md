---
title: "[Solution] TypeScript TS2732 — Cannot find module (module resolution)"
description: "TS2732 occurs when module resolution can't find the specified module."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Configure moduleResolution in tsconfig or install the package."
---

The error "TypeScript TS2732 — Cannot find module (module resolution)" occurs when module resolution can't find the specified module.

## Solution

Configure moduleResolution in tsconfig or install the package.

## Code Example

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "moduleResolution": "node"
  }
}
```
