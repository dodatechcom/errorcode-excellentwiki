---
title: "[Solution] Express SIGINT Handler Error"
description: "SIGINT not handled."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

SIGINT not handled.

## Common Causes

No handler.

## How to Fix

Add handler.

## Example

```javascript
process.on('SIGINT', () => { server.close(); process.exit(0); });
```
