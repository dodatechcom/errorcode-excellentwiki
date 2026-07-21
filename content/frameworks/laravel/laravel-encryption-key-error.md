---
title: "[Solution] Laravel Encryption Key Error"
description: "Fix Laravel RuntimeException wrong key length for encryption. Resolve invalid APP_KEY configuration."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when the `APP_KEY` in your `.env` file is missing, malformed, or not the correct length for the encryption driver being used.

## Common Causes

- `APP_KEY` is not set in `.env` after fresh installation
- Key was generated with a different cipher than the one configured in `config/app.php`
- `.env` file was overwritten during deployment
- Key contains extra whitespace or newline characters
- Base64-encoded key is missing the `base64:` prefix

## How to Fix

1. Generate a new application key:

```bash
php artisan key:generate
```

2. Verify the key in `.env` starts with `base64:`:

```text
APP_KEY=base64:8f3qxP+u1P3q2mN...long-string...==
```

3. Ensure the cipher in `config/app.php` matches the key format:

```php
'cipher' => 'AES-256-CBC',
```

4. Clear all caches after changing the key:

```bash
php artisan cache:clear
php artisan config:clear
```

## Examples

```php
// Encrypting data will fail without a valid key
$encrypted = Crypt::encrypt('sensitive-data');
// RuntimeException: No encryption keys have been configured.

// The key is used by default in session and cookie drivers
// A bad key will cause session/auth failures across the app
```
