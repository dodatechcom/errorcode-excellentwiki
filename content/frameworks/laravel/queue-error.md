---
title: "Queue job failed"
description: "Laravel queue worker encounters an unhandled exception while processing a queued job"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["queue", "job", "worker", "failed", "horizon"]
weight: 5
---

This error occurs when a Laravel queue worker encounters an unhandled exception while processing a job. The job may be retried, marked as failed, or retried indefinitely depending on configuration.

## Common Causes

- Exception thrown inside the job's `handle()` method
- Job references a model or service that is no longer available
- External service (API, database) is unavailable when job executes
- Job exceeds the configured timeout

## How to Fix

1. Implement `failed()` method in the job class:

```php
class ProcessOrder implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public function handle(OrderService $service)
    {
        $service->process($this->orderId);
    }

    public function failed(Throwable $exception)
    {
        \Log::error("Job failed: {$exception->getMessage()}");
    }
}
```

2. Configure retry behavior:

```php
class ProcessOrder implements ShouldQueue
{
    public int $tries = 3;
    public int $timeout = 120;

    public function backoff()
    {
        return [30, 60, 120]; // seconds between retries
    }
}
```

3. Move failed jobs to the failed_jobs table for later inspection:

```php
// config/queue.php
'failed' => [
    'driver' => 'database-uuids',
    'database' => 'mysql',
    'table' => 'failed_jobs',
],
```

4. Retry a failed job manually:

```php
php artisan queue:retry <job-uuid>
# or retry all failed jobs
php artisan queue:retry all
```

## Examples

```php
// Job that fails due to missing service
class SendEmail implements ShouldQueue
{
    public function handle()
    {
        Mail::to('user@example.com')->send(new WelcomeMail());
        // Throws exception if mail server is down
    }
}
```

```text
Illuminate\Queue\MaxAttemptsExceededException: App\Jobs\SendEmail has been attempted 3 times
```

## Related Errors

- [Queue job failed]({{< relref "/frameworks/laravel/queue-error" >}})
