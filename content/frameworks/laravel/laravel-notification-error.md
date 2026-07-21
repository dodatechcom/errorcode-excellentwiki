---
title: "[Solution] Laravel Notification Error"
description: "Notification not sending."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Notification not sending.

## Common Causes

Not configured.

## How to Fix

Add Notifiable.

## Example

```php
class User extends Authenticatable { use Notifiable; }
User::find(1)->notify(new Shipped($o));
```
