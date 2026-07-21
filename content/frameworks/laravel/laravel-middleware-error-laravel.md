---
title: "[Solution] Laravel Middleware Error Laravel"
description: "Middleware not executing."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Middleware not executing.

## Common Causes

Not registered.

## How to Fix

Register in kernel.

## Example

```php
protected $middleware = [\n    \App\Http\Middleware\TrimStrings::class,\n];
```
