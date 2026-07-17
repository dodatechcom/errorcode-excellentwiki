---
title: "[Solution] Heroku Config Var Not Set Error — Fix Environment Variables"
description: "Fix Heroku config var errors. Resolve missing environment variables, config set issues, and secret management problems."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
weight: 4
---

A Heroku config var not set error occurs when your application tries to access an environment variable that is not configured in Heroku's config vars. Unlike local development, Heroku does not use .env files.

## What This Error Means

```
app[web.1]: Error: DATABASE_URL must be set
app[web.1]:     at Object.connect (/app/src/database.js:5:15)
```

Your application expects an environment variable that is not defined in Heroku's config vars.

## Why It Happens

- The config var was never set
- The var was set but the dyno was not restarted
- The var name has a typo
- Using .env file locally but not setting vars in Heroku
- Config vars were accidentally deleted

## How to Fix It

### Set Config Vars

```bash
# Set a single var
heroku config:set DATABASE_URL="postgresql://..."

# Set multiple vars
heroku config:set DATABASE_URL="postgresql://..." API_KEY="secret"

# Set from .env file
cat .env | xargs -L 1 heroku config:set
```

### List Current Config Vars

```bash
# Show all config vars
heroku config

# Show specific var
heroku config:get DATABASE_URL

# Show as JSON
heroku config --json
```

### Remove a Config Var

```bash
heroku config:unset DATABASE_URL
```

### Check in Dashboard

```bash
# In Heroku Dashboard:
# Settings > Config Vars > Reveal Config Vars
```

### Handle Different Environments

```bash
# Use Heroku Pipelines for staging/production
# Set vars per app

# Staging
heroku config:set DATABASE_URL="postgresql://staging-..." --app my-app-staging

# Production
heroku config:set DATABASE_URL="postgresql://prod-..." --app my-app-prod
```

### Verify Config in App

```javascript
// Check config vars on startup
const required = ['DATABASE_URL', 'API_KEY', 'SECRET'];
const missing = required.filter(key => !process.env[key]);

if (missing.length > 0) {
  console.error('Missing config vars:', missing.join(', '));
  process.exit(1);
}
```

### Use Config File

```javascript
// config.js
const config = {
  databaseUrl: process.env.DATABASE_URL,
  apiKey: process.env.API_KEY,
  secret: process.env.SECRET,
};

// Validate all required vars
Object.entries(config).forEach(([key, value]) => {
  if (!value) {
    throw new Error(`Missing config var: ${key.toUpperCase()}`);
  }
});

module.exports = config;
```

## Common Mistakes

- Relying on .env files which do not work on Heroku
- Not restarting dynos after setting config vars
- Setting vars on wrong app in pipeline
- Exposing secrets in git history
- Not rotating secrets periodically

## Related Pages

- [Heroku Build Error]({{< relref "/tools/heroku/heroku-build-error" >}}) — Build failed / compilation error
- [Heroku Dyno Error]({{< relref "/tools/heroku/heroku-dyno-error" >}}) — R14 Memory quota exceeded
