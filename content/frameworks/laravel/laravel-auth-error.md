---
title: "AuthenticationException - unauthenticated"
description: "Laravel throws AuthenticationException when a user is not authenticated and tries to access a protected route"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["auth", "authentication", "middleware", "login", "unauthenticated"]
weight: 5
---

This error occurs when an unauthenticated user attempts to access a route protected by the `auth` middleware. Laravel throws `Illuminate\Auth\AuthenticationException` and redirects to the login page or returns a 401 JSON response.

## Common Causes

- User is not logged in and accessing a protected route
- Session has expired or been invalidated
- API token has been revoked or is missing
- Guard configuration mismatch for multi-auth setups
- Cookie-based session not being sent with AJAX requests

## How to Fix

1. Check authentication in Blade or controllers:

```php
// In Blade
@if(Auth::check())
    <p>Welcome, {{ Auth::user()->name }}</p>
@endif

// In Controller
if (!auth()->check()) {
    return redirect()->route('login');
}
```

2. Configure the `auth` middleware redirect in `Handler.php`:

```php
protected function unauthenticated($request, AuthenticationException $exception)
{
    if ($request->expectsJson()) {
        return response()->json(['error' => 'Unauthenticated'], 401);
    }

    return redirect()->guest($exception->login() ?? route('login'));
}
```

3. Set up multi-auth guards properly:

```php
// config/auth.php
'guards' => [
    'web' => [
        'driver' => 'session',
        'provider' => 'users',
    ],
    'admin' => [
        'driver' => 'session',
        'provider' => 'admins',
    ],
],

// Usage
Route::middleware('auth:admin')->group(function () {
    Route::get('/admin/dashboard', [AdminDashboardController::class, 'index']);
});
```

## Examples

```php
Route::middleware('auth')->get('/profile', [ProfileController::class, 'show']);
// AuthenticationException if user is not logged in
```

## Related Errors

- [Validation error]({{< relref "/frameworks/laravel/validation-error2" >}})
- [CSRF error]({{< relref "/frameworks/laravel/csrf-error" >}})
