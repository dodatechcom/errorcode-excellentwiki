---
title: "[Solution] TypeScript TS2688 — Cannot find type definition (React)"
description: "TS2688 occurs when React type definitions are missing."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Install @types/react."
types: ["react"]
---

The error "[Solution] TypeScript TS2688 — Cannot find type definition (React)" occurs when ts2688 occurs when react type definitions are missing.

## Solution

Install @types/react.

## Code Example

```typescript
// Fix:
npm install @types/react
// tsconfig.json
types: ["react"]
```
