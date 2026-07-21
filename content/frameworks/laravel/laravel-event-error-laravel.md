---
title: "[Solution] laravel Event Error Laravel"
description: "Event not dispatching."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Event not dispatching.

## Common Causes

Not firing.

## How to Fix

Dispatch event.

## Example

```php
Event::new OrderShipped($order)->dispatch();
// or event(new OrderShipped($order));
```
