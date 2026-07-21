---
title: "[Solution] Express SIGTERM Handler Error"
description: "SIGTERM not handled."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

SIGTERM not handled.

## Common Causes

No handler.

## How to Fix

Add handler.

## Example

```javascript
process.on('SIGTERM', () => server.close(() => process.exit(0)));
```
