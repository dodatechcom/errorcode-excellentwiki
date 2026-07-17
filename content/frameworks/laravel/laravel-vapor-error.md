---
title: "Vapor deployment error"
description: "Laravel Vapor throws deployment errors when deploying the application to AWS Lambda"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["vapor", "deployment", "aws", "lambda", "serverless"]
weight: 5
---

This error occurs when Laravel Vapor fails during deployment to AWS Lambda. It can be triggered by configuration issues, asset compilation failures, or Lambda function constraints.

## Common Causes

- `vapor.yml` misconfigured or missing required settings
- Asset compilation fails during the build phase
- Lambda function exceeds memory or timeout limits
- Environment variables not properly set in Vapor
- Artifact size exceeds Lambda deployment package limit

## How to Fix

1. Verify `vapor.yml` configuration:

```yaml
id: your-project-id
name: your-project-name
environments:
    production:
        memory: 1024
        cli-memory: 512
        timeout: 30
        runtime: php-8.2
        build:
            - 'npm ci && npm run build'
            - 'php artisan config:cache'
            - 'php artisan route:cache'
```

2. Check deployment logs:

```bash
# View deployment status
vapor deploy production

# Check logs for errors
vapor logs production --since=5m
```

3. Optimize build artifacts to stay under Lambda limits:

```bash
# In your build script
npm ci --production
composer install --no-dev --optimize-autoloader
php artisan icons:cache
php artisan view:cache
```

## Examples

```yaml
# Common error: artifact exceeds 250MB limit
build:
    - 'npm ci && npm run build'  # node_modules too large

# Fix: exclude dev dependencies
build:
    - 'npm ci --production && npm run build'
```

## Related Errors

- [Octane error]({{< relref "/frameworks/laravel/octane-error" >}})
- [Sail error]({{< relref "/frameworks/laravel/sail-error" >}})
