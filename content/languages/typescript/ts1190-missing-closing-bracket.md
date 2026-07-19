---
title: "[Solution] TypeScript TS1190 — Missing closing bracket"
description: "TS1190 occurs when a bracket is not closed."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "syntax-error"]]
severity: "error"
solution: "Add the missing closing bracket."
---

The error "[Solution] TypeScript TS1190 — Missing closing bracket" occurs when ts1190 occurs when a bracket is not closed.

## Solution

Add the missing closing bracket.

## Code Example

```typescript
const arr = [1, 2, 3; // TS1190 - missing bracket
const arr = [1, 2, 3]; // Fix
```
