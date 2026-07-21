---
title: "[Solution] Express View Engine Not Set"
description: "Cannot render templates."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Cannot render templates.

## Common Causes

Not configured.

## How to Fix

Set engine.

## Example

```javascript
app.set('view engine', 'ejs');
app.set('views', './views');
```
