---
title: "[Solution] Netlify Environment Variable Not Found Error — Fix Env Variables"
description: "Fix Netlify environment variable errors. Resolve missing env vars, build-time variables, and secret management issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
weight: 10
---

A Netlify environment variable not found error occurs when your site or functions cannot access expected environment variables. Variables may not be set for the correct context or may need special configuration.

## What This Error Means

Your application or functions return undefined or null when accessing environment variables. Netlify provides different variables for different contexts: build time, functions, and browser (client-side).

## Why It Happens

- The environment variable is not set in site settings
- The variable is set for the wrong deploy context
- The variable uses characters that need escaping
- Build-time variables are not available at runtime
- Functions and browser context have different variable access
- The variable name has a typo or different casing

## How to Fix It

### Set Environment Variables via Dashboard

```bash
# In Netlify Dashboard:
# Site Settings > Build & deploy > Environment

# Click "Edit variables"
# Add: KEY = value
# Check "Available to build process" or "Available to functions"
```

### Set Variables via CLI

```bash
# Set a variable
netlify env:set DATABASE_URL "postgresql://..."

# Set for specific context
netlify env:set API_KEY "secret" --context production
netlify env:set API_KEY "test-key" --context deploy-preview

# Import from .env file
netlify env:import .env

# List all variables
netlify env:list
```

### Configure Variables in netlify.toml

```toml
# netlify.toml
[build.environment]
  NODE_VERSION = "18"
  DATABASE_URL = "postgresql://..."
```

### Access Variables in Functions

```javascript
// netlify/functions/my-function.js
exports.handler = async (event) => {
  // Access environment variables
  const dbUrl = process.env.DATABASE_URL;
  const apiKey = process.env.API_KEY;

  if (!dbUrl) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'DATABASE_URL not set' }),
    };
  }

  return {
    statusCode: 200,
    body: JSON.stringify({ configured: true }),
  };
};
```

### Access Variables in Frontend

```html
<!-- Variables must be prefixed with NETLIFY_ for browser access -->
<!-- Set in Dashboard > Environment Variables -->

<script>
  // These are available at build time
  const apiUrl = '${NETLIFY_API_URL}';
</script>
```

### Handle Secrets

```bash
# Use Netlify's secret management
# In Dashboard > Site Settings > Environment

# Mark sensitive variables as "Hidden"
# They will not be shown in the dashboard after saving

# For CLI
netlify env:set STRIPE_SECRET_KEY "sk_live_..." --context production
```

### Debug Missing Variables

```javascript
// Debug endpoint
exports.handler = async () => {
  const vars = {
    DATABASE_URL: !!process.env.DATABASE_URL,
    API_KEY: !!process.env.API_KEY,
    NODE_ENV: process.env.NODE_ENV,
  };

  return {
    statusCode: 200,
    body: JSON.stringify(vars),
  };
};
```

### Fix Variable Context Issues

```bash
# Variables can be scoped to:
# - All (default)
# - Production only
# - Deploy Preview only
# - Branch deploy only

# Make sure your variable is set for the right context
netlify env:set API_KEY "prod-key" --context production
netlify env:set API_KEY "test-key" --context deploy-preview
```

## Common Mistakes

- Setting variables only for production but testing on deploy previews
- Not re-deploying after adding environment variables
- Using NODE_ENV instead of checking Netlify-specific variables
- Not prefixing browser-accessible variables with NETLIFY_
- Exposing secrets in client-side code

## Related Pages

- [Netlify Functions Error]({{< relref "/tools/netlify/netlify-functions-error" >}}) — Serverless function error
- [Netlify Build Error]({{< relref "/tools/netlify/netlify-build-error" >}}) — Build failed
