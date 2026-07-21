---
title: "[Solution] Laravel Rate Limiter Error"
description: "Rate limiting not working."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Rate limiting not working.

## Common Causes

Not defined.

## How to Fix

Define.

## Example

```php
RateLimiter::for('api', fn(R $r) => Limit::perMinute(60));
```
