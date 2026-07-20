---
title: "[Solution] PHP SYMFONY_DEPENDENCY_INJECTION_ERROR — Symfony DI Container Error"
description: "Fix PHP Symfony DependencyInjection errors. Check service definitions, verify autowiring, and handle circular references. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 125
---

# PHP SYMFONY_DEPENDENCY_INJECTION_ERROR — Symfony DI Container Error

The Symfony dependency injection container failed to resolve a service. This error occurs when services are misconfigured, autowiring fails, circular references exist, or required parameters are missing.

## Common Causes

### Service not found in container

```php
<?php
// Trying to get undefined service
$container->get('app.nonexistent_service');
// Symfony\Component\DependencyInjection\Exception\ServiceNotFoundException
?>
```

### Autowiring cannot resolve type

```php
<?php
class UserController extends AbstractController
{
    public function __construct(
        private NonExistentService $service // no service implements this type
    ) {}
}
// Symfony\Component\DependencyInjection\Exception\AutowiringFailedException
?>
```

### Circular reference

```php
<?php
class ServiceA
{
    public function __construct(private ServiceB $b) {}
}

class ServiceB
{
    public function __construct(private ServiceA $a) {} // circular!
}
// ServiceCircularReferenceException
?>
```

### Missing required parameter

```php
<?php
// services.yaml
App\Service\Mailer:
    arguments:
        $apiKey: '%env(MAILER_API_KEY)%'  # env var not set
// EnvNotFoundException or RuntimeException
?>
```

### Wrong service ID

```php
<?php
// config/services.yaml
services:
    App\Service\UserService: ~

// In controller
$userService = $this->container->get('UserService'); // wrong ID, should be full class name
// ServiceNotFoundException
?>
```

## How to Fix

### Fix 1: Register Services Properly

Define services in YAML or PHP configuration.

```yaml
# config/services.yaml
services:
    _defaults:
        autowire: true
        autoconfigure: true
        public: false

    App\:
        resource: '../src/'
        exclude:
            - '../src/DependencyInjection/'
            - '../src/Entity/'
            - '../src/Kernel.php'

    App\Service\UserService:
        arguments:
            $mailer: '@mailer.mailer'
            $logger: '@logger'

    App\Service\ExternalApi:
        factory: ['@App\Factory\ApiFactory', 'create']
        arguments:
            $apiKey: '%env(EXTERNAL_API_KEY)%'
```

### Fix 2: Fix Autowiring Issues

```php
<?php
// Explicitly wire dependencies when autowiring fails
class UserController extends AbstractController
{
    public function __construct(
        private UserService $userService,
        private LoggerInterface $logger
    ) {}
}

// When a type has multiple implementations, use tagged services
// config/services.yaml
App\Service\NotificationInterface: ~
App\Service\EmailNotification:
    tags: ['app.notification']
    arguments:
        $mailer: '@mailer.mailer'
App\Service\SmsNotification:
    tags: ['app.notification']

// In code
use Symfony\Component\DependencyInjection\TaggedIterator;

class NotificationService
{
    public function __construct(
        private iterable $notifications // auto-injected with tagged services
    ) {}

    public function send(string $type, string $message): void
    {
        foreach ($this->notifications as $notification) {
            if ($notification->supports($type)) {
                $notification->send($message);
            }
        }
    }
}
?>
```

### Fix 3: Break Circular References

```php
<?php
// Use a proxy or lazy loading
class ServiceA
{
    private ?ServiceB $b = null;

    // Use setter injection to break cycle
    public function setServiceB(ServiceB $b): void
    {
        $this->b = $b;
    }
}

// Or use a proxy
use Symfony\Component\ProxyManager\Proxy\VirtualProxyInterface;

class ServiceA
{
    public function __construct(
        private \Closure $serviceBFactory // lazy instantiation
    ) {}

    public function getServiceB(): ServiceB
    {
        return ($this->serviceBFactory)();
    }
}

// Or use interface segregation
interface LoggerAwareInterface
{
    public function setLogger(LoggerInterface $logger): void;
}
?>
```

### Fix 4: Handle Missing Parameters

```php
<?php
// Use default values in services.yaml
App\Service\Mailer:
    arguments:
        $apiKey: '%env(default:default_key:MAILER_API_KEY)%'
        $timeout: '%env(int:MAILER_TIMEOUT:30)%'

// Validate parameters on boot
class AppExtension implements CompilerPassInterface
{
    public function process(ContainerBuilder $container): void
    {
        $apiKey = $container->getParameter('app.api_key');
        if (empty($apiKey)) {
            throw new \RuntimeException('app.api_key parameter is not configured');
        }
    }
}
?>
```

### Fix 5: Debug Container Services

```php
<?php
// List all registered services
$services = $container->getServiceIds();
sort($services);
foreach ($services as $serviceId) {
    echo $serviceId . PHP_EOL;
}

// Check if service exists
if ($container->has('App\Service\UserService')) {
    $service = $container->get('App\Service\UserService');
}

// Dump container in dev mode
// php bin/console debug:container
// php bin/console debug:container --tag=app.notification
// php bin/console debug:autowiring App\
?>
```

## Examples

### Complete Service Definition

```php
<?php
namespace App\Service;

use Psr\Log\LoggerInterface;

class OrderProcessor
{
    public function __construct(
        private readonly UserService $userService,
        private readonly PaymentGateway $paymentGateway,
        private readonly LoggerInterface $logger,
    ) {}

    public function process(array $orderData): Order
    {
        $this->logger->info('Processing order', ['data' => $orderData]);
        // Process order
    }
}

// config/services.yaml
App\Service\OrderProcessor:
    arguments:
        $userService: '@App\Service\UserService'
        $paymentGateway: '@App\Service\StripeGateway'
    tags: ['app.order_processor']
?>
```

## Related Errors

- [Symfony Console Error]({{< relref "/languages/php/symfony-console-error" >}})
- [Symfony HttpKernel Error]({{< relref "/languages/php/symfony-http-kernel-error" >}})
- [Symfony Messenger Error]({{< relref "/languages/php/symfony-messenger-error" >}})
