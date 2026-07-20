---
title: "[Solution] PHP LARAVEL_MASS_ASSIGNMENT_ERROR — Laravel MassAssignmentException"
description: "Fix PHP Laravel MassAssignmentException. Define $fillable/$guarded, check model configuration, and handle mass assignment safely. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 119
---

# PHP LARAVEL_MASS_ASSIGNMENT_ERROR — Laravel MassAssignmentException

Laravel prevented a mass assignment operation because the model's `$fillable` or `$guarded` properties are not configured. This is a security feature that blocks untrusted data from being mass-assigned to sensitive model attributes.

## Common Causes

### No $fillable or $guarded defined

```php
<?php
class User extends Model
{
    // No $fillable or $guarded defined
}

$user = User::create(['name' => 'Alice', 'email' => 'alice@example.com']);
// Illuminate\Database\Eloquent\MassAssignmentException
?>
```

### Using create() without $fillable

```php
<?php
class User extends Model
{
    protected $fillable = ['name']; // email not in fillable
}

$user = User::create([
    'name' => 'Alice',
    'email' => 'alice@example.com', // not fillable
]);
// MassAssignmentException — email is guarded
?>
```

### fill() called with guarded attributes

```php
<?php
class User extends Model
{
    protected $fillable = ['name', 'email'];
    protected $guarded = ['role', 'is_admin'];
}

$user = new User();
$user->fill(['name' => 'Alice', 'role' => 'admin', 'is_admin' => true]);
// MassAssignmentException — role and is_admin are guarded
?>
```

### Using update() with unguarded fields

```php
<?php
class User extends Model
{
    protected $fillable = ['name', 'email'];
}

$user = User::find(1);
$user->update(['name' => 'Bob', 'password' => 'newpass']);
// MassAssignmentException — password is not fillable
?>
```

### Request data contains unexpected fields

```php
<?php
class User extends Model
{
    protected $fillable = ['name', 'email'];
}

$user = User::create($request->all());
// MassAssignmentException — request may contain unexpected fields
?>
```

## How to Fix

### Fix 1: Define $fillable for Safe Mass Assignment

Whitelist only the attributes that can be mass-assigned.

```php
<?php
class User extends Model
{
    protected $fillable = [
        'name',
        'email',
        'password',
        'bio',
        'avatar_url',
    ];
}

// Now create() works
$user = User::create([
    'name' => 'Alice',
    'email' => 'alice@example.com',
    'password' => Hash::make('secret'),
]);

// update() also works
$user->update(['name' => 'Bob']);

// fill() works
$user = new User();
$user->fill(['name' => 'Charlie', 'email' => 'charlie@example.com']);
$user->save();
?>
```

### Fix 2: Use $guarded to Block Specific Attributes

Blacklist attributes that should never be mass-assigned.

```php
<?php
class User extends Model
{
    // Protect only sensitive fields — everything else is fillable
    protected $guarded = [
        'id',
        'role',
        'is_admin',
        'email_verified_at',
        'remember_token',
        'created_at',
        'updated_at',
    ];
}

// All non-guarded attributes can be mass-assigned
$user = User::create([
    'name' => 'Alice',
    'email' => 'alice@example.com',
    'bio' => 'Developer',
]);
?>
```

### Fix 3: Filter Request Data Before Creating

Use validated data instead of raw request input.

```php
<?php
class UserController extends Controller
{
    public function store(Request $request)
    {
        $validated = $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|email|unique:users,email',
            'password' => 'required|string|min:8|confirmed',
            'bio' => 'nullable|string|max:1000',
        ]);

        $validated['password'] = Hash::make($validated['password']);

        $user = User::create($validated);
        return redirect()->route('users.show', $user);
    }

    public function update(Request $request, User $user)
    {
        $validated = $request->validate([
            'name' => 'sometimes|string|max:255',
            'email' => "sometimes|email|unique:users,email,{$user->id}",
            'bio' => 'nullable|string|max:1000',
        ]);

        $user->update($validated);
        return redirect()->route('users.show', $user);
    }
}
?>
```

### Fix 4: Use Force Fill for Admin Operations

Override guarded attributes temporarily when needed.

```php
<?php
class UserController extends Controller
{
    public function promote(Request $request, User $user)
    {
        // Admin-only operation — use forceFill
        $user->forceFill([
            'role' => $request->input('role'),
            'is_admin' => true,
        ])->save();

        return back()->with('success', 'User promoted');
    }

    public function destroy(Request $request, User $user)
    {
        $user->forceDelete();
        return redirect()->route('users.index');
    }
}
?>
```

### Fix 5: Conditional $fillable Based on Context

```php
<?php
class User extends Model
{
    protected $fillable = [
        'name',
        'email',
        'password',
        'bio',
        'avatar_url',
    ];

    // Methods that need access to guarded fields
    public function promoteToAdmin(): void
    {
        $this->forceFill(['role' => 'admin', 'is_admin' => true])->save();
    }

    public function demoteToUser(): void
    {
        $this->forceFill(['role' => 'user', 'is_admin' => false])->save();
    }
}

// In controller
$user = User::find($id);
$user->promoteToAdmin();
?>
```

## Examples

### Complete Model with $fillable

```php
<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class Article extends Model
{
    use SoftDeletes;

    protected $fillable = [
        'title',
        'slug',
        'content',
        'excerpt',
        'status',
        'published_at',
        'author_id',
    ];

    protected $guarded = [
        'id',
        'views_count',
        'created_at',
        'updated_at',
    ];

    protected $casts = [
        'published_at' => 'datetime',
        'status' => 'string',
    ];

    public function author()
    {
        return $this->belongsTo(User::class);
    }
}

// Usage
$article = Article::create([
    'title' => 'Hello World',
    'slug' => 'hello-world',
    'content' => 'Content here',
    'status' => 'draft',
]);
?>
```

## Related Errors

- [Laravel Model Not Found]({{< relref "/languages/php/laravel-model-not-found" >}})
- [Laravel Validation Error]({{< relref "/languages/php/laravel-validation-error" >}})
- [Laravel Eloquent Error]({{< relref "/languages/php/laravel-eloquent-error" >}})
