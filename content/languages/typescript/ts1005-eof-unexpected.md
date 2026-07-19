---
title: "[Solution] TypeScript TS1005 — ',' expected (EOF unexpected)"
description: "TS1005 occurs when unexpected end of file is reached."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "syntax-error"]]
severity: "error"
solution: "Check for unclosed brackets or missing syntax."
---

The error "[Solution] TypeScript TS1005 — ',' expected (EOF unexpected)" occurs when ts1005 occurs when unexpected end of file is reached.

## Solution

Check for unclosed brackets or missing syntax.

## Code Example

```typescript
const obj = {
  name: 'Alice'
  // TS1005 - missing comma or closing brace
```
