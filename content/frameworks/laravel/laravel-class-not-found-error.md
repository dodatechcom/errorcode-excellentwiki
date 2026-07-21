---
title: "[Solution] Laravel Class Not Found Error"
description: "PHP class not found."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

PHP class not found.

## Common Causes

Wrong namespace.

## How to Fix

Import correctly.

## Example

```php
use App\Models\User;
$user = User::find(1);
```
