---
title: "[Solution] TypeScript TS18049 — 'X' possibly null or undefined (check)"
description: "TS18049 can be resolved with explicit null/undefined check."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Check for both null and undefined before using."
---

The error "[Solution] TypeScript TS18049 — 'X' possibly null or undefined (check)" occurs when ts18049 can be resolved with explicit null/undefined check.

## Solution

Check for both null and undefined before using.

## Code Example

```typescript
function getVal(): string | null | undefined { ... }
const val = getVal();
if (val != null) console.log(val.length); // Fix
```
