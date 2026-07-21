---
title: "[Solution] Netlify Background Function Error"
description: "Fix Netlify background function errors. Resolve background processing issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Background Function Error can prevent your application from working correctly.

## Common Causes

- Function not returning 202
- Function exceeds 15 minute limit
- No retry mechanism
- Function not logged

## How to Fix

### Return 202

```javascript
exports.handler = async () => {
  return { statusCode: 202, body: "Accepted" };
};
```

