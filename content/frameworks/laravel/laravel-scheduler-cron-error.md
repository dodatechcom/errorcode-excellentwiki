---
title: "[Solution] Laravel Scheduler Cron Not Running Error"
description: "Fix Laravel scheduled tasks not executing. Resolve cron job not triggering artisan schedule:run commands."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when Laravel's task scheduler does not run because the server crontab is not configured or the cron entry is incorrect.

## Common Causes

- Server crontab does not have an entry for `schedule:run`
- Cron daemon is not installed or not running
- Wrong user runs the cron job (does not have access to the app)
- Path to `php` binary is incorrect in crontab
- Crontab entry has syntax errors

## How to Fix

1. Add the cron entry to the server:

```bash
* * * * * cd /path-to-your-project && php artisan schedule:run >> /dev/null 2>&1
```

2. Verify cron is running:

```bash
# Check cron service status
sudo systemctl status cron

# View crontab for the user
crontab -l
```

3. Use systemd as an alternative to cron:

```ini
# /etc/systemd/system/laravel-scheduler.service
[Unit]
Description=Laravel Scheduler

[Service]
User=www-data
WorkingDirectory=/var/www/html
ExecStart=/usr/bin/php artisan schedule:run --verbose --no-interaction

[Install]
WantedBy=multi-user.target
```

4. Test the scheduler manually:

```bash
php artisan schedule:run
```

## Examples

```php
// Define a scheduled task
$schedule->command('orders:process')->everyMinute();
$schedule->command('reports:generate')->dailyAt('02:00');
$schedule->command('cache:prune-stale-tags')->hourly();

// The cron entry must run every minute for Laravel to handle timing
// * * * * * php artisan schedule:run
```
