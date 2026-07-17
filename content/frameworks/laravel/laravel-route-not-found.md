---
title: "RouteNotFoundException - route not defined"
description: "Laravel throws RouteNotFoundException when a named route or URL generation references a route that does not exist"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Laravel tries to generate a URL for a named route that does not exist in the routing table. It throws `Symfony\Component\Routing\Exception\RouteNotFoundException`.

## Common Causes

- Route name is misspelled in `route()` helper
- Route was removed or renamed in `routes/web.php`
- Route is defined in a group with a prefix that was changed
- Using `route()` with a route defined only in API routes but calling from web context

## How to Fix

1. Verify the route exists by listing all routes:

```bash
php artisan route:list
```

2. Use `route()` with the correct name:

```php
// In routes/web.php
Route::get('/users/{user}', [UserController::class, 'show'])->name('users.show');

// In Blade or Controller
$url = route('users.show', ['user' => 1]);
// Returns: http://example.com/users/1
```

3. Use fallback routes to handle undefined routes:

```php
Route::fallback(function () {
    return response()->json(['error' => 'Route not found'], 404);
});
```

4. Check for conditional route registration:

```php
// Routes wrapped in conditionals may not be registered
if (config('app.features.new_dashboard')) {
    Route::get('/dashboard', ...)->name('dashboard');
}
```

## Examples

```php
// Route name typo
return redirect()->route('users.shwo', $user->id);
// RouteNotFoundException: Route [users.shwo] not defined
```

## Related Errors

- [Model not found]({{< relref "/frameworks/laravel/laravel-model-not-found" >}})
- [Blade error]({{< relref "/frameworks/laravel/blade-error" >}})
