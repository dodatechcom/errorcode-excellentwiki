---
title: "[Solution] Express res.vary Error"
description: "Vary header not setting."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Vary header not setting.

## Common Causes

Wrong usage.

## How to Fix

Use res.vary.

## Example

```javascript
res.vary('Accept-Encoding');
```
