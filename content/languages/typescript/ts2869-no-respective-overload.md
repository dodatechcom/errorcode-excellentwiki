---
title: "[Solution] TypeScript TS2869 — No respective overload exists for 'X'"
description: "TS2869 occurs when no overload matches when calling a function."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Check the overloads and provide compatible arguments."
---

The error "[Solution] TypeScript TS2869 — No respective overload exists for 'X'" occurs when ts2869 occurs when no overload matches when calling a function.

## Solution

Check the overloads and provide compatible arguments.

## Code Example

```typescript
function handle(x: string): void;
function handle(x: number): void;
handle(true); // TS2869
```
