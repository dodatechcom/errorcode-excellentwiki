---
title: "[Solution] laravel Route Group Error"
description: "Route group middleware not applying."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Route group middleware not applying.

## Common Causes

Wrong syntax.

## How to Fix

Use group correctly.

## Example

```php
Route::middleware(['auth'])->group(function () {
    Route::get('/dashboard', [DashController::class, 'index']);
});
```
