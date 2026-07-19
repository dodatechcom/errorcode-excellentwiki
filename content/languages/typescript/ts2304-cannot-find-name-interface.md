---
title: "[Solution] TypeScript TS2304 — Cannot find name (interface)"
description: "TS2304 occurs when using an interface that hasn't been declared."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Import or declare the interface."
---

The error "[Solution] TypeScript TS2304 — Cannot find name (interface)" occurs when ts2304 occurs when using an interface that hasn't been declared.

## Solution

Import or declare the interface.

## Code Example

```typescript
function process(data: UserData) {} // TS2304
interface UserData { name: string; }
```
