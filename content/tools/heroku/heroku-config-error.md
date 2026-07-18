---
title: "[Solution] Heroku Config Var Not Set or Invalid — How to Fix"
description: "Fix Heroku config var errors by checking missing environment variables, validating syntax, updating settings with the CLI, and ensuring config vars propagate to all dynos."
tools: ["heroku"]
error-types: ["config-error"]
severities: ["error"]
weight: 5
comments: true
---

A Heroku config var error occurs when your application tries to access an environment variable that is not set, has an invalid value, or has not propagated to running dynos. Config vars are Heroku's mechanism for managing environment-specific configuration.

## What This Error Means

Config vars in Heroku are key-value pairs that are set on your application and exposed as environment variables to all running dynos. When you set a config var, Heroku restarts all dynos to pick up the new value. If the config var is missing, has the wrong value, or the dyno restarts have not completed, your application may fail to start or behave incorrectly.

Errors can occur during initial deployment (missing required vars), after updating vars (stale dynos), or when the config var value contains invalid characters or exceeds size limits.

## Why It Happens

- A required config var was never set on the Heroku application
- The config var name has a typo or does not match what the code expects
- Config var values contain special characters that are not properly escaped
- The config var value exceeds the 32KB size limit
- Dyno restarts have not completed after config var changes
- The `.env` file in development has variables that are not set in production
- Config vars are set on the wrong Heroku app (staging vs production)
- The application uses `process.env` or `ENV` incorrectly

## Common Error Messages

```
 ▸    Missing required config var DATABASE_URL
# or
 ▸    Config var DATABASE_URL is not a valid URL
# or
 ▸    Error: KEY=value pair is malformed
# or
 ▸    You must set the SECRET_KEY_BASE config var before deploying
```

## How to Fix It

### 1. List Current Config Vars

```bash
# List all config vars for the app
heroku config -a my-app

# Get a specific config var
heroku config:get DATABASE_URL -a my-app

# Get config vars in shell-exportable format
heroku config -s -a my-app
```

### 2. Set or Update Config Vars

```bash
# Set a single config var
heroku config:set SECRET_KEY_BASE=abc123 -a my-app

# Set multiple config vars
heroku config:set \
    DB_POOL=10 \
    MAX_UPLOAD_SIZE=50MB \
    CACHE_TTL=3600 \
    -a my-app

# Set with special characters (use quotes)
heroku config:set DATABASE_URL="postgres://user:pass@host:5432/db" -a my-app
```

### 3. Remove Config Vars

```bash
# Remove a config var
heroku config:unset OBSOLETE_KEY -a my-app

# Remove multiple config vars
heroku config:unset OLD_KEY1 OLD_KEY2 -a my-app
```

### 4. Use .env File for Local Development

```bash
# Create a .env file matching Heroku config
echo "DATABASE_URL=postgres://localhost:5432/dev_db" > .env
echo "SECRET_KEY_BASE=local_dev_key" >> .env
echo "REDIS_URL=redis://localhost:6379" >> .env

# Use heroku local to run with .env
heroku local

# Verify .env is in .gitignore
echo ".env" >> .gitignore
```

### 5. Validate Config Var Values

```python
import os

# Add validation at application startup
required_vars = [
    'DATABASE_URL',
    'SECRET_KEY_BASE',
    'REDIS_URL',
]

missing_vars = []
for var in required_vars:
    if not os.environ.get(var):
        missing_vars.append(var)

if missing_vars:
    raise RuntimeError(
        f"Missing required config vars: {', '.join(missing_vars)}"
    )
```

### 6. Check for Config Var Size Limits

```bash
# Config var values are limited to 32KB
# For large values, store them in a database or S3
# Check the size of a config var value:
heroku config:get LARGE_CONFIG -a my-app | wc -c
```

### 7. Force Dyno Restart for Config Var Propagation

```bash
# Config var changes automatically restart dynos
# But if dynos seem stale, force a restart:
heroku ps:restart -a my-app

# For review apps, recreate the app:
heroku review-app:destroy my-pr-42
heroku review-app:create my-pr-42
```

### 8. Set Config Vars from a File

```bash
# Export current config to a file
heroku config -s -a my-app > heroku-config.txt

# Edit the file, then re-import
# Delete all existing config vars first
heroku config:unset $(heroku config -s -a my-app | cut -d= -f1) -a my-app

# Set from file
xargs -a heroku-config.txt heroku config:set -a my-app
```

## Common Scenarios

### Missing DATABASE_URL on First Deploy

A developer deploys a Rails app to Heroku for the first time. The app fails to start because `DATABASE_URL` is not set. Heroku automatically sets `DATABASE_URL` when you provision a Heroku Postgres addon. Run `heroku addons:create heroku-postgresql:mini -a my-app` to fix it.

### Staging and Production Config Mismatch

A feature works in staging but fails in production because `STRIPE_API_KEY` is set in staging but not in production. Use Heroku Pipelines to promote config vars along with slug builds, or manually synchronize config vars across environments.

### Special Characters in Config Var Values

A config var `REDIS_PASSWORD` contains a `#` character. When the application reads it, the URL parsing truncates at the `#`. URL-encode special characters: heroku config:set REDIS_URL="redis://user:pass%23word@host:6379" -a my-app.

## Prevent It

- Use a startup validation script that checks all required config vars
- Maintain an `app.json` manifest file with required config vars documented
- Use Heroku Pipelines to promote config vars alongside releases
- Keep a `.env.example` file in version control as documentation
- Use Heroku's `heroku config:set` with shell-quoting for special characters
- Automate config var management with Heroku Platform API
- Set up monitoring to alert when critical config vars are missing
- Review config var values regularly and remove unused ones

## Related Pages

- [Heroku Release Error](/tools/heroku/heroku-release-error)
- [Heroku DB Error](/tools/heroku/heroku-db-error)
- [Heroku App Not Found](/tools/heroku/heroku-app-not-found)
