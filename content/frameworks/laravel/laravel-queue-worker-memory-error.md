---
title: "[Solution] Laravel Queue Worker Out of Memory"
description: "Fix Laravel queue worker killed by OOM. Resolve memory limit exceeded error for Laravel queue workers."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when a Laravel queue worker process exceeds the system or PHP memory limit and is killed by the OS or PHP runtime.

## Common Causes

- Worker processes large collections without chunking
- Memory leak in long-running worker (accumulated Eloquent models)
- `$memory` limit on job is too low
- Worker runs indefinitely without restarting
- Large payload serialized in the queue

## How to Fix

1. Increase the worker memory limit:

```bash
php artisan queue:work --memory=512
```

2. Set memory on the job class:

```php
class GenerateReport implements ShouldQueue
{
    public int $memory = 256;
}
```

3. Use `chunk` to process large datasets:

```php
public function handle(): void
{
    User::chunk(200, function ($users) {
        foreach ($users as $user) {
            Notification::send($user, new MonthlyDigest());
        }
    });
}
```

4. Force periodic worker restarts:

```bash
php artisan queue:work --max-jobs=500 --max-time=3600
```

## Examples

```php
// Worker killed after processing 100k records in memory
$users = User::all(); // loads everything into memory
foreach ($users as $user) { ... }
// PHP Fatal error: Allowed memory size of 128M exhausted

// Fix: use cursor or chunk
$users = User::cursor(); // lazy collection
foreach ($users as $user) {
    $this->process($user); // memory stays low
}
```
