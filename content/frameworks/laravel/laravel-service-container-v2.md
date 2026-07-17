---
title: "Service container resolution error"
description: "Laravel throws BindingResolutionException when the service container cannot resolve a class or interface"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Laravel's service container cannot resolve a class, interface, or abstract type. It throws `Illuminate\Contracts\Container\BindingResolutionException` when dependencies are missing or unresolvable.

## Common Causes

- Class depends on an interface that is not bound in the container
- Circular dependency between two or more classes
- Missing autoloading for the class
- Constructor parameter is not type-hinted
- Package not registered in the service provider

## How to Fix

1. Bind interfaces to their implementations in a service provider:

```php
use App\Contracts\UserRepositoryInterface;
use App\Repositories\DatabaseUserRepository;

class AppServiceProvider extends ServiceProvider
{
    public function register(): void
    {
        $this->app->bind(UserRepositoryInterface::class, DatabaseUserRepository::class);
    }
}
```

2. Use `make()` with error handling for optional dependencies:

```php
try {
    $service = app()->make(PaymentGateway::class);
} catch (\Illuminate\Contracts\Container\BindingResolutionException $e) {
    Log::error('Could not resolve service: ' . $e->getMessage());
    $service = new OfflinePaymentGateway();
}
```

3. Resolve circular dependencies using a proxy or event:

```php
// Instead of circular dependency, use events
class OrderService
{
    public function create(array $data)
    {
        $order = Order::create($data);
        event(new OrderCreated($order));
        return $order;
    }
}
```

4. Verify class autoloading with Composer:

```bash
composer dump-autoload
```

## Examples

```php
// Binding in AppServiceProvider
$this->app->singleton(CacheManager::class, function ($app) {
    return new CustomCacheManager($app['config']);
});

// Resolving from the container
$cache = app()->make(CacheManager::class);

// Using the container helper
$service = resolve(PaymentGateway::class);
```

## Related Errors

- [Route not defined error]({{< relref "/frameworks/laravel/laravel-route-not-found-v2" >}})
- [Cache driver error]({{< relref "/frameworks/laravel/laravel-cache-error-v2" >}})
