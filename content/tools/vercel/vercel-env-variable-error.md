---
title: "[Solution] Vercel Environment Variable Error"
description: "Fix Vercel environment variable errors when variables are missing or misconfigured."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel Environment Variable Error

Vercel environment variables are not available or cause errors.

```
ReferenceError: process.env.VARIABLE_NAME is not defined
```

## Common Causes

- Variable not set in Vercel Dashboard
- Variable not available in current environment
- Variable name typo
- Variable scoped to wrong environment
- Sensitive variable exposed client-side

## How to Fix

### Set Variables in Dashboard

```bash
# Via CLI
vercel env add VARIABLE_NAME production
vercel env add VARIABLE_NAME preview
vercel env add VARIABLE_NAME development

# List all variables
vercel env ls
```

### Use NEXT_PUBLIC_ for Client Access

```bash
# Public variable (accessible client-side)
NEXT_PUBLIC_API_URL=https://api.example.com

# Server-only variable
DATABASE_URL=postgres://...
```

### Configure in vercel.json

```json
{
  "build": {
    "env": {
      "NODE_ENV": "production"
    }
  }
}
```

### Scope to Environments

```bash
# Development only
vercel env add DEBUG development
# Value: true

# Production only
vercel env add API_KEY production
# Value: secret-key
```

### Check Variable Availability

```javascript
// Server-side
console.log(process.env.DATABASE_URL);

// Client-side (only NEXT_PUBLIC_ vars)
console.log(process.env.NEXT_PUBLIC_API_URL);
```

## Examples

```bash
# Import variables from .env file
vercel env pull .env.local

# Override variable for specific deploy
vercel deploy --env MY_VAR=value
```
