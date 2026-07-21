---
title: "[Solution] Express res.cookie Error"
description: "Cookie not setting."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Cookie not setting.

## Common Causes

Wrong options.

## How to Fix

Set options.

## Example

```javascript
res.cookie('name', 'value', { maxAge: 900000, httpOnly: true });
```
