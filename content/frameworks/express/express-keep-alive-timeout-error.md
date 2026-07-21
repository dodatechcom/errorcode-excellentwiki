---
title: "[Solution] Express Keep-Alive Timeout Error"
description: "Connections dropping."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Connections dropping.

## Common Causes

Timeout too short.

## How to Fix

Adjust timeout.

## Example

```javascript
app.keepAliveTimeout = 65000;
```
