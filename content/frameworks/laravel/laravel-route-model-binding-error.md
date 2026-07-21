---
title: "[Solution] Laravel Route Model Binding Error"
description: "Route model binding not working."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Route model binding not working.

## Common Causes

Wrong parameter name.

## How to Fix

Match variable.

## Example

```php
Route::get('/users/{user}', [UserController::class, 'show']);
```
