---
title: "Method X does not exist on instance"
description: "Laravel throws this error via PHP when you call a method that is not defined on the object or class instance."
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["methods", "objects", "eloquent", "php"]
weight: 5
---

This error occurs when you call a method on an object that does not have that method defined. In Laravel projects it frequently happens with Eloquent models when accessing relationships via method syntax without defining them, or when using a Facade that resolves to an unexpected class.

## Common Causes

- Calling a relationship method (e.g. `$user->posts()`) without defining it on the model
- Using an outdated package version where a method was removed or renamed
- Calling a method on a Facade that resolves to a different underlying class than expected
- Typo in the method name

## How to Fix

Define the relationship method on the Eloquent model:

```php
// app/Models/User.php
class User extends Model
{
    public function posts()
    {
        return $this->hasMany(Post::class);
    }
}
```

Verify the method exists on the class:

```bash
php artisan tinker
>>> $user = App\Models\User::first();
>>> get_class_methods($user);
```

If using a Facade, check the underlying class:

```php
// Verify what the facade resolves to
$realClass = get_class(Cache::getFacadeRoot());
```

## Example

```php
$user = App\Models\User::first();
$posts = $user->posts;  // Trying to access as property, but posts() is not defined
```

```text
Error: Call to undefined method App\Models\User::posts()
```

## Related Errors

- [Class 'X' not found]({{< relref "/frameworks/laravel/class-not-found" >}})
