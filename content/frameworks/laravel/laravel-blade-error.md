---
title: "ViewException - Blade template error"
description: "Laravel throws ViewException when a Blade template has syntax errors or references undefined variables"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when a Blade template fails to compile or references a variable/method that is not available. It throws `Illuminate\View\ViewException` with details about the template file and line number.

## Common Causes

- Undefined variable passed to the view
- Blade directive syntax error (`@if`, `@foreach`, etc.)
- Missing `@endsection` or `@endif` closing directives
- Calling a method on a null variable
- Missing view file in `resources/views`

## How to Fix

1. Check the error message for the exact file and line:

```text
ViewException: Undefined variable $user (View: resources/views/users/show.blade.php)
```

2. Use `@isset` or null coalescing for optional variables:

```blade
{{-- Safe access to optional variable --}}
@isset($user)
    <p>Welcome, {{ $user->name }}</p>
@endisset

{{-- Or using null coalescing --}}
<p>Welcome, {{ $user->name ?? 'Guest' }}</p>
```

3. Always pass required data to views:

```php
public function show($id)
{
    $user = User::find($id);

    return view('users.show', [
        'user' => $user,
        'title' => 'User Profile',
    ]);
}
```

4. Use `@error` directive for validation errors:

```blade
<input type="text" name="email" value="{{ old('email') }}">
@error('email')
    <span class="text-red-500">{{ $message }}</span>
@enderror
```

## Examples

```blade
{{-- Missing @endif causes compilation error --}}
@if($showContent)
    <p>{{ $content }}</p>

// ViewException: syntax error, unexpected @endif
```

## Related Errors

- [Route not found]({{< relref "/frameworks/laravel/route-not-found3" >}})
- [Model not found]({{< relref "/frameworks/laravel/laravel-model-not-found" >}})
