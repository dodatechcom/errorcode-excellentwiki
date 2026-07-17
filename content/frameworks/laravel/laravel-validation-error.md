---
title: "ValidationException - validation failed"
description: "Laravel throws ValidationException when request data fails validation rules"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when incoming request data does not pass the defined validation rules. Laravel throws `Illuminate\Validation\ValidationException` with detailed error messages for each failed rule.

## Common Causes

- Required fields are missing from the request
- Field values do not match expected format (email, URL, etc.)
- Unique constraint violated during store/update
- Custom validation rules reject the input
- Request data type mismatch (string instead of integer)

## How to Fix

1. Use `validate()` in the controller for inline validation:

```php
public function store(Request $request)
{
    $validated = $request->validate([
        'name' => 'required|string|max:255',
        'email' => 'required|email|unique:users,email',
        'age' => 'required|integer|min:18',
    ]);

    User::create($validated);
}
```

2. Create a Form Request for reusable validation:

```php
class StoreUserRequest extends FormRequest
{
    public function rules(): array
    {
        return [
            'name' => 'required|string|max:255',
            'email' => 'required|email|unique:users,email',
        ];
    }
}
```

3. Handle the exception globally in `Handler.php`:

```php
public function register()
{
    $this->renderable(function (ValidationException $e, $request) {
        return response()->json([
            'errors' => $e->errors(),
        ], 422);
    });
}
```

## Examples

```php
// Missing required field triggers ValidationException
$request->validate(['email' => 'required|email']);
// ValidationException: The email field is required.
```

## Related Errors

- [Auth error]({{< relref "/frameworks/laravel/auth-error4" >}})
- [CSRF error]({{< relref "/frameworks/laravel/csrf-error" >}})
