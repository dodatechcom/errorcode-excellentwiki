---
title: "[Solution] Express EACCES Permission Error"
description: "Cannot bind to privileged port."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Cannot bind to privileged port.

## Common Causes

Port below 1024.

## How to Fix

Use higher port.

## Example

```javascript
app.listen(3000);
```
