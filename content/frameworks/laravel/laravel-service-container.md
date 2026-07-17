---
title: "BindingResolutionException - service container"
description: "Laravel throws BindingResolutionException when the service container cannot resolve a dependency"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["service-container", "dependency-injection", "binding", "resolve", "ioc"]
weight: 5
---

This error occurs when Laravel's service container cannot resolve a class dependency during injection. It throws `Illuminate\Container\BindingResolutionException` when the container has no binding or cannot auto-wire the requested type.

## Common Causes

- Interface not bound to a concrete implementation
- Circular dependency between two services
- Class requires primitive values without explicit binding
- Constructor has required parameters with no defaults
- Trying to resolve an abstract class directly

## How to Fix

1. Bind interfaces to implementations in `AppServiceProvider`:

```php
use App\Contracts\PaymentGateway;
use App\Services\StripePaymentGateway;

public function register(): void
{
    $this->app->bind(PaymentGateway::class, StripePaymentGateway::class);
}
```

2. Resolve circular dependencies using interfaces:

```php
// Bad — circular dependency
class ServiceA {
    public function __construct(ServiceB $b) {}
}
class ServiceB {
    public function __construct(ServiceA $a) {}
}

// Fix — use an interface
class ServiceB {
    public function __construct(ServiceAInterface $a) {}
}
```

3. Use `when->needs->give` for contextual binding:

```php
$this->app->when(MailchimpNotification::class)
    ->needs(MailTransport::class)
    ->give(SmtpMailTransport::class);
```

## Examples

```php
// No binding registered for the interface
$payment = app(PaymentGateway::class);
// BindingResolutionException: Target [App\Contracts\PaymentGateway] is not instantiable
```

## Related Errors

- [Bean not found (Spring)]({{< relref "/frameworks/spring/bean-not-found" >}})
- [Validation error]({{< relref "/frameworks/laravel/validation-error2" >}})
