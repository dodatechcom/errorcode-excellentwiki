---
title: "[Solution] TypeScript TS2304 — Cannot find name (class)"
description: "TS2304 occurs when using a class that hasn't been declared."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Import or declare the class before use."
---

The error "[Solution] TypeScript TS2304 — Cannot find name (class)" occurs when ts2304 occurs when using a class that hasn't been declared.

## Solution

Import or declare the class before use.

## Code Example

```typescript
const user = new User(); // TS2304
class User { name = 'Alice'; }
```
