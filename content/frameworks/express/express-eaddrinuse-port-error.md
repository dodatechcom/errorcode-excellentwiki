---
title: "[Solution] Express EADDRINUSE Port Error"
description: "Port already in use."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Port already in use.

## Common Causes

Another process on port.

## How to Fix

Kill process.

## Example

```javascript
lsof -i :3000
kill -9 <PID>
```
