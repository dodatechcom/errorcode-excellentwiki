---
title: "[Solution] Express Morgan Logger Error"
description: "Not logging."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Not logging.

## Common Causes

Not configured.

## How to Fix

Add morgan.

## Example

```javascript
const morgan = require('morgan');
app.use(morgan('combined'));
```
