---
title: "Route not defined error"
description: "Laravel throws RouteNotFoundException when a named route is not defined"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when you call `route()` or `url()` with a route name that is not defined in your routes files. Laravel throws `Symfony\Component\Routing\Exception\NotFoundException` or returns a 404 response.

## Common Causes

- Route name is misspelled or does not exist
- Route is defined in a route group with a prefix that changes the name
- Package route is not loaded in the service provider
- Cached routes are outdated after adding new routes
- Route is conditionally registered

## How to Fix

1. List all registered routes to verify names:

```bash
php artisan route:list --name=users
```

2. Use `route()` with a safe fallback:

```php
use Illuminate\Support\Facades\Route;

if (Route::has('dashboard')) {
    return redirect()->route('dashboard');
}

return redirect('/dashboard');
```

3. Clear the route cache after adding new routes:

```bash
php artisan route:clear
```

4. Register a global handler for missing named routes:

```php
use Symfony\Component\Routing\Exception\NotFoundException;

public function register()
{
    $this->renderable(function (NotFoundException $e, $request) {
        if ($request->expectsJson()) {
            return response()->json(['error' => 'Route not found'], 404);
        }
        abort(404);
    });
}
```

## Examples

```php
// This throws if 'users.index' route is not defined
return redirect()->route('users.index'));

// Safe route generation
$url = Route::has('posts.show')
    ? route('posts.show', $post->id)
    : '/posts';
```

## Related Errors

- [Model not found]({{< relref "/frameworks/laravel/laravel-model-not-found-v2" >}})
- [Blade template compilation error]({{< relref "/frameworks/laravel/laravel-blade-error-v2" >}})
