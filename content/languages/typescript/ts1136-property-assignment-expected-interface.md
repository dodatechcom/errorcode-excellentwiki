---
title: "[Solution] TypeScript TS1136 — Property assignment expected (interface)"
description: "TS1136 occurs when interface syntax is incorrect."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "syntax-error"]]
severity: "error"
solution: "Use correct interface syntax with colons."
---

The error "[Solution] TypeScript TS1136 — Property assignment expected (interface)" occurs when ts1136 occurs when interface syntax is incorrect.

## Solution

Use correct interface syntax with colons.

## Code Example

```typescript
interface User {
  name = string; // TS1136 - use : instead of =
}
```
