---
title: "[Solution] laravel Task Scheduler Error"
description: "Scheduled task not running."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Scheduled task not running.

## Common Causes

Cron not set.

## How to Fix

Add cron entry.

## Example

```php
$schedule->command('inspire')->hourly();
// Cron: * * * * * php artisan schedule:run
```
