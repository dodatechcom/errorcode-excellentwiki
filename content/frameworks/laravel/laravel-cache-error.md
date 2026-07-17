---
title: "Cache store not found error"
description: "Laravel throws InvalidArgumentException when the configured cache store is not defined"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["cache", "store", "redis", "memcached", "configuration"]
weight: 5
---

This error occurs when Laravel tries to use a cache store that is not configured in `config/cache.php` or the `.env` file. It throws `InvalidArgumentException: Cache store [X] is not defined`.

## Common Causes

- `CACHE_STORE` in `.env` references a store not defined in `config/cache.php`
- Custom cache store not registered in the configuration file
- Cache driver package not installed (e.g., `predis/predis` for Redis)
- Environment mismatch between development and production configs

## How to Fix

1. Verify the `CACHE_STORE` environment variable:

```env
CACHE_STORE=redis
# or
CACHE_STORE=file
# or
CACHE_STORE=database
```

2. Add a custom cache store in `config/cache.php`:

```php
'stores' => [
    'redis' => [
        'driver' => 'redis',
        'connection' => 'cache',
        'lock_connection' => 'default',
    ],

    'custom' => [
        'driver' => 'redis',
        'connection' => 'custom_cache',
    ],
],
```

3. Use try-catch when accessing cache:

```php
use Illuminate\Support\Facades\Cache;

try {
    $value = Cache::store('redis')->get('key');
} catch (\InvalidArgumentException $e) {
    Log::warning('Cache store not available: ' . $e->getMessage());
    $value = null;
}
```

## Examples

```php
// .env has CACHE_STORE=memcached but memcached is not configured
$value = Cache::get('user:1');
// InvalidArgumentException: Cache store [memcached] is not defined
```

## Related Errors

- [Queue error]({{< relref "/frameworks/laravel/queue-error" >}})
- [Mail error]({{< relref "/frameworks/laravel/mail-error" >}})
