---
title: "ThrottleRequestsException - rate limit"
description: "Laravel throws ThrottleRequestsException when a request exceeds the configured rate limit"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["throttle", "rate-limit", "middleware", "api", "too-many-requests"]
weight: 5
---

This error occurs when a client sends too many requests within a given time window and exceeds Laravel's rate limit. The throttle middleware returns a 429 Too Many Requests response.

## Common Causes

- Client sending excessive API requests in a short period
- Rate limit configured too aggressively for the use case
- Missing or incorrect rate limit key (per-user vs per-IP)
- Bot or script hitting the endpoint repeatedly
- Shared IP address causing rate limit collisions

## How to Fix

1. Configure rate limits in `RouteServiceProvider` or `bootstrap/app.php`:

```php
RateLimiter::for('api', function (Request $request) {
    return Limit::perMinute(60)->by(
        $request->user()?->id ?: $request->ip()
    );
});
```

2. Apply rate limits to routes:

```php
Route::middleware('throttle:api')->group(function () {
    Route::get('/posts', [PostController::class, 'index']);
    Route::post('/posts', [PostController::class, 'store']);
});
```

3. Handle 429 responses gracefully:

```php
public function handle($request, Closure $next)
{
    $response = $next($request);

    if ($response->getStatusCode() === 429) {
        return response()->json([
            'error' => 'Rate limit exceeded',
            'retry_after' => $response->headers->get('Retry-After'),
        ], 429);
    }

    return $response;
}
```

## Examples

```php
// 100 requests per minute limit
Route::middleware('throttle:100,1')->get('/api/users', ...);
// ThrottleRequestsException after 100th request
```

## Related Errors

- [CSRF error]({{< relref "/frameworks/laravel/csrf-error" >}})
- [Auth error]({{< relref "/frameworks/laravel/auth-error4" >}})
