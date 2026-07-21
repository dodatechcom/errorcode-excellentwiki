---
title: "[Solution] Express Uncaught Exception Express"
description: "Uncaught exception crashing."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Uncaught exception crashing.

## Common Causes

No handler.

## How to Fix

Add handler.

## Example

```javascript
process.on('uncaughtException', (e) => { console.error(e); process.exit(1); });
```
