---
title: "[Solution] PHP SYMFONY_MESSENGER_ERROR — Message Dispatch/Handling Failed"
description: "Fix PHP SYMFONY_MESSENGER_ERROR by checking transport config, verifying handlers, and handling message failures. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 115
---

# PHP SYMFONY_MESSENGER_ERROR — Message Dispatch/Handling Failed

A message dispatch or handling error occurred in Symfony Messenger. This happens when transport configuration is wrong, message handlers are missing, or message processing fails.

## Common Causes

```php
// Message class missing required properties
class SendEmailMessage
{
    // no constructor, no way to set recipient
    public $to; // uninitialized property
}
```

```php
// Handler class not registered as a service
class SendEmailHandler
{
    // not tagged with messenger.message_handler in services.yaml
}
```

```php
// Transport not configured
# config/packages/messenger.yaml
framework:
    messenger:
        transports:
            async: 'doctrine://default' // database driver not available
```

```php
// Handler method signature doesn't match message class
class OrderHandler implements MessageHandlerInterface
{
    public function __invoke(SendEmailMessage $msg): void // wrong message type
    {
        // handles SendEmailMessage but dispatched OrderMessage
    }
}
```

```php
// Failed transport not configured
# messages go to failed transport but failed_transport doesn't exist
```

## How to Fix

### Fix 1: Configure Messenger Transport

```yaml
# config/packages/messenger.yaml
framework:
    messenger:
        transports:
            async:
                dsn: '%env(MESSENGER_TRANSPORT_DSN)%'
                retry_strategy:
                    max_retries: 3
                    delay: 1000
                    multiplier: 2
                    max_delay: 0
                failure_transport: failed

            failed:
                dsn: 'doctrine://default?queue_name=failed'

            sync: 'sync://'

        failure_transport: failed

        routing:
            'App\Message\SendEmailMessage': async
            'App\Message\OrderMessage': async
            'App\Message\NotificationMessage': sync
```

### Fix 2: Create Proper Message and Handler

```php
// src/Message/SendEmailMessage.php
namespace App\Message;

final class SendEmailMessage
{
    public function __construct(
        private readonly string $to,
        private readonly string $subject,
        private readonly string $body,
    ) {
    }

    public function getTo(): string
    {
        return $this->to;
    }

    public function getSubject(): string
    {
        return $this->subject;
    }

    public function getBody(): string
    {
        return $this->body;
    }
}
```

```php
// src/MessageHandler/SendEmailHandler.php
namespace App\MessageHandler;

use App\Message\SendEmailMessage;
use Symfony\Component\Messenger\Attribute\AsMessageHandler;
use Symfony\Component\Messenger\Exception\UnrecoverableMessageException;

#[AsMessageHandler]
class SendEmailHandler
{
    public function __construct(
        private readonly MailerInterface $mailer,
    ) {
    }

    public function __invoke(SendEmailMessage $message): void
    {
        try {
            $email = (new Email())
                ->from('noreply@example.com')
                ->to($message->getTo())
                ->subject($message->getSubject())
                ->text($message->getBody());

            $this->mailer->send($email);
        } catch (\Throwable $e) {
            throw new UnrecoverableMessageException(
                'Failed to send email: ' . $e->getMessage()
            );
        }
    }
}
```

### Fix 3: Handle Failed Messages

```bash
# List failed messages
php bin/console messenger:failed:show

# Retry failed messages
php bin/console messenger:failed:retry

# Delete failed messages
php bin/console messenger:failed:purge

# View message details
php bin/console messenger:failed:show -vv

# Consume messages with timeout
php bin/console messenger:consume async --time-limit=300

# Consume specific transports
php bin/console messenger:consume async failed
```

### Fix 4: Debug Messenger Configuration

```bash
# Debug messenger setup
php bin/console debug:messenger

# List available transports
php bin/console messenger:consume --list-transports

# Check failed messages
php bin/console messenger:failed:show
```

```php
// Dispatch with stamps for debugging
use Symfony\Component\Messenger\Stamp\DispatchAfterCurrentBusStamp;
use Symfony\Component\Messenger\Stamp\BusStamp;

$message = new SendEmailMessage('user@example.com', 'Test', 'Hello');
$bus->dispatch($message, [
    new DispatchAfterCurrentBusStamp(),
]);

// In handler, add delay stamp
use Symfony\Component\Messenger\Stamp\DelayStamp;

$bus->dispatch($message, [
    new DelayStamp(5000), // delay 5 seconds
]);

// Use sender stamp to route to specific transport
use Symfony\Component\Messenger\Stamp\SenderStamp;

$bus->dispatch($message, [
    new SenderStamp('async'),
]);
```

## Examples

```php
// Complete messenger setup example
// Controller dispatching messages
class OrderController extends AbstractController
{
    #[Route('/order', name: 'order_new')]
    public function new(Request $request, MessageBusInterface $bus): Response
    {
        $order = new Order();
        $form = $this->createForm(OrderType::class, $order);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $em = $this->getDoctrine()->getManager();
            $em->persist($order);
            $em->flush();

            // Dispatch async message
            $bus->dispatch(new ProcessOrderMessage($order->getId()));

            $this->addFlash('success', 'Order placed! Processing...');
            return $this->redirectToRoute('order_show', ['id' => $order->getId()]);
        }

        return $this->render('order/new.html.twig', [
            'form' => $form->createView(),
        ]);
    }
}
```

## Related Errors

- [Symfony Security Error](/languages/php/symfony-security-error)
- [Symfony Route Error](/languages/php/symfony-route-error)
- [Laravel Queue Error](/languages/php/laravel-queue)
- [Doctrine Connection Error](/languages/php/doctrine-connection)
