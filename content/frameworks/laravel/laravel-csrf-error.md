---
title: "TokenMismatchException - CSRF token mismatch"
description: "Laravel throws TokenMismatchException when the CSRF token in the request does not match the session token"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["csrf", "token", "security", "middleware", "session"]
weight: 5
---

This error occurs when a POST, PUT, PATCH, or DELETE request does not include a valid CSRF token. Laravel's `VerifyCsrfToken` middleware compares the token in the request with the one stored in the session and throws `Illuminate\Session\TokenMismatchException`.

## Common Causes

- Form does not include `@csrf` directive
- AJAX request missing the `X-CSRF-TOKEN` header
- Session expired or cookie not sent with the request
- Multiple tabs causing session token rotation
- CSRF token not refreshed after page load

## How to Fix

1. Include the CSRF token in Blade forms:

```html
<form method="POST" action="/posts">
    @csrf
    <input type="text" name="title">
    <button type="submit">Submit</button>
</form>
```

2. Include CSRF token in AJAX requests:

```javascript
// Using meta tag
const token = document.querySelector('meta[name="csrf-token"]').content;

fetch('/api/posts', {
    method: 'POST',
    headers: {
        'X-CSRF-TOKEN': token,
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ title: 'New Post' }),
});
```

3. Exclude routes from CSRF verification in `Middleware.php`:

```php
protected $except = [
    'api/*',
    'webhooks/*',
];
```

## Examples

```html
<!-- Missing @csrf causes TokenMismatchException -->
<form method="POST" action="/login">
    <input name="email" type="email">
    <button type="submit">Login</button>
</form>

<!-- Fixed with @csrf -->
<form method="POST" action="/login">
    @csrf
    <input name="email" type="email">
    <button type="submit">Login</button>
</form>
```

## Related Errors

- [Auth error]({{< relref "/frameworks/laravel/auth-error4" >}})
- [Validation error]({{< relref "/frameworks/laravel/validation-error2" >}})
