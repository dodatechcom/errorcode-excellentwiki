---
title: "[Solution] PHP SYMFONY_EVENT_DISPATCHER_ERROR — Symfony EventDispatcher Error"
description: "Fix PHP Symfony EventDispatcher errors. Check listener definition, verify event name, and handle propagation. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 128
---

# PHP SYMFONY_EVENT_DISPATCHER_ERROR — Symfony EventDispatcher Error

The Symfony EventDispatcher encountered an error while dispatching an event. This error occurs when listeners are not registered correctly, event names are wrong, listener methods do not exist, or event propagation stopping causes issues.

## Common Causes

### Listener method does not exist

```php
<?php
class UserEventListener
{
    // Symfony looks for methods named after the event
    // e.g., onUserCreated or __invoke
    public function handleUserCreated(UserCreatedEvent $event)
    {
        // This method won't be called unless properly configured
    }
}
// LogicException: Method "handleUserCreated" does not exist
?>
```

### Wrong event name in listener registration

```php
<?php
// services.yaml
App\EventListener\UserEventListener:
    tags:
        - { name: kernel.event_listener, event: user.created }  # wrong event name
        # Should be: App\Event\UserCreatedEvent
?>
```

### Stopping propagation prematurely

```php
<?php
class UserEventListener
{
    public function onUserCreated(UserCreatedEvent $event): void
    {
        $event->stopPropagation();
        // Other listeners will not be notified
    }
}
?>
```

### Type error in listener

```php
<?php
class UserEventListener
{
    public function onUserCreated(UserCreatedEvent $event): void
    {
        $user = $event->getUser();
        $user->nonexistentMethod(); // calling undefined method
        // Error propagates through event system
    }
}
?>
```

### Missing event class

```php
<?php
$dispatcher->dispatch(new NonExistentEvent(), 'user.created');
// Class 'NonExistentEvent' not found
?>
```

## How to Fix

### Fix 1: Define Listener Methods Correctly

```php
<?php
namespace App\EventListener;

use App\Event\UserCreatedEvent;

class UserEventListener
{
    // Method 1: Named method matching event class
    public function onUserCreated(UserCreatedEvent $event): void
    {
        $user = $event->getUser();
        // Handle user created
    }

    // Method 2: __invoke for single-event listeners
    public function __invoke(UserCreatedEvent $event): void
    {
        $user = $event->getUser();
        // Handle user created
    }
}
?>
```

### Fix 2: Register Listeners Correctly

```php
<?php
// Method 1: YAML configuration
// services.yaml
services:
    App\EventListener\UserEventListener:
        tags:
            - { name: kernel.event_listener, event: App\Event\UserCreatedEvent }
            - { name: kernel.event_listener, event: App\Event\UserDeletedEvent }

    # Method 2: PHP attribute (Symfony 6.1+)
    // App/EventListener/UserEventListener.php
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    class UserEventListener implements EventSubscriberInterface
    {
        public static function getSubscribedEvents(): array
        {
            return [
                UserCreatedEvent::class => ['onUserCreated', 10], // priority 10
                UserDeletedEvent::class => 'onUserDeleted',
            ];
        }

        public function onUserCreated(UserCreatedEvent $event): void {}
        public function onUserDeleted(UserDeletedEvent $event): void {}
    }

    // Method 3: Inline registration
    $dispatcher->addListener(UserCreatedEvent::class, function (UserCreatedEvent $event) {
        // Handle event
    }, 10);
?>
```

### Fix 3: Handle Event Propagation

```php
<?php
class UserEventListener
{
    public function onUserCreated(UserCreatedEvent $event): void
    {
        // Do not stop propagation unless absolutely necessary
        $event->getDispatcher()->dispatch(
            new UserWelcomeEvent($event->getUser()),
            UserWelcomeEvent::class
        );
    }

    public function onUserCreatedHighPriority(UserCreatedEvent $event): void
    {
        // Only stop propagation for security checks
        if (!$event->getUser()->isEmailVerified()) {
            $event->stopPropagation();
            throw new \RuntimeException('Email not verified');
        }
    }
}
?>
```

### Fix 4: Create Proper Event Classes

```php
<?php
namespace App\Event;

use Symfony\Contracts\EventDispatcher\Event;

class UserCreatedEvent extends Event
{
    public function __construct(
        private readonly User $user,
        private readonly array $context = [],
    ) {}

    public function getUser(): User
    {
        return $this->user;
    }

    public function getContext(): array
    {
        return $this->context;
    }
}

// Dispatch the event
$event = new UserCreatedEvent($user, ['source' => 'registration']);
$dispatcher->dispatch($event, UserCreatedEvent::class);
?>
```

### Fix 5: Debug Event Listeners

```php
<?php
// List all registered events
// php bin/console debug:event-dispatcher

// List listeners for specific event
// php bin/console debug:event-dispatcher App\Event\UserCreatedEvent

// In code
$dispatcher = $container->get('event_dispatcher');
$listeners = $dispatcher->getListeners(UserCreatedEvent::class);
foreach ($listeners as $listener) {
    echo get_class($listener) . PHP_EOL;
}

// Check if propagation was stopped
$event = new UserCreatedEvent($user);
$dispatcher->dispatch($event, UserCreatedEvent::class);
echo "Propagation stopped: " . ($event->isPropagationStopped() ? 'yes' : 'no') . PHP_EOL;
?>
```

## Examples

### Complete Event System

```php
<?php
// Event class
namespace App\Event;

class OrderPlacedEvent
{
    public function __construct(
        private readonly Order $order,
    ) {}

    public function getOrder(): Order
    {
        return $this->order;
    }
}

// Listener
namespace App\EventListener;

use App\Event\OrderPlacedEvent;

class OrderNotificationListener
{
    public function __construct(
        private readonly MailerInterface $mailer,
        private readonly LoggerInterface $logger,
    ) {}

    public function onOrderPlaced(OrderPlacedEvent $event): void
    {
        $order = $event->getOrder();
        $this->logger->info("Order placed: {$order->getId()}");
        // Send email notification
    }
}

// services.yaml
App\EventListener\OrderNotificationListener:
    tags:
        - { name: kernel.event_listener, event: App\Event\OrderPlacedEvent, priority: 0 }
?>
```

## Related Errors

- [Symfony HttpKernel Error]({{< relref "/languages/php/symfony-http-kernel-error" >}})
- [Symfony Messenger Error]({{< relref "/languages/php/symfony-messenger-error" >}})
- [Symfony DependencyInjection Error]({{< relref "/languages/php/symfony-dependency-injection-error" >}})
