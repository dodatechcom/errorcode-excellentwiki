---
title: "[Solution] Express Headers Timeout Error"
description: "Headers timeout."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Headers timeout.

## Common Causes

Timeout too short.

## How to Fix

Increase timeout.

## Example

```javascript
app.headersTimeout = 66000;
```
