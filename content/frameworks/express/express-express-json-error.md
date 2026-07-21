---
title: "[Solution] Express express.json Error"
description: "Body not parsing."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Body not parsing.

## Common Causes

Wrong Content-Type.

## How to Fix

Set correct type.

## Example

```javascript
app.use(express.json({ limit: '10mb' }));
```
