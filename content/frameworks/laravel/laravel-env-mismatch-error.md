---
title: "[Solution] Laravel Environment Mismatch Error"
description: "Fix Laravel config cache env mismatch error. Resolve APP_ENV not matching cached configuration in Laravel."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when cached configuration files contain values from a different environment than the one currently running.

## Common Causes

- `config:cache` was run in production but `.env` changed to development
- `.env.production` overrides values not reflected in cache
- Deployment runs `config:cache` before setting correct `APP_ENV`
- Docker container has stale cached config from build stage
- `.env` file does not match `APP_ENV` value

## How to Fix

1. Clear all cached configs:

```bash
php artisan config:clear
php artisan cache:clear
```

2. Re-cache with the correct environment:

```bash
APP_ENV=production php artisan config:cache
```

3. Never cache config during development:

```php
// Only cache in production deploy scripts
if (env('APP_ENV') === 'production') {
    Artisan::call('config:cache');
}
```

4. Use `env()` helper carefully with cached config:

```php
// BAD: env() returns null after config:cache
'value' => env('SOME_VALUE', 'default'),

// GOOD: use config files instead
// config/app.php
'value' => env('SOME_VALUE', 'default'),
// Then use config('app.value')
```

## Examples

```php
// Cache created in production, then env switches to development
php artisan config:cache  // cached production values
// Change APP_ENV=development
php artisan tinker
// config('app.debug') still returns true (production cached value)

// Fix:
php artisan config:clear
php artisan config:cache  // re-cache current env
```
