---
title: "[Solution] Laravel Blade @auth Error"
description: "@auth not working."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

@auth not working.

## Common Causes

Not logged in.

## How to Fix

Check auth.

## Example

```blade
@auth
    Welcome, {{ Auth::user()->name }}
@endauth
```
