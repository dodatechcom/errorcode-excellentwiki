---
title: "[Solution] TypeScript TS2309 — Unused import"
description: "TS2309 occurs when an imported name is not used in the file."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Remove the unused import or use it in the code."
---

The error "[Solution] TypeScript TS2309 — Unused import" occurs when ts2309 occurs when an imported name is not used in the file.

## Solution

Remove the unused import or use it in the code.

## Code Example

```typescript
import { readFile, writeFile } from 'fs'; // TS2309 - writeFile unused
readFile('test.txt', () => {});
```
