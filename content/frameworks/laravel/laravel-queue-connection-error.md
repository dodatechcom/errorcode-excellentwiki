---
title: "[Solution] Laravel Queue Connection Error"
description: "Fix Laravel failed to connect to queue connection errors. Resolve Redis or SQS queue driver connection issues."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when Laravel cannot establish a connection to the configured queue driver, such as Redis, SQS, or Beanstalkd.

## Common Causes

- Queue service is not running (Redis, Beanstalkd, SQS)
- Connection credentials in `config/queue.php` or `.env` are wrong
- Network firewall blocks the queue port
- `QUEUE_CONNECTION` in `.env` does not match an entry in `config/queue.php`
- Redis or SQS endpoint has changed after infrastructure update

## How to Fix

1. Verify your queue connection setting in `.env`:

```text
QUEUE_CONNECTION=redis
```

2. Test the Redis connection manually:

```bash
redis-cli ping
# Should return: PONG
```

3. For SQS, confirm credentials and region:

```text
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_DEFAULT_REGION=us-east-1
SQS_QUEUE=your-queue-name
```

4. Add a connection timeout in `config/queue.php`:

```php
'redis' => [
    'driver' => 'redis',
    'connection' => 'default',
    'queue' => env('REDIS_QUEUE', 'default'),
    'retry_after' => 90,
    'block_for' => null,
],
```

## Examples

```php
// Dispatching fails when queue connection is down
dispatch(new SendInvoice($invoice));
// Symfony\\Component\\Debug\\Exception\\FatalErrorException:
//   Redis::connect(): connect() failed: Connection refused

// Check the connection at runtime
if (Queue::connection()->ready()) {
    dispatch(new ProcessOrder($order));
}
```
