---
title: "[Solution] Laravel Model Cast Error"
description: "Casting not working."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Casting not working.

## Common Causes

Wrong type.

## How to Fix

Define casts.

## Example

```php
protected $casts = ['email_verified_at' => 'datetime', 'is_admin' => 'boolean'];
```
