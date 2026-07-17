---
title: "Queue worker connection error"
description: "Laravel queue worker fails to connect to the queue broker such as Redis, SQS, or database"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when the Laravel queue worker cannot establish or maintain a connection to the configured queue broker. The worker process throws a connection exception and stops processing jobs.

## Common Causes

- Queue broker (Redis, SQS, database) is down or unreachable
- Incorrect connection credentials in `.env`
- Redis max connections exceeded
- Worker lost connection due to timeout
- Dusk or Horizon misconfiguration

## How to Fix

1. Verify queue configuration in `.env`:

```
QUEUE_CONNECTION=redis

REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379
```

2. Add retry logic with connection handling:

```php
use Illuminate\Queue\RedisQueue;

class RetryableRedisQueue extends RedisQueue
{
    public function push($job, $data = '', $queue = null)
    {
        try {
            return parent::push($job, $data, $queue);
        } catch (\Exception $e) {
            Log::error('Queue connection failed, retrying...', ['error' => $e->getMessage()]);
            sleep(5);
            return parent::push($job, $data, $queue);
        }
    }
}
```

3. Run the worker with connection retry and timeout options:

```bash
php artisan queue:work --sleep=3 --tries=3 --max-time=3600
```

4. Use Horizon to manage worker processes with auto-restart:

```bash
php artisan horizon:terminate
php artisan horizon
```

## Examples

```php
// Dispatching a job with retry on failure
dispatch(new SendEmailJob($user))
    ->onQueue('emails')
    ->afterCommit();

// Customizing connection per job
class ProcessPayment implements ShouldQueue
{
    public $connection = 'redis';
    public $queue = 'payments';
}
```

## Related Errors

- [Mail transport error]({{< relref "/frameworks/laravel/laravel-mail-error-v2" >}})
- [Cache driver error]({{< relref "/frameworks/laravel/laravel-cache-error-v2" >}})
