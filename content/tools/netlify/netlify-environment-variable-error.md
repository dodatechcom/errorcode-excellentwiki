---
title: "[Solution] Netlify Environment Variable Error"
description: "Fix Netlify environment variable errors when variables are not available during builds or functions."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

# Netlify Environment Variable Error

Netlify environment variables are not accessible during builds or function execution.

```
Environment variable not found: API_KEY
```

## Common Causes

- Variable not set in Netlify Dashboard
- Variable scoped to wrong deploy context
- Variable name misspelled
- Variable not available in function runtime
- Secrets not properly encrypted

## How to Fix

### Set Variables in Dashboard

```
1. Go to Site settings > Environment variables
2. Add variable with key and value
3. Select scope: All, Build, Runtime, or specific context
```

### Configure Variables in netlify.toml

```toml
[build.environment]
  NODE_VERSION = "18"
  NEXT_TELEMETRY_DISABLED = "1"
```

### Scope Variables to Context

```toml
[context.production.environment]
  NODE_ENV = "production"

[context.deploy-preview.environment]
  NODE_ENV = "staging"
```

### Access Variables in Functions

```javascript
// Variables available via process.env
exports.handler = async (event) => {
  const apiKey = process.env.API_KEY;
  if (!apiKey) {
    return { statusCode: 500, body: "API_KEY not set" };
  }
};
```

### Check Variable Availability

```bash
# In build script
echo "NODE_VERSION: $NODE_VERSION"
echo "API_KEY: ${API_KEY:-NOT SET}"
```

### Use Secrets Properly

```toml
# For sensitive values, use Netlify Dashboard
# Settings > Environment variables > Secrets
# Values are encrypted and hidden after save
```

## Examples

```toml
# Complete environment configuration
[build.environment]
  NODE_VERSION = "20"
  npm_config_production = "false"

[context.production.environment]
  DATABASE_URL = "postgres://..."

[context.deploy-preview.environment]
  DATABASE_URL = "postgres://..."
  DEBUG = "true"
```
