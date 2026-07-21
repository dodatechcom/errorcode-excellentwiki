---
title: "[Solution] Laravel Job Stuck in Processing"
description: "Fix Laravel jobs stuck in processing state in the jobs table. Resolve unprocessing queue jobs in database driver."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when jobs remain in the `jobs` or `failed_jobs` table in a "reserved" or "processing" state indefinitely, never completing or failing properly.

## Common Causes

- Queue worker crashed or was killed mid-job (SIGKILL, OOM)
- `$timeout` is too low and job is killed before update
- `reserve` lock not released due to DB connection drop
- Job throws an uncaught exception that bypasses the failure handler
- Multiple workers processing the same queue without `--force`

## How to Fix

1. Release stuck jobs manually:

```php
use Illuminate\Support\Facades\DB;

DB::table('jobs')
    ->where('queue', 'default')
    ->where('reserved_at', '<', now()->subMinutes(5))
    ->update(['reserved_at' => null, 'attempts' => 0]);
```

2. Set appropriate `retryAfter` in the queue config:

```php
'redis' => [
    'driver' => 'redis',
    'retry_after' => 120,
],
```

3. Use the `failing` callback to track stuck jobs:

```php
Queue::failing(function ($connection, $job, $exception) {
    Log::warning('Job stuck: ' . $job->getRawBody());
});
```

4. Monitor with Horizon or artisan:

```bash
php artisan queue:work --max-jobs=1000 --max-time=3600
```

## Examples

```php
// Worker killed by OOM leaves job stuck
// The reserved_at timestamp is set but never cleared
Artisan::call('queue:work', [
    '--once' => true,
    '--queue' => 'default',
]);

// Manually retry stuck jobs
$stuckJobs = DB::table('jobs')
    ->where('reserved_at', '<', now()->subMinutes(10))
    ->get();

foreach ($stuckJobs as $job) {
    DB::table('jobs')->where('id', $job->id)->update([
        'reserved_at' => null,
        'attempts' => 0,
    ]);
}
```
