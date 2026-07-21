---
title: "[Solution] Laravel Email Verification Error"
description: "Fix Laravel email verification link invalid or expired. Resolve MustVerifyEmail contract issues in Laravel."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when a user clicks the email verification link but the token is invalid, the URL has expired, or the user model does not implement the `MustVerifyEmail` contract.

## Common Causes

- User model does not implement `Illuminate\Contracts\Auth\MustVerifyEmail`
- Verification token expired (default 60 minutes in some configs)
- `APP_URL` mismatch causes the signed URL to be invalid
- `email_verified_at` column is missing from users table
- Queue worker not processing verification mail

## How to Fix

1. Add the `MustVerifyEmail` interface to the User model:

```php
namespace App\Models;

use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Foundation\Auth\User as Authenticatable;

class User extends Authenticatable implements MustVerifyEmail
{
    // ...
}
```

2. Ensure the `email_verified_at` column exists:

```php
Schema::table('users', function (Blueprint $table) {
    $table->timestamp('email_verified_at')->nullable();
});
```

3. Allow verification routes without auth middleware:

```php
Route::get('/email/verify', [VerifyEmailController::class, 'show'])
    ->middleware('signed')
    ->name('verification.verify');
```

4. Resend verification if needed:

```php
$user->sendEmailVerificationNotification();
```

## Examples

```php
// User clicks link but gets "Invalid" page
// Verification link: /email/verify/15/abc123?signature=...
// Error: The verification link is invalid or has expired.

// Fix the URL helper to use the correct APP_URL
 url(route('verification.verify', [
    'id' => $user->id,
    'hash' => sha1($user->email),
]));
```
