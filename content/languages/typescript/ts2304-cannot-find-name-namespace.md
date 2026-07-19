---
title: "[Solution] TypeScript TS2304 — Cannot find name (namespace)"
description: "TS2304 occurs when using a namespace member that hasn't been imported."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Import the namespace or use the full path."
---

The error "[Solution] TypeScript TS2304 — Cannot find name (namespace)" occurs when ts2304 occurs when using a namespace member that hasn't been imported.

## Solution

Import the namespace or use the full path.

## Code Example

```typescript
namespace Utils {
  export function helper() { return 'help'; }
}
console.log(helper()); // TS2304
console.log(Utils.helper()); // Fix
```
