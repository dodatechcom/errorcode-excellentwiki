---
title: "[Solution] PHP LARAVEL_QUEUE_WORKER_ERROR — Laravel Queue Worker Error"
description: "Fix PHP Laravel Queue worker errors. Check job class, verify connection, and handle failures. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 123
---

# PHP LARAVEL_QUEUE_WORKER_ERROR — Laravel Queue Worker Error

A Laravel queue worker encountered an error while processing a job. This error occurs when the job class is missing, the queue connection is unavailable, serialization fails, or the job exceeds memory/time limits.

## Common Causes

### Job class not found

```php
<?php
// Dispatching job that doesn't exist
SendEmailJob::dispatch($user);
// LogicException: Unable to locate job class "App\Jobs\SendEmailJob"
?>
```

### Queue connection unavailable

```php
<?php
// .env: QUEUE_CONNECTION=redis
// But Redis server is down
dispatch(new ProcessOrder($order));
// Symfony\Component\Mailer\Exception\TransportExceptionInterface: Redis connection refused
?>
```

### Job exceeds memory limit

```php
<?php
class ProcessLargeReport implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public function handle(): void
    {
        $data = Report::all(); // loads millions of rows into memory
        // Worker killed: allowed memory size exhausted
    }
}
?>
```

### Job throws unhandled exception

```php
<?php
class SendNotification implements ShouldQueue
{
    public function handle(): void
    {
        $this->mailer->send(); // throws exception
        // Job fails, retried repeatedly
    }
}
?>
```

### Failed job not configured

```php
<?php
// config/queue.php — failed_jobs_table migration not run
// queue:work tries to log failure but table doesn't exist
dispatch(new ImportantJob($data));
// Worker crashes when trying to log failure
?>
```

## How to Fix

### Fix 1: Ensure Job Class Exists and Is Discoverable

```php
<?php
namespace App\Jobs;

use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Queue\SerializesModels;

class ProcessOrder implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public int $tries = 3;
    public int $timeout = 60;

    public function __construct(
        public Order $order
    ) {}

    public function handle(): void
    {
        $this->order->update(['status' => 'processing']);
        // Process order logic
    }

    public function failed(\Throwable $exception): void
    {
        Log::error("ProcessOrder failed for order {$this->order->id}: " . $exception->getMessage());
    }
}
?>
```

### Fix 2: Verify Queue Connection

```php
<?php
// Check queue connection in config/queue.php
'connections' => [
    'redis' => [
        'driver' => 'redis',
        'connection' => 'default',
        'queue' => env('REDIS_QUEUE', 'default'),
        'retry_after' => 90,
        'block_for' => null,
    ],
    'database' => [
        'driver' => 'database',
        'table' => 'jobs',
        'queue' => 'default',
        'retry_after' => 90,
    ],
],

// Test connection
use Illuminate\Support\Facades\Queue;
$queue = Queue::connection('redis');
echo "Queue connection OK" . PHP_EOL;
?>
```

### Fix 3: Handle Memory and Timeout Limits

```php
<?php
class ProcessLargeReport implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public int $timeout = 300; // 5 minutes
    public int $tries = 3;
    public int $maxExceptions = 1;

    public function handle(): void
    {
        // Process in chunks instead of loading all into memory
        Report::query()
            ->chunk(1000, function ($reports) {
                foreach ($reports as $report) {
                    $this->processReport($report);
                }

                // Free memory
                gc_collect_cycles();
            });
    }

    private function processReport(Report $report): void
    {
        // Process individual report
    }
}
?>
```

### Fix 4: Handle Job Failures

```php
<?php
class SendNotification implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    public int $tries = 3;
    public int $backoff = [30, 60, 120]; // seconds between retries

    public function handle(): void
    {
        $this->mailer->to($this->user->email)->send(new OrderShipped($this->order));
    }

    public function failed(\Throwable $exception): void
    {
        // Called when job fails permanently
        Log::error("Notification failed for user {$this->user->id}: " . $exception->getMessage());

        $this->user->update(['notification_failed' => true]);
    }
}

// Handle failed jobs globally
// app/Providers/AppServiceProvider.php
use Illuminate\Queue\Events\JobFailed;

public function boot(): void
{
    Queue::failing(function (JobFailed $event) {
        Log::critical("Job failed: " . $event->job->resolveName());
    });
}
?>
```

### Fix 5: Run Failed Jobs Migration

```php
<?php
// Create failed_jobs table
// Run: php artisan queue:failed-table
// Run: php artisan migrate

// In config/queue.php, set failed driver
'failed' => [
    'driver' => env('QUEUE_FAILED_DRIVER', 'database-uuids'),
    'database' => env('DB_CONNECTION', 'mysql'),
    'table' => 'failed_jobs',
],

// Retry failed jobs
// artisan command: php artisan queue:retry --all
// Or retry specific ID: php artisan queue:retry {id}
?>
```

## Examples

### Complete Queue Configuration

```php
<?php
// .env
QUEUE_CONNECTION=redis
REDIS_QUEUE=default
REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379

// Dispatch with delay
dispatch(new ProcessOrder($order))->delay(now()->addMinutes(5));

// Dispatch to specific queue
dispatch(new SendEmail($user))->onQueue('emails');

// Dispatch to specific connection
dispatch(new SyncInventory($product))->onConnection('database');

// Prevent duplication
dispatch(new SyncInventory($product))->unique('sync_inventory');
?>
```

## Related Errors

- [Redis Connection Error]({{< relref "/languages/php/redis-connection-error" >}})
- [Laravel Model Not Found]({{< relref "/languages/php/laravel-model-not-found" >}})
- [Symfony Messenger Error]({{< relref "/languages/php/symfony-messenger-error" >}})
