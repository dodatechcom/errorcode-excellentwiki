---
title: "[Solution] Netlify Synchronous Function Error"
description: "Fix Netlify synchronous function errors. Resolve standard function issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Synchronous Function Error can prevent your application from working correctly.

## Common Causes

- Function timeout
- Response not returned
- Error not caught
- Response format invalid

## How to Fix

### Return Response

```javascript
exports.handler = async () => {
  return {
    statusCode: 200,
    body: JSON.stringify({ message: "OK" })
  };
};
```

