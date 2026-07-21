---
title: "[Solution] Laravel Eloquent Undefined Relation Error"
description: "Fix Laravel Call to undefined relationship on model. Resolve undefined Eloquent relationship method errors."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when you try to eager-load or access a relationship that is not defined on the Eloquent model.

## Common Causes

- Relationship method name is misspelled in `with()` or `load()`
- Method exists but does not return a relationship instance
- Model was recently updated and the method was removed or renamed
- Relationship defined on a different model and called on the wrong one
- Using `belongsTo` instead of `hasMany` or vice versa

## How to Fix

1. Verify the relationship method exists on the model:

```php
class User extends Model
{
    public function posts(): HasMany
    {
        return $this->hasMany(Post::class);
    }
}
```

2. Check the method returns the correct relationship type:

```php
// Wrong: returns a query builder instead of a relationship
public function posts()
{
    return Post::where('user_id', $this->id); // BAD
}

// Correct: returns a HasMany instance
public function posts(): HasMany
{
    return $this->hasMany(Post::class);
}
```

3. Use `load` to lazy-load after the query:

```php
$users = User::all();
$users->load('posts'); // loads relationship on collection
```

4. Check for typo in the relationship name:

```php
// Method is "posts" not "post"
User::with('posts')->get(); // correct
User::with('post')->get();  // undefined relationship "post"
```

## Examples

```php
// Calling undefined relationship
User::with('orders')->get();
// BadMethodCallException: Call to undefined relationship [orders] on model [App\Models\User]

// Method does not return a relationship
class Order extends Model
{
    public function customer()
    {
        return Customer::find($this->customer_id); // BAD
    }
}
```
