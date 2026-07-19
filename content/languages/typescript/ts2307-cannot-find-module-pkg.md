---
title: "[Solution] TypeScript TS2307 — Cannot find module (package)"
description: "TS2307 occurs when TypeScript cannot find the specified package."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Install the package using npm or yarn."
---

The error "[Solution] TypeScript TS2307 — Cannot find module (package)" occurs when ts2307 occurs when typescript cannot find the specified package.

## Solution

Install the package using npm or yarn.

## Code Example

```typescript
import express from 'express'; // TS2307 if not installed
// Fix: npm install express
```
