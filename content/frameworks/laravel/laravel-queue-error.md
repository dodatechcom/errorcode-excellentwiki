---
title: "ConnectionFailedException - queue connection"
description: "Laravel throws ConnectionFailedException when the queue worker cannot connect to the queue driver"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["queue", "connection", "driver", "redis", "beanstalkd"]
weight: 5
---

This error occurs when Laravel's queue system cannot connect to the configured queue driver (Redis, SQS, Beanstalkd, etc.). It throws `Illuminate\Queue\ConnectionFailedException`.

## Common Causes

- Queue driver server (Redis, Beanstalkd) is not running
- Incorrect connection credentials in `.env`
- Connection timeout due to network issues
- Queue driver port is blocked by firewall
- Memory exhaustion on the queue server

## How to Fix

1. Verify queue configuration in `.env`:

```env
QUEUE_CONNECTION=redis

REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379
```

2. Test the queue connection:

```php
use Illuminate\Support\Facades\Queue;

try {
    Queue::push(new SendEmailJob($user));
    echo 'Job dispatched successfully';
} catch (\Illuminate\Queue\ConnectionFailedException $e) {
    Log::error('Queue connection failed: ' . $e->getMessage());
}
```

3. Use a fallback driver for critical jobs:

```php
class SendEmailJob implements ShouldQueue
{
    public function __construct(public User $user) {}

    public function handle(): void
    {
        Mail::to($this->user)->send(new WelcomeEmail());
    }

    public function failed(\Throwable $exception): void
    {
        // Called when all retry attempts are exhausted
        Log::error('Email job failed: ' . $exception->getMessage());
    }
}
```

## Examples

```php
// Dispatching to a Redis queue when Redis is down
dispatch(new ProcessOrder($order));
// ConnectionFailedException: Redis connection refused
```

## Related Errors

- [Mail error]({{< relref "/frameworks/laravel/mail-error" >}})
- [Cache error]({{< relref "/frameworks/laravel/cache-error" >}})
