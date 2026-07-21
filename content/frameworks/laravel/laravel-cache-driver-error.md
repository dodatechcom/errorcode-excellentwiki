---
title: "[Solution] Laravel Cache Driver Error"
description: "Fix Laravel cache driver not supported or cache store not configured. Resolve invalid cache configuration errors."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when the configured cache driver is unavailable, misconfigured, or the required PHP extension is missing.

## Common Causes

- `CACHE_DRIVER` in `.env` references a store not defined in `config/cache.php`
- Required PHP extension is not installed (e.g., `ext-redis`, `ext-memcached`)
- Redis or Memcached server is not running
- Cache prefix contains invalid characters
- APCu extension not loaded when using `apc` driver

## How to Fix

1. Verify the cache driver in `.env`:

```text
CACHE_DRIVER=file
```

2. For Redis, ensure the extension is installed:

```bash
composer require predis/predis
# or install phpredis extension
```

3. Check `config/cache.php` defines the store:

```php
'stores' => [
    'redis' => [
        'driver' => 'redis',
        'connection' => 'cache',
        'prefix' => env('CACHE_PREFIX', 'laravel_cache'),
    ],
],
```

4. Test the cache connection:

```php
Cache::store('redis')->put('test', 'value', 60);
$value = Cache::store('redis')->get('test');
```

## Examples

```php
// Using a driver that is not installed
config(['cache.store' => 'memcached']);
Cache::put('key', 'value', 60);
// RuntimeException: Memcached extension not installed

// Switch to file driver as fallback
config(['cache.store' => 'file']);
Cache::put('key', 'value', 60); // works
```
