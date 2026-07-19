---
title: "[Solution] TypeScript TS1136 — Property assignment expected"
description: "TS1136 occurs when a property assignment is expected in an object literal."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "syntax-error"]]
severity: "error"
solution: "Add proper property syntax (key: value)."
---

The error "[Solution] TypeScript TS1136 — Property assignment expected" occurs when ts1136 occurs when a property assignment is expected in an object literal.

## Solution

Add proper property syntax (key: value).

## Code Example

```typescript
const config = {
  debug
  verbose: true // TS1136 - missing colon
```
