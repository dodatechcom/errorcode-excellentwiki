---
title: "[Solution] Laravel Password Reset Token Error"
description: "Fix Laravel password reset token invalid or expired. Resolve Cannot decrypt encryption error in reset flow."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when a user clicks a password reset link but the token is invalid, expired, or cannot be decrypted due to key mismatch.

## Common Causes

- Password reset token has expired (default 60 minutes)
- `APP_KEY` was regenerated after the token was created
- User clicked an old reset link from a previous request
- `password_residents` table has wrong token hashing
- Email link was corrupted by URL encoding or line wrapping

## How to Fix

1. Extend the token expiration in `config/auth.php`:

```php
'passwords' => [
    'users' => [
        'provider' => 'users',
        'table' => 'password_reset_tokens',
        'expire' => 120, // minutes
        'throttle' => 60,
    ],
],
```

2. Clear stale tokens before generating new ones:

```php
use Illuminate\Support\Facades\DB;

DB::table('password_reset_tokens')
    ->where('email', $email)
    ->delete();
```

3. Ensure the token is URL-safe when embedded in emails:

```php
$url = url("/reset-password/{$token}");
// Token should not contain + / = characters
```

4. Use the built-in broker properly:

```php
Password::broker('users')->sendResetLink($credentials);
```

## Examples

```php
// Token expired after 60 minutes
// "This password reset token is invalid."
Password::broker('users')->reset($credentials, function ($user, $password) {
    $user->password = Hash::make($password);
    $user->save();
});
// TokenNotFoundException
```
