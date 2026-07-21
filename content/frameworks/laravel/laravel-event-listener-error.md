---
title: "[Solution] Laravel Event Listener Error"
description: "Event not triggering."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Event not triggering.

## Common Causes

Not registered.

## How to Fix

Register.

## Example

```php
protected $listen = [OrderShipped::class => [SendNotification::class]];
```
