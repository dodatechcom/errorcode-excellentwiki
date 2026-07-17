---
title: "Route not found (404)"
description: "Laravel returns a 404 error when no route matches the incoming request URL"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Laravel cannot find a route that matches the request URL and HTTP method. The framework returns a 404 Not Found response or the `NotFoundHttpException`.

## Common Causes

- Route not defined in `routes/web.php` or `routes/api.php`
- HTTP method mismatch (e.g. POST route accessed via GET)
- Route group prefix or name does not match the URL
- Missing or incorrect middleware blocking the route

## How to Fix

1. List all registered routes for debugging:

```bash
php artisan route:list
```

2. Define the route correctly:

```php
// routes/web.php
Route::get('/users', [UserController::class, 'index']);
Route::post('/users', [UserController::class, 'store']);
```

3. Handle 404 errors gracefully with a custom handler:

```php
// app/Exceptions/Handler.php
public function render($request, Throwable $e)
{
    if ($e instanceof NotFoundHttpException) {
        return response()->view('errors.404', [], 404);
    }
    return parent::render($request, $e);
}
```

4. Verify route names and prefixes match:

```php
Route::prefix('api')->group(function () {
    Route::get('/users', [UserController::class, 'index'])->name('users.index');
});
// Access at: /api/users (not /users)
```

## Examples

```php
// Route is defined for POST but accessed via GET
Route::post('/users', [UserController::class, 'store']);

// Browser navigates to: GET /users
// NotFoundHttpException: No query results for model [App\Models\User]
```

## Related Errors

- [Method not found on instance]({{< relref "/frameworks/laravel/method-not-found" >}})
