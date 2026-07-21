---
title: "[Solution] laravel Observer Error Laravel"
description: "Observer not working."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Observer not working.

## Common Causes

Not registered.

## How to Fix

Register observer.

## Example

```php
protected $observe = [\n    Order::class => OrderObserver::class,\n];
```
