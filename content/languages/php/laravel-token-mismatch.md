---
title: "[Solution] PHP LARAVEL_CSRF_TOKEN_MISMATCH — CSRF Token Verification Failed"
description: "Fix PHP LARAVEL_CSRF_TOKEN_MISMATCH by including @csrf in forms, verifying token generation, and handling AJAX properly. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 125
---

# PHP LARAVEL_CSRF_TOKEN_MISMATCH — CSRF Token Verification Failed

A CSRF token verification failed in Laravel. This error occurs when the CSRF token is missing from forms, the token has expired, or AJAX requests don't include the token properly.

## Common Causes

```blade
{{-- Missing @csrf directive in form --}}
<form method="POST" action="/users">
    <input type="text" name="name">
    <button type="submit">Submit</button>
</form>
```

```javascript
// AJAX request without CSRF token
fetch('/api/users', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: { 'Content-Type': 'application/json' }
    // missing X-CSRF-TOKEN header
});
```

```php
// Session expired or regenerated
// User submitted form after session timeout
```

```php
// VerifyCsrfToken middleware disabled for route
// But CSRF verification is required
```

```php
// Token mismatch due to cached page
// Form was cached without fresh token
```

## How to Fix

### Fix 1: Include @csrf in All Forms

```blade
{{-- Blade form with @csrf --}}
<form method="POST" action="{{ route('users.store') }}">
    @csrf

    <input type="text" name="name" value="{{ old('name') }}">
    <input type="email" name="email" value="{{ old('email') }}">
    <button type="submit">Create User</button>
</form>

{{-- PUT/PATCH/DELETE forms need @method too --}}
<form method="POST" action="{{ route('users.update', $user) }}">
    @csrf
    @method('PUT')

    <input type="text" name="name" value="{{ $user->name }}">
    <button type="submit">Update User</button>
</form>

{{-- Raw HTML form --}}
<form method="POST" action="/users">
    <input type="hidden" name="_token" value="{{ csrf_token() }}">

    <input type="text" name="name">
    <button type="submit">Submit</button>
</form>
```

### Fix 2: Handle AJAX Requests

```javascript
// JavaScript — include CSRF token in AJAX requests
// Method 1: Meta tag approach
const csrfToken = document.querySelector('meta[name="csrf-token"]').content;

fetch('/users', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRF-TOKEN': csrfToken,
        'X-Requested-With': 'XMLHttpRequest',
    },
    body: JSON.stringify({ name: 'John', email: 'john@example.com' }),
})
.then(response => response.json())
.then(data => console.log(data));

// Method 2: Cookie approach (for SPA)
// Laravel provides XSRF-TOKEN cookie
// Axios reads this cookie automatically
axios.post('/users', { name: 'John', email: 'john@example.com' });

// Method 3: Manual token from form
const token = document.querySelector('input[name="_token"]').value;
```

```blade
{{-- Add CSRF meta tag in layout --}}
<head>
    <meta name="csrf-token" content="{{ csrf_token() }}">
</head>
```

```javascript
// jQuery AJAX setup
$.ajaxSetup({
    headers: {
        'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
    }
});

// Vue.js with axios
// resources/js/bootstrap.js
window.axios = require('axios');
window.axios.defaults.headers.common['X-CSRF-TOKEN'] =
    document.querySelector('meta[name="csrf-token"]').content;
```

### Fix 3: Exclude Routes from CSRF Protection

```php
// app/Http/Middleware/VerifyCsrfToken.php
protected $except = [
    'api/*', // all API routes
    'webhooks/*',
    'payment/callback',
];

// In Kernel.php (Laravel 10)
protected $middlewareGroups = [
    'web' => [
        // ...
        \App\Http\Middleware\VerifyCsrfToken::class,
    ],
];

// In AppServiceProvider (Laravel 11)
public function boot(): void
{
    $this->app[VerifyCsrfToken::class]->except([
        'api/*',
        'webhooks/*',
    ]);
}
```

### Fix 4: Regenerate CSRF Token

```php
// In controller
public function store(Request $request)
{
    // Token is automatically validated by VerifyCsrfToken

    // If token mismatch, regenerate session
    $request->session()->regenerate();

    $validated = $request->validate([...]);
    // ...
}

// Manual token refresh
csrf_token(); // generate new token
```

```blade
{{-- Refresh token in form periodically --}}
<form method="POST" action="/users" id="userForm">
    @csrf
    <input type="text" name="name">
    <button type="submit">Submit</button>
</form>

<script>
// Refresh token every 30 minutes
setInterval(() => {
    fetch('/refresh-token')
        .then(response => response.json())
        .then(data => {
            document.querySelector('input[name="_token"]').value = data.token;
        });
}, 1800000);
</script>
```

## Examples

```blade
{{-- Complete form example with error handling --}}
<form method="POST" action="{{ route('contact.store') }}">
    @csrf

    <div class="form-group">
        <label for="name">Name</label>
        <input type="text" name="name" id="name"
               value="{{ old('name') }}"
               class="@error('name') is-invalid @enderror">

        @error('name')
            <span class="error">{{ $message }}</span>
        @enderror
    </div>

    <div class="form-group">
        <label for="email">Email</label>
        <input type="email" name="email" id="email"
               value="{{ old('email') }}"
               class="@error('email') is-invalid @enderror">

        @error('email')
            <span class="error">{{ $message }}</span>
        @enderror
    </div>

    <button type="submit">Send Message</button>
</form>

@if(session('success'))
    <div class="alert alert-success">
        {{ session('success') }}
    </div>
@endif
```

```php
// API controller handling CSRF
class ApiUserController extends Controller
{
    public function store(Request $request)
    {
        $validated = $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|email',
        ]);

        $user = User::create($validated);

        return response()->json($user, 201);
    }
}
```

## Related Errors

- [Laravel Validation Error](/languages/php/laravel-validation-error)
- [Symfony Security Error](/languages/php/symfony-security-error)
- [Session Start Error](/languages/php/session-start-error)
- [CodeIgniter Session Error](/languages/php/codeigniter-session-error)
