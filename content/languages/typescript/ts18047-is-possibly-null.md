---
title: "[Solution] TypeScript TS18047 — 'X' is possibly 'null'"
description: "TS18047 occurs when using a value that could be null."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Add a null check or use optional chaining."
---

The error "[Solution] TypeScript TS18047 — 'X' is possibly 'null'" occurs when ts18047 occurs when using a value that could be null.

## Solution

Add a null check or use optional chaining.

## Code Example

```typescript
function find(id: number): User | null { ... }
const user = find(1);
console.log(user.name); // TS18047
```
