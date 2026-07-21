---
title: "[Solution] Express req.accepts Error"
description: "Content negotiation failing."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Content negotiation failing.

## Common Causes

No matching type.

## How to Fix

Check Accept.

## Example

```javascript
if (req.accepts('html')) res.send('<h1>Hi</h1>');
```
