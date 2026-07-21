---
title: "[Solution] Laravel Queue Worker Error"
description: "Queue worker not processing."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Queue worker not processing.

## Common Causes

Not running.

## How to Fix

Start worker.

## Example

```bash
php artisan queue:work --tries=3
```
