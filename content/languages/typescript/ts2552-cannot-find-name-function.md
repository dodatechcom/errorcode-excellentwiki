---
title: "[Solution] TypeScript TS2552 — Cannot find name (did you mean function)"
description: "TS2552 suggests similar function names when one is misspelled."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use the correct function name."
---

The error "[Solution] TypeScript TS2552 — Cannot find name (did you mean function)" occurs when ts2552 suggests similar function names when one is misspelled.

## Solution

Use the correct function name.

## Code Example

```typescript
function processData() {}
processDat(); // TS2552 - did you mean processData?
```
