---
title: "[Solution] Express req.acceptsCharsets Error"
description: "Charset negotiation failing."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Charset negotiation failing.

## Common Causes

No matching charset.

## How to Fix

Check Accept-Charset.

## Example

```javascript
const charset = req.acceptsCharsets('utf-8');
```
