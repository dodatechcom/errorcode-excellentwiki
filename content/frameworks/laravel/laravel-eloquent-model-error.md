---
title: "[Solution] Laravel Eloquent Model Error"
description: "Model not found."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Model not found.

## Common Causes

Wrong table.

## How to Fix

Check table.

## Example

```php
class User extends Model { protected $table = 'users'; }
```
