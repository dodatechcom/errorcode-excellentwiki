---
title: "[Solution] TypeScript TS2532 — Object is possibly undefined (optional chaining)"
description: "TS2532 occurs when accessing properties on optional values."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use optional chaining (?.) to safely access properties."
---

The error "[Solution] TypeScript TS2532 — Object is possibly undefined (optional chaining)" occurs when ts2532 occurs when accessing properties on optional values.

## Solution

Use optional chaining (?.) to safely access properties.

## Code Example

```typescript
interface Config { debug?: boolean; }
function check(config: Config) {
  console.log(config.debug); // TS2532
```
