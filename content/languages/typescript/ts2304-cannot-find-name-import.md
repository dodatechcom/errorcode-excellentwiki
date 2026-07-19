---
title: "[Solution] TypeScript TS2304 — Cannot find name (missing import)"
description: "TS2304 occurs when a required import is missing from the file."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Add the missing import statement at the top of the file."
---

The error "[Solution] TypeScript TS2304 — Cannot find name (missing import)" occurs when ts2304 occurs when a required import is missing from the file.

## Solution

Add the missing import statement at the top of the file.

## Code Example

```typescript
import { readFile } from 'fs';
readFile('test.txt', () => {});
```
