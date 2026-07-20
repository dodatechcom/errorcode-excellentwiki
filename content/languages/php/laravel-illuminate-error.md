---
title: "[Solution] PHP LARAVEL_ILLUMINATE_ERROR — Container/Dependency Injection Failed"
description: "Fix PHP LARAVEL_ILLUMINATE_ERROR by checking binding definitions, verifying class existence, and handling circular dependencies. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 124
---

# PHP LARAVEL_ILLUMINATE_ERROR — Container/Dependency Injection Failed

A container or dependency injection error occurred in Laravel. This happens when a class cannot be resolved, bindings are circular, or required dependencies are missing.

## Common Causes

```php
// Circular dependency
class A
{
    public function __construct(B $b) { } // A depends on B
}

class B
{
    public function __construct(A $a) { } // B depends on A — infinite loop
}
```

```php
// Class not found or autoloaded
class UserController extends Controller
{
    public function __construct(NonExistentService $service) { }
}
```

```php
// Interface not bound in container
interface PaymentGateway { }

class StripeGateway implements PaymentGateway { }

class OrderController extends Controller
{
    public function __construct(PaymentGateway $gateway) { }
    // PaymentGateway interface not bound
}
```

```php
// Wrong binding syntax
$this->app->bind('PaymentGateway', function () {
    return new StripeGateway($wrongDependency); // $wrongDependency undefined
});
```

```php
// Trying to inject non-instantiable class
$this->app->make(SomeAbstractClass::class); // abstract class can't be resolved
```

## How to Fix

### Fix 1: Check Binding Definitions

```php
// app/Providers/AppServiceProvider.php
namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use App\Services\PaymentGateway;
use App\Services\StripeGateway;
use App\Services\PayPalGateway;

class AppServiceProvider extends ServiceProvider
{
    public function register(): void
    {
        // Bind interface to concrete implementation
        $this->app->bind(PaymentGateway::class, StripeGateway::class);

        // Or with factory closure
        $this->app->bind(PaymentGateway::class, function ($app) {
            return new StripeGateway(
                $app->make(StripeApiKey::class)
            );
        });

        // Singleton binding (one instance)
        $this->app->singleton(PaymentGateway::class, StripeGateway::class);

        // Contextual binding
        $this->app->when(OrderController::class)
            ->needs(PaymentGateway::class)
            ->give(StripeGateway::class);

        $this->app->when(RefundController::class)
            ->needs(PaymentGateway::class)
            ->give(StripeGateway::class);
    }

    public function boot(): void
    {
        // ...
    }
}
```

### Fix 2: Verify Class Exists and is Instantiable

```php
// Check if class exists before using
if (class_exists(App\Services\PaymentGateway::class)) {
    $gateway = app(PaymentGateway::class);
}

// Use abstract type hint with concrete binding
$this->app->bind('payment', function ($app) {
    return $app->make(StripeGateway::class);
});

// Use app()->make() with error handling
try {
    $service = app(NonExistentService::class);
} catch (\Illuminate\Contracts\Container\BindingNotFoundException $e) {
    Log::error("Service not found: {$e->getMessage()}");
}

// In controller constructor
class UserController extends Controller
{
    public function __construct(
        protected UserService $userService,
        protected MailerInterface $mailer,
    ) {
        // These must be resolvable
    }
}
```

### Fix 3: Handle Circular Dependencies

```php
// Option A: Use interface to break cycle
interface NotificationSenderInterface
{
    public function send(User $user, string $message): void;
}

class EmailSender implements NotificationSenderInterface
{
    public function __construct(
        protected MailerInterface $mailer,
    ) {}

    public function send(User $user, string $message): void
    {
        $this->mailer->raw($message, function ($email) use ($user) {
            $email->to($user->email);
        });
    }
}

// Bind interface, not concrete class
$this->app->bind(NotificationSenderInterface::class, EmailSender::class);
```

```php
// Option B: Use setter injection
class OrderService
{
    protected $notificationSender;

    public function setNotificationSender(NotificationSenderInterface $sender): void
    {
        $this->notificationSender = $sender;
    }

    public function processOrder(Order $order): void
    {
        // Use $this->notificationSender
    }
}

// Or use contextual binding
$this->app->when(OrderService::class)
    ->needs(NotificationSenderInterface::class)
    ->give(function ($app) {
        return $app->make(EmailSender::class);
    });
```

### Fix 4: Resolve Dependencies Manually

```php
// Use app() helper
$userService = app(UserService::class);

// With parameters
$service = app(MailService::class, ['driver' => 'smtp']);

// Use container directly
$service = $this->app->make(UserService::class);

// Resolve from method
$gateway = resolve(PaymentGateway::class);

// Check if binding exists
if ($this->app->bound(PaymentGateway::class)) {
    $gateway = $this->app->make(PaymentGateway::class);
}

// Use when/needs for contextual binding
$this->app->when(ReportController::class)
    ->needs(ReportFormatter::class)
    ->give(PdfFormatter::class);

$this->app->when(EmailController::class)
    ->needs(ReportFormatter::class)
    ->give(HtmlFormatter::class);
```

## Examples

```php
// Complete dependency injection example
// app/Services/UserService.php
namespace App\Services;

class UserService
{
    public function __construct(
        protected UserRepository $userRepository,
        protected MailerInterface $mailer,
        protected CacheInterface $cache,
    ) {}

    public function getUser(int $id): ?User
    {
        return $this->cache->remember("user.{$id}", 3600, function () use ($id) {
            return $this->userRepository->find($id);
        });
    }

    public function createUser(array $data): User
    {
        $user = $this->userRepository->create($data);
        $this->mailer->to($user->email)->send(new WelcomeMail($user));
        return $user;
    }
}

// Bind in AppServiceProvider
$this->app->bind(UserRepositoryInterface::class, EloquentUserRepository::class);
$this->app->bind(MailerInterface::class, MailManager::class);

// In controller — auto-resolved
class UserController extends Controller
{
    public function __construct(
        protected UserService $userService,
    ) {}

    public function show(int $id)
    {
        $user = $this->userService->getUser($id);
        return view('users.show', compact('user'));
    }
}
```

## Related Errors

- [Laravel Model Not Found](/languages/php/laravel-model-not-found)
- [Laravel Route Not Found](/languages/php/laravel-route-not-found)
- [Symfony Route Error](/languages/php/symfony-route-error)
- [PHP Fatal Error](/languages/php/fatal-error)
