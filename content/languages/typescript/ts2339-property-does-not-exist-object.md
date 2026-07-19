---
title: "[Solution] TypeScript TS2339 — Property does not exist on type (object)"
description: "TS2339 occurs when accessing a property not defined in the type."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Add the property to the type definition or use optional chaining."
---

The error "[Solution] TypeScript TS2339 — Property does not exist on type (object)" occurs when ts2339 occurs when accessing a property not defined in the type.

## Solution

Add the property to the type definition or use optional chaining.

## Code Example

```typescript
interface User { name: string; }
const user: User = { name: 'Alice' };
console.log(user.age); // TS2339
```
