---
title: "[Solution] TypeScript TS2375 — Type not assignable (exactOptionalPropertyTypes)"
description: "TS2375 occurs when exactOptionalPropertyTypes is enabled and types don't match."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use undefined explicitly or disable exactOptionalPropertyTypes."
---

The error "[Solution] TypeScript TS2375 — Type not assignable (exactOptionalPropertyTypes)" occurs when ts2375 occurs when exactoptionalpropertytypes is enabled and types don't match.

## Solution

Use undefined explicitly or disable exactOptionalPropertyTypes.

## Code Example

```typescript
interface Config { debug?: boolean; }
const config: Config = { debug: undefined }; // TS2375
const config: Config = {}; // Fix - omit the property
```
