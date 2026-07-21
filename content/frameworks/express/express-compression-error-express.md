---
title: "[Solution] Express Compression Error Express"
description: "Compression not working."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Compression not working.

## Common Causes

Not added.

## How to Fix

Add compression.

## Example

```javascript
const compression = require('compression');
app.use(compression());
```
