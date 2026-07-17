---
title: "ModelNotFoundException - model not found"
description: "Laravel throws ModelNotFoundException when an Eloquent model record cannot be found in the database"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when you call `findOrFail()` or `firstOrFail()` on an Eloquent model and no matching record exists. Laravel throws `Illuminate\Database\Eloquent\ModelNotFoundException`.

## Common Causes

- Record was deleted but application still references its ID
- Incorrect ID passed to `findOrFail()` or route model binding
- Query conditions filter out all matching records
- Database was reset or migrated without seeding

## How to Fix

1. Use `find()` instead of `findOrFail()` when the record may not exist:

```php
$user = User::find($id);

if (!$user) {
    return response()->json(['error' => 'User not found'], 404);
}
```

2. Register a custom `ModelNotFoundException` handler:

```php
use Illuminate\Database\Eloquent\ModelNotFoundException;

public function register()
{
    $this->renderable(function (ModelNotFoundException $e, $request) {
        return response()->json([
            'error' => 'Resource not found',
            'message' => class_basename($e->getModel()) . ' not found',
        ], 404);
    });
}
```

3. Use route model binding with a fallback route:

```php
Route::get('/users/{user?}', [UserController::class, 'show']);

public function show(?User $user)
{
    if (!$user) {
        return response()->json(['error' => 'User not found'], 404);
    }
}
```

## Examples

```php
// Throws ModelNotFoundException if no user with id=999
$user = User::findOrFail(999);

// Using route model binding — throws if slug doesn't match
Route::get('/posts/{post:slug}', [PostController::class, 'show']);

// Safe lookup with default
$user = User::findOr($id, fn () => User::factory()->make());
```

## Related Errors

- [Route not found]({{< relref "/frameworks/laravel/laravel-route-not-found-v2" >}})
- [File not found]({{< relref "/frameworks/laravel/laravel-file-not-found-v2" >}})
