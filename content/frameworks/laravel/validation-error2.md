---
title: "Validation error (422)"
description: "Laravel returns a 422 Unprocessable Entity when request validation fails"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when a Laravel request fails the validation rules defined in a Form Request class, inline rules in the controller, or the `validate()` method.

## Common Causes

- Required fields missing from the request
- Data does not match the validation rules (e.g. email format, max length)
- Using `$request->input()` before calling `validate()`
- Custom validation rule failing

## How to Fix

1. Use Form Request classes for complex validation:

```php
// app/Http/Requests/StoreUserRequest.php
class StoreUserRequest extends FormRequest
{
    public function rules()
    {
        return [
            'name' => 'required|string|max:255',
            'email' => 'required|email|unique:users',
            'password' => 'required|min:8|confirmed',
        ];
    }
}
```

2. Use inline validation in controllers:

```php
public function store(Request $request)
{
    $validated = $request->validate([
        'name' => 'required|string|max:255',
        'email' => 'required|email',
    ]);

    User::create($validated);
    return redirect()->route('users.index');
}
```

3. Customize the validation error response:

```php
class StoreUserRequest extends FormRequest
{
    public function messages()
    {
        return [
            'email.unique' => 'This email is already registered.',
            'password.min' => 'Password must be at least 8 characters.',
        ];
    }
}
```

## Examples

```php
// Request: POST /users
// Body: {"name": "", "email": "invalid"}

$request->validate([
    'name' => 'required',
    'email' => 'required|email',
]);
// ValidationException: The name field is required.
// The email field must be a valid email address.
```

## Related Errors

- [Authentication failed]({{< relref "/frameworks/laravel/auth-error4" >}})
