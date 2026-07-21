---
title: "[Solution] Laravel Queue Job Error"
description: "Job not dispatching."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Job not dispatching.

## Common Causes

Queue not configured.

## How to Fix

Configure driver.

## Example

```php
QUEUE_CONNECTION=redis
Job::dispatch($d)->onQueue('emails');
```
