---
title: "Blade template compilation error"
description: "Laravel throws TemplateNotFoundException or compilation errors when Blade templates cannot be compiled"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["blade", "template", "compilation", "view", "syntax"]
weight: 5
---

This error occurs when Laravel cannot compile a Blade template due to syntax errors, missing views, or invalid directives. The `Illuminate\View\ViewException` is thrown during template rendering.

## Common Causes

- Blade syntax error in the template (unclosed `@if`, `@foreach`, etc.)
- Referenced view file does not exist in `resources/views`
- Missing variable passed to the view
- Compiled cache is stale or corrupted
- Invalid Blade component usage

## How to Fix

1. Clear the compiled view cache:

```bash
php artisan view:clear
```

2. Use the correct Blade syntax and validate your templates:

```php
// resources/views/users/index.blade.php
@section('content')
    @foreach($users as $user)
        <div class="user">
            <h2>{{ $user->name }}</h2>
            <p>{{ $user->email }}</p>
        </div>
    @endforeach
@endsection
```

3. Pass all required variables to views:

```php
public function index()
{
    $users = User::all();

    return view('users.index', compact('users'));
}
```

4. Handle missing view errors gracefully:

```php
use Illuminate\View\ViewException;

public function register()
{
    $this->renderable(function (ViewException $e, $request) {
        if (config('app.debug')) {
            return; // Show debug page
        }

        return response()->view('errors.500', [], 500);
    });
}
```

## Examples

```php
// Invalid: unclosed @if directive
// @if($user->isAdmin())
// <p>Admin</p>

// Valid:
@if($user->isAdmin())
    <p>Admin</p>
@endif

// Component with required prop
<x-alert type="error" message="{{ $error }}" />
```

## Related Errors

- [Route not defined error]({{< relref "/frameworks/laravel/laravel-route-not-found-v2" >}})
- [Service container resolution error]({{< relref "/frameworks/laravel/laravel-service-container-v2" >}})
