---
title: "[Solution] Laravel Auth Guard Mismatch Error"
description: "Fix Laravel auth guard mismatch driver mismatch error. Resolve authentication guard configuration issues."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when the authentication guard uses a provider or driver that does not match the configured user model or database schema.

## Common Causes

- Guard configured with `eloquent` driver but model does not exist
- Provider references a table that has no `password` column
- Multiple guards (web, api, admin) use different providers pointing to wrong models
- User model does not implement `Authenticatable` contract
- Custom guard driver not registered in `AuthServiceProvider`

## How to Fix

1. Verify guard configuration in `config/auth.php`:

```php
'guards' => [
    'web' => [
        'driver' => 'session',
        'provider' => 'users',
    ],
    'api' => [
        'driver' => 'sanctum',
        'provider' => 'users',
    ],
],
'providers' => [
    'users' => [
        'driver' => 'eloquent',
        'model' => App\Models\User::class,
    ],
],
```

2. Ensure the model table has required columns:

```php
Schema::table('users', function (Blueprint $table) {
    $table->string('email')->unique();
    $table->string('password');
});
```

3. Switch guards at runtime when needed:

```php
Auth::guard('admin')->attempt($credentials);
$user = Auth::guard('api')->user();
```

## Examples

```php
// Guard references a model with no password column
Auth::attempt(['email' => 'user@example.com', 'password' => 'secret']);
// InvalidArgumentException: User does not exist.

// Admin guard uses wrong provider
// config/auth.php providers.admin.model = App\\Models\\Admin::class
// But Admin model table is missing 'password' column
```
