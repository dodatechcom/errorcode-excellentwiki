---
title: "Authentication required error"
description: "Laravel throws AuthenticationException when an unauthenticated user accesses a protected route"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["auth", "authentication", "login", "middleware", "guard"]
weight: 5
---

This error occurs when an unauthenticated user tries to access a route protected by the `auth` middleware. Laravel throws `Illuminate\Auth\AuthenticationException` and redirects to the login page or returns a 401 response.

## Common Causes

- User is not logged in but accessing a protected route
- Session expired or token invalid
- Wrong authentication guard configured for the route
- Sanctum or Passport token is missing or expired
- Middleware applied to the wrong route group

## How to Fix

1. Check if the user is authenticated before accessing protected data:

```php
public function dashboard(Request $request)
{
    if (!$request->user()) {
        return redirect()->route('login');
    }

    return view('dashboard', ['user' => $request->user()]);
}
```

2. Register a custom `AuthenticationException` handler:

```php
use Illuminate\Auth\AuthenticationException;

protected function unauthenticated($request, AuthenticationException $exception)
{
    if ($request->expectsJson()) {
        return response()->json(['error' => 'Unauthenticated'], 401);
    }

    return redirect()->guest($exception->redirectTo() ?? route('login'));
}
```

3. Use the correct guard for API routes:

```php
// api.php
Route::middleware('auth:sanctum')->group(function () {
    Route::get('/user', function (Request $request) {
        return $request->user();
    });
});
```

## Examples

```php
// Route protected by auth middleware
Route::middleware(['auth'])->group(function () {
    Route::get('/profile', [ProfileController::class, 'show']);
});

// Using a specific guard
Route::middleware(['auth:admin'])->group(function () {
    Route::get('/admin', [AdminController::class, 'index']);
});
```

## Related Errors

- [CSRF token mismatch]({{< relref "/frameworks/laravel/laravel-csrf-error-v2" >}})
- [Rate throttle exceeded]({{< relref "/frameworks/laravel/laravel-throttle-error-v2" >}})
