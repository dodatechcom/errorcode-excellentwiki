---
title: "[Solution] TypeScript TS2300 — Duplicate identifier (import)"
description: "TS2300 occurs when the same name is imported from different modules."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use import aliases to resolve naming conflicts."
---

The error "[Solution] TypeScript TS2300 — Duplicate identifier (import)" occurs when ts2300 occurs when the same name is imported from different modules.

## Solution

Use import aliases to resolve naming conflicts.

## Code Example

```typescript
import { select } from 'd3';
import { select } from 'jquery'; // TS2300
// Fix:
import { select as d3Select } from 'd3';
import { select as $select } from 'jquery';
```
