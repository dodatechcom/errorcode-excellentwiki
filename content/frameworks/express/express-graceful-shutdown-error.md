---
title: "[Solution] Express Graceful Shutdown Error"
description: "Server not shutting down."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Server not shutting down.

## Common Causes

No signal handlers.

## How to Fix

Handle signals.

## Example

```javascript
process.on('SIGTERM', () => server.close(() => process.exit(0)));
```
