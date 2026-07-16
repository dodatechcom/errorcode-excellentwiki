---
title: "Authentication failed"
description: "Laravel throws AuthenticationException when the user credentials are invalid or the guard fails"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["authentication", "login", "guard", "session", "sanctum"]
weight: 5
---

This error occurs when Laravel's authentication system rejects a login attempt because the credentials are invalid, the user is not found, or the authentication guard is misconfigured.

## Common Causes

- Invalid email or password combination
- User account is deactivated (`active` column is `false`)
- Wrong authentication guard configured for the route
- Sanctum or Passport token has expired

## How to Fix

1. Use Laravel's built-in auth helper:

```php
use Illuminate\Support\Facades\Auth;

if (Auth::attempt(['email' => $email, 'password' => $password])) {
    return redirect()->intended('/dashboard');
}
return back()->withErrors(['email' => 'Invalid credentials']);
```

2. Handle failed authentication in the controller:

```php
public function login(Request $request)
{
    $credentials = $request->validate([
        'email' => 'required|email',
        'password' => 'required',
    ]);

    if (!Auth::attempt($credentials)) {
        return response()->json(['error' => 'Invalid credentials'], 401);
    }

    $token = Auth::user()->createToken('auth-token')->plainTextToken;
    return response()->json(['token' => $token]);
}
```

3. Use the correct guard for multi-auth:

```php
// config/auth.php
'guards' => [
    'web' => ['driver' => 'session', 'provider' => 'users'],
    'admin' => ['driver' => 'session', 'provider' => 'admins'],
],

// In controller
if (!Auth::guard('admin')->attempt($credentials)) {
    return response()->json(['error' => 'Admin auth failed'], 401);
}
```

## Examples

```php
Auth::attempt(['email' => 'user@example.com', 'password' => 'wrongpassword']);
// false — authentication failed
```

```text
Illuminate\Auth\AuthenticationException: Unauthenticated.
```

## Related Errors

- [Validation error]({{< relref "/frameworks/laravel/validation-error2" >}})
