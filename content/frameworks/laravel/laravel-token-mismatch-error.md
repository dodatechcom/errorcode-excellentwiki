---
title: "[Solution] Laravel Token Mismatch Error"
description: "Fix Laravel TokenMismatchException verify CSRF token. Resolve 419 page expired errors in Laravel forms."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when the CSRF token sent with a form submission does not match the token stored in the user's session.

## Common Causes

- Session expired between page load and form submission
- Browser cookies are blocked or cleared
- Multiple browser tabs with different sessions
- `APP_URL` mismatch causes cookie domain issues
- Cached page contains a stale CSRF token
- Token verification disabled in `VerifyCsrfToken` middleware

## How to Fix

1. Include the CSRF token in your Blade form:

```html
<form method="POST" action="/submit">
    @csrf
    <input type="text" name="name">
    <button type="submit">Submit</button>
</form>
```

2. For AJAX requests, include the token in headers:

```javascript
axios.post('/api/submit', data, {
    headers: {
        'X-CSRF-TOKEN': document.querySelector('meta[name="csrf-token"]').content
    }
});
```

3. Ensure `APP_URL` matches your domain in `.env`:

```text
APP_URL=http://localhost:8000
```

4. Whitelist specific routes if needed:

```php
// app/Http/Middleware/VerifyCsrfToken.php
protected $except = [
    'webhook/*',
    'api/payment/callback',
];
```

## Examples

```php
// Submitting a form with expired session returns 419
// POST /contact  =>  419 | Page Expired

// Verify the token is being generated in the layout
// <meta name="csrf-token" content="{{ csrf_token() }}">
```
