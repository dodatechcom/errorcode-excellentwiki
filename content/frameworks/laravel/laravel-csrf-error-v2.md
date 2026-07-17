---
title: "CSRF token mismatch"
description: "Laravel throws TokenMismatchException when the CSRF token in the request does not match the session token"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["csrf", "token", "security", "session", "middleware"]
weight: 5
---

This error occurs when a POST, PUT, or DELETE request is submitted without a valid CSRF token. Laravel throws `Illuminate\Session\TokenMismatchException` to protect against cross-site request forgery attacks.

## Common Causes

- Form does not include `@csrf` Blade directive
- Session expired while user was on the page
- JavaScript AJAX request missing CSRF token header
- Cookie-based session issues in SPA or API contexts
- Multiple tabs open with different session states

## How to Fix

1. Add the CSRF token to Blade forms:

```html
<form method="POST" action="/posts">
    @csrf
    <input type="text" name="title">
    <button type="submit">Create</button>
</form>
```

2. Include CSRF token in JavaScript AJAX requests:

```javascript
// Using meta tag approach
const token = document.querySelector('meta[name="csrf-token"]').content;

fetch('/posts', {
    method: 'POST',
    headers: {
        'X-CSRF-TOKEN': token,
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ title: 'New Post' }),
});
```

3. Add the CSRF meta tag to your layout:

```html
<meta name="csrf-token" content="{{ csrf_token() }}">
```

4. Exclude specific routes from CSRF verification (use sparingly):

```php
// Kernel.php or bootstrap/app.php
protected $middlewareGroup = [
    'web' => [
        // ...
        \Illuminate\Foundation\Http\Middleware\VerifyCsrfToken::class,
    ],
];

// Except specific URIs
protected $except = [
    'webhooks/*',
];
```

## Examples

```php
// Generating a token manually
$token = csrf_token();

// Checking token in a request
if ($request->input('_token') !== session('token')) {
    abort(419);
}
```

## Related Errors

- [Authentication required error]({{< relref "/frameworks/laravel/laravel-auth-error-v2" >}})
- [Validation failed]({{< relref "/frameworks/laravel/laravel-validation-error-v2" >}})
