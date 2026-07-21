---
title: "[Solution] Laravel Route Parameter Not Provided Error"
description: "Fix Laravel missing required route parameter or type mismatch. Resolve route parameter binding failures in Laravel."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when a named route requires parameters that are not supplied, or when the parameter type does not match the expected type.

## Common Causes

- `route()` helper called without required parameters
- Route defined with typed parameters (e.g., `{id:int}`) receiving wrong type
- Route model binding fails because the record does not exist
- Optional parameter `?` suffix missing causing required param to be null
- Redirect or URL generation missing parameters

## How to Fix

1. Always provide required parameters when generating URLs:

```php
$url = route('orders.show', ['order' => $order->id]);
// Not: route('orders.show')
```

2. Use optional parameters for non-required segments:

```php
Route::get('/users/{id}/{tab?}', [UserController::class, 'show'])
    ->defaults(['tab', 'profile']);
```

3. Handle missing route model bindings gracefully:

```php
Route::bind('order', function ($value) {
    return Order::findOrFail($value);
});
```

4. Define typed parameters where appropriate:

```php
Route::get('/posts/{post:id}', [PostController::class, 'show']);
```

## Examples

```php
// Forgetting to pass a required parameter
route('orders.show');
// InvalidArgumentException: Missing required parameter "order".

// Route model binding fails for non-existent record
// GET /orders/99999
// ModelNotFoundException: No query results for model [App\Models\Order] 99999
```
