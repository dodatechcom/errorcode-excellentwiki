---
title: "[Solution] laravel Rate Limit Error Laravel"
description: "Rate limit not applied."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Rate limit not applied.

## Common Causes

Not defined.

## How to Fix

Define limiter.

## Example

```php
RateLimiter::for('api', fn(Request $r) => Limit::perMinute(60));
```
