---
title: "[Solution] TypeScript TS2783 — Unused import (noUnusedLocals)"
description: "TS2783 occurs when an import is not used with noUnusedLocals enabled."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Remove unused imports."
---

The error "[Solution] TypeScript TS2783 — Unused import (noUnusedLocals)" occurs when ts2783 occurs when an import is not used with nounusedlocals enabled.

## Solution

Remove unused imports.

## Code Example

```typescript
import { useState, useEffect } from 'react'; // useEffect unused
// Fix: remove unused import
```
