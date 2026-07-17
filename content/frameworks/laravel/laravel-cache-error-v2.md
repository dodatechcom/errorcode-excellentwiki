---
title: "Cache driver error"
description: "Laravel cache operations fail when the configured cache driver is unavailable or misconfigured"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Laravel cannot read from or write to the configured cache store. The cache facade throws an exception when the underlying driver (Redis, Memcached, database) is unreachable or misconfigured.

## Common Causes

- Cache driver server is down or unreachable
- Wrong driver configured in `.env`
- Redis memory limit exceeded
- Memcached connection failure
- Cache store permissions issue

## How to Fix

1. Check cache configuration in `.env`:

```
CACHE_DRIVER=redis

REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379
```

2. Use a fallback cache driver:

```php
use Illuminate\Support\Facades\Cache;

function cacheWithFallback(string $key, callable $callback, int $ttl = 60)
{
    try {
        return Cache::remember($key, $ttl, $callback);
    } catch (\Exception $e) {
        Log::warning('Cache driver failed, using array: ' . $e->getMessage());
        return $callback();
    }
}
```

3. Switch to the array driver for local development if needed:

```
CACHE_DRIVER=array
```

4. Register a custom cache failure handler:

```php
use Illuminate\Support\Facades\Cache;

Cache::macro('rememberSafe', function ($key, $ttl, $callback) {
    try {
        return Cache::remember($key, $ttl, $callback);
    } catch (\Exception $e) {
        report($e);
        return $callback();
    }
});
```

## Examples

```php
// Cache usage that handles driver failure gracefully
try {
    $users = Cache::remember('active-users', 600, function () {
        return User::where('active', true)->get();
    });
} catch (\Exception $e) {
    $users = User::where('active', true)->get();
    Log::error('Cache failed: ' . $e->getMessage());
}
```

## Related Errors

- [Queue worker connection error]({{< relref "/frameworks/laravel/laravel-queue-error-v2" >}})
- [Service container resolution error]({{< relref "/frameworks/laravel/laravel-service-container-v2" >}})
