---
title: "[Solution] laravel Service Provider Error"
description: "Service not registering."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Service not registering.

## Common Causes

Not in provider.

## How to Fix

Register in provider.

## Example

```php
public function register() {
    $this->app->singleton(MyService::class, function ($app) {
        return new MyService();
    });
}
```
