---
title: "[Solution] TypeScript TS2339 — Property does not exist on class instance"
description: "TS2339 occurs when accessing a non-existent property on a class."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Add the property to the class or check for typos."
---

The error "[Solution] TypeScript TS2339 — Property does not exist on class instance" occurs when ts2339 occurs when accessing a non-existent property on a class.

## Solution

Add the property to the class or check for typos.

## Code Example

```typescript
class User {
  name = 'Alice';
}
const user = new User();
console.log(user.age); // TS2339
```
