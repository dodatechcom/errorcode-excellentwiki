---
title: "[Solution] TypeScript TS1190 — Missing closing brace"
description: "TS1190 occurs when there is an unclosed block or declaration."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "syntax-error"]]
severity: "error"
solution: "Add the missing closing brace."
---

The error "[Solution] TypeScript TS1190 — Missing closing brace" occurs when ts1190 occurs when there is an unclosed block or declaration.

## Solution

Add the missing closing brace.

## Code Example

```typescript
function doSomething() {
  if (true) {
    console.log('hi');
  // TS1190 - missing closing brace for function
```
