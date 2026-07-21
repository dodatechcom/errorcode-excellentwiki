---
title: "[Solution] Laravel Blade @yield Error"
description: "@yield not showing."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

@yield not showing.

## Common Causes

Section not defined.

## How to Fix

Use @yield/@section.

## Example

```blade
@yield('content')
@section('content')<p>Content</p>@endsection
```
