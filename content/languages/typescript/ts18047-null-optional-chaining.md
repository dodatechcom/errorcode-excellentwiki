---
title: "[Solution] TypeScript TS18047 — 'X' is possibly null (optional chaining)"
description: "TS18047 can be resolved with optional chaining."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use optional chaining (?.) to safely access properties."
---

The error "[Solution] TypeScript TS18047 — 'X' is possibly null (optional chaining)" occurs when ts18047 can be resolved with optional chaining.

## Solution

Use optional chaining (?.) to safely access properties.

## Code Example

```typescript
function findUser(id: number): User | null { ... }
const name = findUser(1)?.name; // Optional chaining
```
