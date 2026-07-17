---
title: "Horizon worker error"
description: "Laravel Horizon throws worker errors when queue workers fail to process jobs"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["horizon", "queue", "worker", "redis", "supervisor"]
weight: 5
---

This error occurs when Laravel Horizon queue workers encounter fatal errors or excessive memory usage, causing the worker process to terminate unexpectedly.

## Common Causes

- Worker memory limit exceeded during long-running jobs
- Redis connection lost while processing jobs
- Job class references a missing or renamed class
- PHP fatal error in job handler
- Supervisor configuration too restrictive

## How to Fix

1. Configure Horizon worker settings in `config/horizon.php`:

```php
'environments' => [
    'production' => [
        'supervisor-1' => [
            'maxProcesses' => 10,
            'balanceMaxShift' => 1,
            'balanceCooldown' => 3,
            'tries' => 3,
            'timeout' => 60,
            'memory' => 512,
        ],
    ],
],
```

2. Implement the `ShouldRetry` interface for failed jobs:

```php
class ProcessPayment implements ShouldQueue, ShouldRetry
{
    public int $tries = 3;

    public function backoff(): array
    {
        return [10, 30, 60]; // seconds between retries
    }

    public function retryUntil(): Carbon
    {
        return now()->addMinutes(5);
    }

    public function handle(): void
    {
        // Payment processing logic
    }
}
```

3. Monitor Horizon via the dashboard:

```bash
# Access the Horizon dashboard at /horizon
# Check worker status and failed jobs
php artisan horizon:status
```

## Examples

```php
// Worker crashes when job references deleted class
// Horizon marks the job as failed
dispatch(new OldJobThatWasDeleted());
// Error: Class 'App\Jobs\OldJobThatWasDeleted' not found
```

## Related Errors

- [Queue error]({{< relref "/frameworks/laravel/queue-error" >}})
- [Schedule error]({{< relref "/frameworks/laravel/schedule-error" >}})
