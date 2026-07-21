---
title: "[Solution] Laravel Job Timeout Error"
description: "Fix Laravel job has been attempted too many times or timed out. Resolve queue job timeout configuration."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error is thrown when a queued job exceeds the configured `$timeout` value and is killed by the queue worker before completing.

## Common Causes

- Job performs a long-running HTTP request or database query
- `$timeout` value on the job class is too low
- Queue worker `--timeout` flag is lower than the job timeout
- Deadlock or infinite loop inside the job
- External API is slow or unresponsive

## How to Fix

1. Increase the timeout on the job class:

```php
class ProcessLargeExport implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public int $timeout = 300; // 5 minutes
}
```

2. Ensure the worker timeout is at least as long as the job timeout:

```bash
php artisan queue:work --timeout=300
```

3. Break long operations into smaller chunks:

```php
public function handle(): void
{
    $chunks = Order::where('status', 'pending')->chunk(100, function ($orders) {
        foreach ($orders as $order) {
            $this->processOrder($order);
        }
    });
}
```

4. Use `retryOn` for transient failures:

```php
public int $tries = 3;
public int $backoff = 60;
```

## Examples

```php
// Worker kills job after 60s default timeout
class ExportReports implements ShouldQueue
{
    public int $timeout = 15;

    public function handle(): void
    {
        // This takes 20+ seconds to complete
        $data = ExternalApi::fetchAllRecords(); // times out
    }
}
// Symfony\\Component\\Process\\Exception\\ProcessTimedOutException
```
