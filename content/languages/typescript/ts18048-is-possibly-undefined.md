---
title: "[Solution] TypeScript TS18048 — 'X' is possibly 'undefined'"
description: "TS18048 occurs when using a value that could be undefined."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Check for undefined or use optional chaining."
---

The error "[Solution] TypeScript TS18048 — 'X' is possibly 'undefined'" occurs when ts18048 occurs when using a value that could be undefined.

## Solution

Check for undefined or use optional chaining.

## Code Example

```typescript
interface Config { host?: string; }
function start(config: Config) {
  console.log(config.host.toUpperCase()); // TS18048
```
