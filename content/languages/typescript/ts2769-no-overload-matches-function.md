---
title: "[Solution] TypeScript TS2769 — No overload matches this call (function)"
description: "TS2769 occurs when no overload of a function matches the provided arguments."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Check the function overloads and provide arguments matching one."
---

The error "[Solution] TypeScript TS2769 — No overload matches this call (function)" occurs when ts2769 occurs when no overload of a function matches the provided arguments.

## Solution

Check the function overloads and provide arguments matching one.

## Code Example

```typescript
function process(value: string): void;
function process(value: number): void;
process(true); // TS2769
```
