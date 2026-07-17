---
title: "ScheduleTaskFailedException"
description: "Laravel throws ScheduleTaskFailedException when a scheduled task fails during execution"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["scheduler", "cron", "task", "command", "failed"]
weight: 5
---

This error occurs when a Laravel scheduled task throws an exception during execution. The scheduler catches the exception and reports it via the configured failure reporting channel.

## Common Causes

- Scheduled command throws an uncaught exception
- Database connection lost during task execution
- Task depends on a service that is unavailable
- File or resource not accessible from the scheduler context
- Permission issues when running as cron job

## How to Fix

1. Wrap scheduled task logic in try-catch:

```php
class SendWeeklyReport extends Command
{
    protected $signature = 'report:weekly';

    public function handle(): int
    {
        try {
            $users = User::where('active', true)->get();

            foreach ($users as $user) {
                Mail::to($user)->send(new WeeklyReport($user));
            }

            return self::SUCCESS;
        } catch (\Exception $e) {
            $this->error('Report failed: ' . $e->getMessage());
            Log::error('Weekly report failed', ['exception' => $e]);
            return self::FAILURE;
        }
    }
}
```

2. Configure failure notifications in `Console/Kernel.php`:

```php
protected function schedule(Schedule $schedule): void
{
    $schedule->command('report:weekly')
        ->daily()
        ->appendOutputTo(storage_path('logs/scheduler.log'));
}
```

3. Use `onFailure` callback in the schedule:

```php
$schedule->command('report:weekly')
    ->daily()
    ->onFailure(function () {
        Log::error('Scheduled task failed');
    });
```

## Examples

```php
// Kernel.php
$schedule->command('orders:process')->everyFiveMinutes();
// ScheduleTaskFailedException if database is unreachable
```

## Related Errors

- [Queue error]({{< relref "/frameworks/laravel/queue-error" >}})
- [Horizon error]({{< relref "/frameworks/laravel/horizon-error" >}})
