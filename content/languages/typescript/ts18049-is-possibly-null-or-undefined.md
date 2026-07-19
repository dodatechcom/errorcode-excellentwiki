---
title: "[Solution] TypeScript TS18049 — 'X' is possibly 'null' or 'undefined'"
description: "TS18049 occurs when a value could be either null or undefined."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Add a check for both null and undefined."
---

The error "[Solution] TypeScript TS18049 — 'X' is possibly 'null' or 'undefined'" occurs when ts18049 occurs when a value could be either null or undefined.

## Solution

Add a check for both null and undefined.

## Code Example

```typescript
function getVal(): string | null | undefined { ... }
const val = getVal();
console.log(val.length); // TS18049
```
