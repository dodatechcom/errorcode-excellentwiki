---
title: "[Solution] Express req.acceptsEncodings Error"
description: "Encoding negotiation failing."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Encoding negotiation failing.

## Common Causes

No matching encoding.

## How to Fix

Check Accept-Encoding.

## Example

```javascript
const enc = req.acceptsEncodings('gzip', 'deflate');
```
