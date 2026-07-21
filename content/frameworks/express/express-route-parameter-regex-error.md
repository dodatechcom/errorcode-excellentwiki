---
title: "[Solution] Express Route Parameter Regex Error"
description: "Route regex not matching."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Route regex not matching.

## Common Causes

Wrong pattern.

## How to Fix

Test pattern.

## Example

```javascript
app.get(/^\/users\/(\d+)$/, (req, res) => {});
```
