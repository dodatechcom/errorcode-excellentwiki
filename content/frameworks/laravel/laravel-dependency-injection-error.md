---
title: "[Solution] Laravel Dependency Injection Error"
description: "Fix Laravel target class does not exist in constructor injection. Resolve autowiring failures in Laravel."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when Laravel's service container cannot automatically resolve a class dependency required by a constructor or method.

## Common Causes

- Class has type-hinted dependencies that are not concrete classes
- Abstract class or interface not bound in the container
- Constructor has a scalar type that cannot be auto-resolved
- Class is not namespaced correctly or autoloading fails
- Self-referencing dependency creates infinite recursion

## How to Fix

1. Bind abstract types to concrete implementations:

```php
$this->app->bind(Mailer::class, MailgunMailer::class);
```

2. Use constructor injection with concrete classes:

```php
class OrderController extends Controller
{
    public function __construct(
        private OrderService $orderService,
        private LoggerInterface $logger
    ) {}
}
```

3. Use `when` for contextual binding:

```php
$this->app->when(MailController::class)
    ->needs(Mailer::class)
    ->give(MailgunMailer::class);

$this->app->when(NotificationController::class)
    ->needs(Mailer::class)
    ->give(SesMailer::class);
```

4. Add `make` fallback with default:

```php
$gateway = app()->makeWith(PaymentGateway::class, ['key' => config('stripe.key')]);
```

## Examples

```php
// Scalar type cannot be resolved automatically
class ReportController extends Controller
{
    public function __construct(private int $limit) {} // fails
}
// BindingResolutionException: Target [int] is not instantiable

// Fix by injecting via method
public function index(int $limit = 25) { ... }
```
