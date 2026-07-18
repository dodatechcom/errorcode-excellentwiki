---
title: "[Solution] Vercel Environment Variable Not Available Error — How to Fix"
description: "Fix Vercel environment variable not available errors. Resolve missing env vars, build-time vs runtime issues, and scope configuration."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Vercel environment variable not available error occurs when your code references an environment variable that is not configured for the current deployment environment or scope. This causes `undefined` values or runtime crashes.

## What This Error Means

Vercel environment variables are scoped to specific environments (Development, Preview, Production) and can be configured at the account, project, or git branch level. When a variable is missing for a given scope, the application receives `undefined` instead of the expected value. Variables must be redeployed after being added or changed.

## Why It Happens

- The environment variable is configured for Production but not Preview
- A branch-specific environment variable does not match the current branch
- The variable was added after the deployment was built (requires redeploy)
- The variable name in code does not match the name in Vercel settings (case-sensitive)
- The variable is marked as encrypted but not properly decoded
- Build-time variables are not accessible at runtime or vice versa
- The variable contains special characters that break the shell
- The variable was accidentally deleted or renamed

## Common Error Messages

- `undefined` — The variable is not set for this environment
- `Environment variable not found` — Runtime code cannot access the variable
- `Missing env variable` — Build step fails due to missing variable
- `Cannot read properties of undefined` — Code tries to use undefined env value

## How to Fix It

### Configure Variables for All Environments

```bash
# In Vercel Dashboard: Settings > Environment Variables

# Set for all environments
DATABASE_URL=postgres://...
NEXT_PUBLIC_API_KEY=abc123

# Or use CLI
vercel env add DATABASE_URL

# Add for specific environment
vercel env add DATABASE_URL production
vercel env add DATABASE_URL preview
vercel env add DATABASE_URL development
```

### Check Variable Scope

```javascript
// Build-time variables (available during build)
process.env.DATABASE_URL       // Server only
process.env.API_SECRET         // Server only

// Client-side variables must be prefixed with NEXT_PUBLIC_
process.env.NEXT_PUBLIC_API_KEY  // Available in browser

// WRONG: Trying to use server variable on client
// This will be undefined in the browser
console.log(process.env.DATABASE_URL);

// RIGHT: Use the correct prefix
console.log(process.env.NEXT_PUBLIC_API_KEY);
```

### Handle Missing Variables Gracefully

```javascript
// WRONG: Throws if variable is undefined
const dbUrl = process.env.DATABASE_URL;
const connection = new Database(dbUrl); // Crashes if undefined

// RIGHT: Validate and fail gracefully
const dbUrl = process.env.DATABASE_URL;
if (!dbUrl) {
  throw new Error(
    'DATABASE_URL environment variable is required. ' +
    'Configure it in Vercel Dashboard > Settings > Environment Variables'
  );
}

// Or use a default for development
const dbUrl = process.env.DATABASE_URL || 'sqlite://local.db';
```

### Access Variables at Runtime

```javascript
// vercel.json — make variables available at runtime
{
  "env": {
    "DATABASE_URL": "@database-url"
  }
}

// For Next.js, use next.config.js for build-time variables
// next.config.js
module.exports = {
  env: {
    CUSTOM_VAR: process.env.CUSTOM_VAR,
  },
};

// Use VERCEL_ENV to detect the current environment
const isProduction = process.env.VERCEL_ENV === 'production';
const isPreview = process.env.VERCEL_ENV === 'preview';
const isDevelopment = process.env.VERCEL_ENV === 'development';
```

### Verify Variable Availability

```javascript
// Debug: list all available environment variables (server only)
export default function handler(req, res) {
  const envInfo = {
    DATABASE_URL: !!process.env.DATABASE_URL,
    API_SECRET: !!process.env.API_SECRET,
    NEXT_PUBLIC_API_KEY: !!process.env.NEXT_PUBLIC_API_KEY,
    NODE_ENV: process.env.NODE_ENV,
    VERCEL_ENV: process.env.VERCEL_ENV,
  };

  res.json(envInfo);
}
```

### Migrate Variables Between Environments

```bash
# Export variables from one environment
vercel env pull .env.local --environment=production

# Import to another environment
vercel env add DATABASE_URL preview < .env.local

# Or use the Vercel CLI to sync variables
vercel env pull .env.production --environment=production
vercel env push .env.production --environment=preview
```

### Handle Sensitive Variables

```bash
# In Vercel Dashboard: Settings > Environment Variables
# Click the eye icon next to a variable to mark it as sensitive
# Sensitive variables are:
# - Never exposed in build logs
# - Cannot be pulled via CLI
# - Encrypted at rest

# Use the "sensitive" flag when adding via CLI
vercel env add DATABASE_URL production --sensitive
```

## Common Scenarios

- **Preview deployment missing vars:** A preview deployment for a pull request does not have access to production-only environment variables, causing the API calls to fail.
- **Branch protection:** Environment variables configured for the `main` branch are not available in feature branch deployments.
- **Build vs runtime confusion:** A variable is set to "Available at Runtime" in Vercel settings, but the code accesses it during `next build`, where it is not available.

## Prevent It

1. Always configure environment variables for both Production and Preview scopes when setting up a new variable
2. Use `NEXT_PUBLIC_` prefix for any variable that needs to be available in client-side code
3. Add environment variable validation at application startup that fails fast with a clear error message

## Related Pages

- [Vercel Edge Config Error]({{< relref "/tools/vercel/vercel-edge-config-error" >}}) — Edge Config read error
- [Vercel Domain Error]({{< relref "/tools/vercel/vercel-domain-error" >}}) — Domain verification failed
