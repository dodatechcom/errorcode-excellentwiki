---
title: "[Solution] Laravel Service Provider Bind Error"
description: "Fix Laravel target class does not exist or binding not found. Resolve service container binding resolution errors."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when the service container tries to resolve a class that has not been bound, or when a binding reference is incorrect.

## Common Causes

- Interface bound to a concrete class that does not exist
- Alias registered under a name that conflicts with another binding
- Provider registers bindings after they are needed (boot order issue)
- Circular dependency between two services
- Typo in the binding key or class name

## How to Fix

1. Register bindings in a service provider:

```php
namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use App\Contracts\PaymentGateway;
use App\Services\StripeGateway;

class PaymentServiceProvider extends ServiceProvider
{
    public function register(): void
    {
        $this->app->bind(PaymentGateway::class, StripeGateway::class);
    }
}
```

2. Use `singleton` for shared instances:

```php
$this->app->singleton(PaymentGateway::class, function ($app) {
    return new StripeGateway(config('services.stripe.key'));
});
```

3. Resolve with type-hint injection:

```php
class CheckoutController extends Controller
{
    public function __construct(private PaymentGateway $gateway) {}
}
```

4. Check for circular dependencies:

```php
// Bad: A depends on B and B depends on A
$this->app->bind(ServiceA::class, fn ($app) => new ServiceA($app->make(ServiceB::class)));
$this->app->bind(ServiceB::class, fn ($app) => new ServiceB($app->make(ServiceA::class)));
```

## Examples

```php
// Resolving an unbound interface
app()->make(PaymentGateway::class);
// BindingNotFoundException: Target [App\Contracts\PaymentGateway] is not instantiable.

// Circular dependency detected
// RuntimeException: Maximum function nesting level reached
```
