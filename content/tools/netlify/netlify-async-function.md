---
title: "[Solution] Netlify Asynchronous Function Error"
description: "Fix Netlify asynchronous function errors. Resolve background function issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Asynchronous Function Error can prevent your application from working correctly.

## Common Causes

- Background function not configured
- Function timed out
- Response not sent
- Function not invoked

## How to Fix

### Create Background Function

```javascript
// netlify/functions/process.js
exports.handler = async (event) => {
  // Long running task
  return { statusCode: 202, body: "Processing" };
};
```

