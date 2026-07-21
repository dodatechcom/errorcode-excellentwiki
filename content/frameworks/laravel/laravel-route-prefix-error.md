---
title: "[Solution] Laravel Route Prefix Error"
description: "Route prefix not applying."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Route prefix not applying.

## Common Causes

Wrong registration.

## How to Fix

Set prefix.

## Example

```php
Route::prefix('api')->group(function () { ... });
```
