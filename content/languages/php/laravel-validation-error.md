---
title: "[Solution] PHP LARAVEL_VALIDATION_ERROR — Form Validation Failed"
description: "Fix PHP LARAVEL_VALIDATION_ERROR by defining validation rules, handling error messages, and using FormRequest. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 121
---

# PHP LARAVEL_VALIDATION_ERROR — Form Validation Failed

Form validation failed in Laravel. This error occurs when request data does not meet defined validation rules, error messages are not properly handled, or FormRequest classes are misconfigured.

## Common Causes

```php
// Missing validation rules
public function store(Request $request)
{
    $user = User::create($request->all()); // no validation
}
```

```php
// Wrong validation rule syntax
$validated = $request->validate([
    'email' => 'required|email', // 'email' rule returns boolean, not descriptive error
    'age' => 'min:18|max:100', // string comparison, not numeric
]);
```

```php
// Validation error not handled properly
$validated = $request->validate([
    'name' => 'required',
]);
// Returns 422 JSON but no redirect for web requests
```

```php
// Custom rule class not registered
use App\Rules\Uppercase; // class doesn't exist
$validated = $request->validate(['name' => ['required', new Uppercase]]);
```

```php
// FormRequest missing authorize method
class StoreUserRequest extends FormRequest
{
    public function authorize(): bool
    {
        return false; // always denies access
    }
}
```

## How to Fix

### Fix 1: Define Proper Validation Rules

```php
// In controller
public function store(Request $request)
{
    $validated = $request->validate([
        'name' => 'required|string|min:2|max:255',
        'email' => 'required|email|max:255|unique:users,email',
        'password' => 'required|string|min:8|confirmed',
        'age' => 'required|integer|min:18|max:120',
        'terms' => 'accepted',
        'avatar' => 'nullable|image|mimes:jpeg,png,jpg,gif|max:2048',
        'role' => 'required|in:admin,user,editor',
        'website' => 'nullable|url',
        'phone' => 'nullable|regex:/^[\+]?[0-9]{3,6}[-\s\.]?[0-9]{3,6}[-\s\.]?[0-9]{3,6}$/',
    ]);

    // $validated contains only validated data
    $user = User::create($validated);

    return redirect()->route('users.show', $user)
        ->with('success', 'User created successfully');
}
```

### Fix 2: Use FormRequest Classes

```php
// app/Http/Requests/StoreUserRequest.php
namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class StoreUserRequest extends FormRequest
{
    public function authorize(): bool
    {
        return true; // allow access
    }

    public function rules(): array
    {
        return [
            'name'     => 'required|string|min:2|max:255',
            'email'    => 'required|email|max:255|unique:users,email',
            'password' => 'required|string|min:8|confirmed',
            'age'      => 'required|integer|min:18',
            'role'     => 'required|in:admin,user,editor',
        ];
    }

    public function messages(): array
    {
        return [
            'name.required'    => 'Please enter your name',
            'email.required'   => 'Email address is required',
            'email.unique'     => 'This email is already registered',
            'password.min'     => 'Password must be at least 8 characters',
            'age.min'          => 'You must be at least 18 years old',
        ];
    }

    public function attributes(): array
    {
        return [
            'name'     => 'full name',
            'email'    => 'email address',
            'password' => 'password',
        ];
    }
}

// In controller
public function store(StoreUserRequest $request)
{
    $validated = $request->validated();
    $user = User::create($validated);

    return redirect()->route('users.show', $user);
}
```

### Fix 3: Handle Validation Errors Manually

```php
// Manual validation
$validator = Validator::make($request->all(), [
    'name'  => 'required|min:3',
    'email' => 'required|email',
]);

if ($validator->fails()) {
    return redirect('user/create')
        ->withErrors($validator)
        ->withInput();
}

// Get error messages
$errors = $validator->errors();
echo $errors->first('name'); // first error for name
echo $errors->get('email'); // all errors for email

// JSON response for AJAX
if ($request->ajax()) {
    return response()->json([
        'errors' => $validator->errors(),
    ], 422);
}
```

### Fix 4: Custom Validation Rules

```php
// app/Rules/Uppercase.php
namespace App\Rules;

use Closure;
use Illuminate\Contracts\Validation\ValidationRule;

class Uppercase implements ValidationRule
{
    public function validate(string $attribute, mixed $value, Closure $fail): void
    {
        if (strtoupper($value) !== $value) {
            $fail("The {$attribute} must be uppercase.");
        }
    }
}

// Usage
$validated = $request->validate([
    'name' => ['required', new Uppercase],
]);
```

## Examples

```php
// Complete validation example
class UserController extends Controller
{
    public function store(StoreUserRequest $request)
    {
        $validated = $request->validated();

        // Hash password before saving
        $validated['password'] = Hash::make($validated['password']);

        $user = User::create($validated);

        // Send welcome email
        Mail::to($user->email)->send(new WelcomeMail($user));

        return redirect()->route('users.show', $user)
            ->with('success', 'Registration successful!');
    }

    public function update(UpdateUserRequest $request, User $user)
    {
        $validated = $request->validated();

        if ($request->has('password')) {
            $validated['password'] = Hash::make($validated['password']);
        }

        $user->update($validated);

        return redirect()->route('users.show', $user)
            ->with('success', 'Profile updated!');
    }
}
```

```blade
{{-- resources/views/user/create.blade.php --}}
<form method="POST" action="{{ route('users.store') }}">
    @csrf

    <div class="form-group">
        <label for="name">Name</label>
        <input type="text" name="name" id="name" value="{{ old('name') }}"
               class="@error('name') is-invalid @enderror">

        @error('name')
            <span class="error">{{ $message }}</span>
        @enderror
    </div>

    <div class="form-group">
        <label for="email">Email</label>
        <input type="email" name="email" id="email" value="{{ old('email') }}"
               class="@error('email') is-invalid @enderror">

        @error('email')
            <span class="error">{{ $message }}</span>
        @enderror
    </div>

    <button type="submit">Register</button>
</form>
```

## Related Errors

- [Laravel Model Not Found](/languages/php/laravel-model-not-found)
- [Symfony Form Error](/languages/php/symfony-form-error)
- [Symfony Validator Error](/languages/php/symfony-validator-error)
- [Laravel Token Mismatch](/languages/php/laravel-token-mismatch)
