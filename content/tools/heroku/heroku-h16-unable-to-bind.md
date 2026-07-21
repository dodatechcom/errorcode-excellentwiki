---
title: "[Solution] Heroku H16 Unable to Bind Error"
description: "Fix Heroku H16 unable to bind errors. Resolve port binding issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku H16 Unable to Bind Error can prevent your application from working correctly.

## Common Causes

- Port not configured
- Port already in use
- PORT env not set

## How to Fix

### Use PORT Environment

```javascript
const port = process.env.PORT || 3000;
app.listen(port);
```

