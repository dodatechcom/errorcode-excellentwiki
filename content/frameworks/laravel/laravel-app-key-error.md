---
title: "[Solution] Laravel APP_KEY Not Set Error"
description: "Fix the missing APP_KEY error in Laravel. Resolve RuntimeException no application encryption key configured."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error appears when Laravel tries to use encryption, sessions, or signed URLs but the `APP_KEY` environment variable is empty or missing entirely.

## Common Causes

- `.env` file does not contain `APP_KEY` at all
- Environment variables are not loaded (wrong `APP_ENV` or dotenv misconfigured)
- Deployment pipeline does not copy `.env` or inject secrets
- Docker container does not mount `.env` correctly
- Key was removed accidentally during a merge conflict

## How to Fix

1. Run the artisan key generator:

```bash
php artisan key:generate
```

2. If artisan fails, generate manually and add to `.env`:

```bash
php -r "echo 'APP_KEY=base64:' . base64_encode(random_bytes(32)) . PHP_EOL;" >> .env
```

3. Verify the environment is loading `.env`:

```php
// bootstrap/app.php or config/app.php
'value' => env('APP_KEY'),
```

4. For Docker, ensure `.env` is mounted or passed as an environment variable:

```yaml
services:
  app:
    env_file:
      - .env
```

## Examples

```php
// Session encryption fails without APP_KEY
session(['key' => 'value']);
// RuntimeException: No application encryption key has been specified.

// Signed URLs also require a valid key
$url = URL::temporarySignedRoute('download', now()->addMinutes(30), ['id' => 1]);
// MissingAppKeyException
```
