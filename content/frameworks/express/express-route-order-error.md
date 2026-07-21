---
title: "[Solution] Express Route Order Error"
description: "Wrong handler matched."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Wrong handler matched.

## Common Causes

Specific after general.

## How to Fix

Define specific first.

## Example

```javascript
app.get('/u/:id', specific);
app.get('/u', general);
```
