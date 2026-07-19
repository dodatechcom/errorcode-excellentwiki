---
title: "[Solution] TypeScript TS2309 — Unused export"
description: "TS2309 occurs when an exported name is not used."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Remove the unused export."
---

The error "[Solution] TypeScript TS2309 — Unused export" occurs when ts2309 occurs when an exported name is not used.

## Solution

Remove the unused export.

## Code Example

```typescript
export const unused = 10; // TS2309 if never imported
```
