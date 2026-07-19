---
title: "[Solution] TypeScript TS2307 — Cannot find module (local file)"
description: "TS2307 occurs when TypeScript cannot find a local module file."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Verify the file path and ensure the file exists."
---

The error "[Solution] TypeScript TS2307 — Cannot find module (local file)" occurs when ts2307 occurs when typescript cannot find a local module file.

## Solution

Verify the file path and ensure the file exists.

## Code Example

```typescript
import { helper } from './utils/helper'; // TS2307 if file missing
export function helper() { return 'help'; }
```
