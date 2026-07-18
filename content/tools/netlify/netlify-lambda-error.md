---
title: "[Solution] Netlify Lambda Function Deployment Error — How to Fix"
description: "Fix Netlify lambda function deployment errors. Resolve function bundling failures, runtime issues, and handler configuration errors."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Netlify lambda function deployment error occurs when your serverless functions fail to deploy or execute. Netlify Functions use AWS Lambda under the hood and require specific bundling and configuration.

## What This Error Means

Netlify Functions are Node.js functions in your `netlify/functions` directory (or configured path). They are bundled during the build process and deployed to AWS Lambda. Failures can occur during bundling, deployment, or runtime execution.

## Why It Happens

- The function file is in the wrong directory or not following the naming convention
- The function exports a handler incorrectly
- Node.js dependencies are not bundled properly
- The function exceeds the execution time or size limits
- The function runtime version is not compatible
- The `netlify.toml` build command does not include function bundling
- The function imports modules that are not compatible with the Lambda runtime
- The function file extension is incorrect

## Common Error Messages

- `Function not found` — The function is not deployed or not in the correct path
- `Handler missing` — The function does not export a `handler` or `default` export
- `Function timed out` — Execution exceeded 10 seconds (free) or 26 seconds (paid)
- `Cannot find module` — Missing dependency in the bundled function
- `Runtime.ExitError` — Function crashed during initialization

## How to Fix It

### Structure Functions Correctly

```javascript
// netlify/functions/hello.js
// Netlify expects: exports.handler or module.exports.handler

exports.handler = async (event, context) => {
  return {
    statusCode: 200,
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message: 'Hello from Netlify Functions!' }),
  };
};

// Or use ES module syntax
export default async (event, context) => {
  return {
    statusCode: 200,
    body: JSON.stringify({ message: 'Hello!' }),
  };
};
```

### Configure Function Path

```toml
# netlify.toml
[build]
  command = "npm run build"
  functions = "netlify/functions"

# If using a custom functions directory
[functions]
  directory = "src/functions"
  node_bundler = "esbuild"
  included_files = ["src/**/*.json"]
```

### Fix Handler Exports

```javascript
// WRONG: No exported handler
async function handleRequest(event) {
  return { statusCode: 200, body: 'OK' };
}

// RIGHT: Export the handler
exports.handler = handleRequest;

// RIGHT: Named export with correct signature
exports.handler = async (event, context) => {
  const { httpMethod, path, queryStringParameters, body } = event;

  // Handle different HTTP methods
  switch (httpMethod) {
    case 'GET':
      return {
        statusCode: 200,
        body: JSON.stringify({ path, query: queryStringParameters }),
      };
    case 'POST':
      return {
        statusCode: 201,
        body: JSON.stringify({ received: JSON.parse(body) }),
      };
    default:
      return { statusCode: 405, body: 'Method not allowed' };
  }
};
```

### Bundle Dependencies Correctly

```json
// package.json — functions need their own dependencies
{
  "name": "my-site",
  "dependencies": {
    "react": "^18.2.0"
  },
  // Function-specific dependencies
  "netlifyConfig": {
    "functions": {
      "external_node_modules": ["sharp", "canvas"]
    }
  }
}
```

```bash
# Install function dependencies
npm install --save uuid axios

# Or use esbuild for automatic bundling
# netlify.toml
[functions]
  node_bundler = "esbuild"
  # esbuild automatically bundles dependencies
```

### Test Functions Locally

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Run functions locally
netlify functions:serve

# Invoke a specific function
netlify functions:invoke hello --payload '{"name": "world"}'

# Test with GET request
netlify functions:invoke hello --method GET

# Check function logs
netlify logs --functions

# Test with environment variables
netlify functions:invoke hello --env API_KEY=abc123
```

## Common Scenarios

- **Wrong file location:** Functions are placed in `src/api/` instead of `netlify/functions/`, so Netlify does not detect them during the build.
- **Missing handler:** A function file exists but does not export a `handler` function. The function is deployed but returns "Handler missing" when invoked.
- **Large dependency tree:** A function imports a heavy library (e.g., `puppeteer`) that exceeds the Lambda size limit, causing the bundle step to fail.

## Prevent It

1. Always place functions in the `netlify/functions` directory (or configured path) and export a `handler` function
2. Use `netlify functions:serve` to test functions locally before deploying
3. Use esbuild bundler for automatic dependency bundling and keep function sizes under 50 MB

## Related Pages

- [Netlify Lambda Error]({{< relref "/tools/netlify/netlify-lambda-error" >}}) — Lambda deployment error
- [Netlify Functions Error]({{< relref "/tools/netlify/netlify-functions-error" >}}) — Function execution error
