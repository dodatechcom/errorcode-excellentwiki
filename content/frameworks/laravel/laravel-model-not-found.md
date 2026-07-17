---
title: "ModelNotFoundException - model not found"
description: "Laravel throws ModelNotFoundException when an Eloquent model is not found in the database"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when you call `findOrFail()` or `firstOrFail()` on an Eloquent model and no matching record exists in the database. Laravel throws `Illuminate\Database\Eloquent\ModelNotFoundException`.

## Common Causes

- Record was deleted but application still references its ID
- Incorrect ID passed to `findOrFail()` or `route model binding`
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

2. Register a custom `ModelNotFoundException` handler in `Handler.php`:

```php
public function register()
{
    $this->renderable(function (ModelNotFoundException $e, $request) {
        return response()->json([
            'error' => 'Resource not found',
            'message' => $e->getModel() . ' not found',
        ], 404);
    });
}
```

3. Use route model binding with a custom key:

```php
Route::get('/users/{user:slug}', [UserController::class, 'show']);
```

## Examples

```php
// This throws ModelNotFoundException if no user with id=999
$user = User::findOrFail(999);

// Using route model binding — throws if slug doesn't match
Route::get('/posts/{post:slug}', [PostController::class, 'show']);
```

## Related Errors

- [Route not found]({{< relref "/frameworks/laravel/route-not-found3" >}})
- [Eloquent query error]({{< relref "/frameworks/laravel/eloquent-error" >}})
