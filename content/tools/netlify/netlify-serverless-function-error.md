---
title: "[Solution] Netlify Serverless Function Error"
description: "Fix Netlify serverless function errors when functions fail to deploy or execute."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

# Netlify Serverless Function Error

Netlify serverless functions fail to deploy or execute correctly.

```
Function execution timeout
netlify/functions/function-name
```

## Common Causes

- Function exceeds memory or time limit
- Missing dependencies in deployment bundle
- Handler function not exported correctly
- Invalid runtime version
- Large dependency bundle size

## How to Fix

### Check Function Configuration

```toml
[build]
  functions = "netlify/functions"

[functions]
  node_bundler = "esbuild"
  included_files = ["data/**"]
```

### Fix Timeout Issues

```javascript
// netlify/functions/my-function.js
exports.handler = async (event) => {
  // Keep under 10 seconds for background
  // 26 seconds for synchronous
  return {
    statusCode: 200,
    body: JSON.stringify({ message: "OK" })
  };
};
```

### Configure Function Settings

```toml
[functions]
  node_bundler = "esbuild"
  [functions.node]
    runtime = "nodejs18.x"
```

### Check Bundle Size

```bash
# Check function sizes
ls -lh .netlify/functions-*/

# Max size is 50MB uncompressed
```

### Test Functions Locally

```bash
# Test function locally
netlify functions:serve
curl http://localhost:9999/.netlify/functions/my-function
```

## Examples

```javascript
// netlify/functions/api-proxy.js
exports.handler = async (event) => {
  try {
    const response = await fetch("https://api.example.com/data", {
      headers: {
        Authorization: `Bearer ${process.env.API_KEY}`
      }
    });
    const data = await response.json();
    return {
      statusCode: 200,
      body: JSON.stringify(data)
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message })
    };
  }
};
```
