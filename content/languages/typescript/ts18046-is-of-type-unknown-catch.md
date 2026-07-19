---
title: "[Solution] TypeScript TS18046 — 'X' is of type 'unknown' (catch block)"
description: "TS18046 occurs when using an error variable typed as unknown in catch blocks."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Type narrow the error before accessing its properties."
---

The error "[Solution] TypeScript TS18046 — 'X' is of type 'unknown' (catch block)" occurs when ts18046 occurs when using an error variable typed as unknown in catch blocks.

## Solution

Type narrow the error before accessing its properties.

## Code Example

```typescript
try {
  JSON.parse(input);
} catch (e) {
  console.log(e.message); // TS18046
  if (e instanceof Error) console.log(e.message);
}
```
