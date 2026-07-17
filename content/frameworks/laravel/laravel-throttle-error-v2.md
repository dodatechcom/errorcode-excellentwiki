---
title: "Rate throttle exceeded"
description: "Laravel throws ThrottleRequestsException when a client exceeds the configured rate limit"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["throttle", "rate-limit", "middleware", "api", "security"]
weight: 5
---

This error occurs when a client sends too many requests within a given time window. Laravel throws `Illuminate\Routing\Exceptions\ThrottleRequestsException` and returns a 429 Too Many Requests response.

## Common Causes

- Client sending too many API requests per minute
- Default throttle limit too low for the use case
- Shared IP hitting limits across multiple users
- No caching driver configured for throttle keys
- Misconfigured throttle middleware on route group

## How to Fix

1. Define custom rate limits in `RouteServiceProvider`:

```php
use Illuminate\Cache\RateLimiting\Limit;
use Illuminate\Support\Facades\RateLimiter;

RateLimiter::for('api', function (Request $request) {
    return Limit::perMinute(60)->by(
        $request->user()?->id ?: $request->ip()
    );
});
```

2. Apply throttle middleware with custom limits:

```php
Route::middleware(['throttle:api'])->group(function () {
    Route::get('/posts', [PostController::class, 'index']);
});

// Or with inline parameters
Route::middleware('throttle:10,1')->group(function () {
    Route::post('/search', [SearchController::class, 'index']);
});
```

3. Handle the 429 response in the exception handler:

```php
use Illuminate\Routing\Exceptions\ThrottleRequestsException;

public function register()
{
    $this->renderable(function (ThrottleRequestsException $e, $request) {
        if ($request->expectsJson()) {
            return response()->json([
                'error' => 'Too many requests. Please try again later.',
            ], 429);
        }

        return back()->withErrors(['throttle' => 'Too many attempts.']);
    });
}
```

4. Use a named throttle for specific route groups:

```php
RateLimiter::for('uploads', function (Request $request) {
    return Limit::perHour(100)->by($request->user()->id);
});

Route::middleware(['throttle:uploads'])->group(function () {
    Route::post('/upload', [UploadController::class, 'store']);
});
```

## Examples

```php
// Per-user throttle
Route::middleware('throttle:60,1')->group(function () {
    Route::get('/dashboard', [DashboardController::class, 'index']);
});

// Per-IP throttle for guest routes
Route::middleware('throttle:20,1')->group(function () {
    Route::post('/contact', [ContactController::class, 'store']);
});
```

## Related Errors

- [Authentication required error]({{< relref "/frameworks/laravel/laravel-auth-error-v2" >}})
- [CSRF token mismatch]({{< relref "/frameworks/laravel/laravel-csrf-error-v2" >}})
