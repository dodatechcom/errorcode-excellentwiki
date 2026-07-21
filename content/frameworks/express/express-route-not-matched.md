---
title: "[Solution] Express Route Not Matched"
description: "Cannot find route."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Cannot find route.

## Common Causes

Wrong method/path.

## How to Fix

Check definitions.

## Example

```javascript
app.get('/hello', (req, res) => res.send('Hi'));
```
