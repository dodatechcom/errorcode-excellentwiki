---
title: "[Solution] PHP LARAVEL_MODEL_NOT_FOUND — Model Not Found by ID"
description: "Fix PHP LARAVEL_MODEL_NOT_FOUND by using findOrFail() correctly, checking table/data, and handling ModelNotFoundException. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 120
---

# PHP LARAVEL_MODEL_NOT_FOUND — Model Not Found by ID

A model was not found by its ID in Laravel. This error occurs when `findOrFail()`, `firstOrFail()`, or route model binding cannot locate the specified record in the database.

## Common Causes

```php
// Model ID doesn't exist in database
$user = User::findOrFail(999); // ID 999 doesn't exist
```

```php
// Wrong table name or model configuration
class Post extends Model
{
    protected $table = 'blog_posts'; // table name mismatch
}
```

```php
// Route model binding with wrong parameter name
Route::get('/user/{id}', [UserController::class, 'show']);
// But controller expects {user} not {id}
public function show(User $user) { }
```

```php
// Soft-deleted model being queried
$user = User::find(1); // returns null if soft-deleted
```

```php
// Database table is empty or truncated
Post::findOrFail(1); // table has no records
```

## How to Fix

### Fix 1: Use findOrFail() Correctly

```php
// Basic usage — throws ModelNotFoundException if not found
$user = User::findOrFail($id);

// Catch the exception
try {
    $user = User::findOrFail($id);
} catch (\Illuminate\Database\Eloquent\ModelNotFoundException $e) {
    abort(404, 'User not found');
    // Or return response
    return response()->json(['error' => 'User not found'], 404);
}

// Use find() and handle null
$user = User::find($id);
if (!$user) {
    return response()->json(['error' => 'User not found'], 404);
}

// Route model binding (automatic 404)
Route::get('/user/{user}', [UserController::class, 'show']);

public function show(User $user)
{
    // $user is automatically resolved, 404 if not found
    return view('user.show', compact('user'));
}
```

### Fix 2: Check Table and Model Configuration

```php
// Verify model table name
class Post extends Model
{
    protected $table = 'posts'; // must match actual table name

    // Or let Laravel infer from class name (Post -> posts)
    // Don't set $table if using convention
}

// Check if table exists
if (!Schema::hasTable('posts')) {
    Log::error('Table posts does not exist');
    Artisan::call('migrate');
}

// Verify model connection
class Post extends Model
{
    protected $connection = 'mysql'; // must match config/database.php connection

    protected $primaryKey = 'id';
    public $incrementing = true;
    protected $keyType = 'int';
}
```

### Fix 3: Handle Soft-Deleted Models

```php
// Include soft-deleted models
$user = User::withTrashed()->find($id);

// Only soft-deleted models
$deletedUsers = User::onlyTrashed()->get();

// Restore soft-deleted model
$user = User::withTrashed()->find($id);
$user->restore();

// Force delete (permanent)
$user->forceDelete();

// In controller
public function show($id)
{
    $user = User::withTrashed()->find($id);

    if (!$user) {
        abort(404);
    }

    if ($user->trashed()) {
        return response()->json([
            'error' => 'User has been deleted',
            'deleted_at' => $user->deleted_at,
        ], 410); // Gone
    }

    return view('user.show', compact('user'));
}
```

### Fix 4: Verify Route Model Binding

```php
// Route definition
Route::get('/user/{user}', [UserController::class, 'show']);

// Controller — parameter name must match route parameter
class UserController extends Controller
{
    public function show(User $user) // $user matches {user} in route
    {
        return view('user.show', compact('user'));
    }
}

// Custom key binding
Route::get('/user/{user:email}', [UserController::class, 'show']);

// Or in model
class User extends Model
{
    public function getRouteKeyName(): string
    {
        return 'slug'; // use slug instead of id
    }
}

// Composite key binding
Route::get('/user/{user:id}/{post:slug}', [UserController::class, 'showPost']);
```

## Examples

```php
// Complete controller with proper model handling
class PostController extends Controller
{
    public function show($id)
    {
        $post = Post::find($id);

        if (!$post) {
            if (request()->expectsJson()) {
                return response()->json([
                    'error' => 'Post not found',
                ], 404);
            }

            abort(404, 'Post not found');
        }

        return view('posts.show', compact('post'));
    }

    public function update(Request $request, $id)
    {
        $post = Post::findOrFail($id);

        $validated = $request->validate([
            'title' => 'required|max:255',
            'content' => 'required',
        ]);

        $post->update($validated);

        return redirect()->route('posts.show', $post)
            ->with('success', 'Post updated successfully');
    }

    public function destroy($id)
    {
        $post = Post::withTrashed()->find($id);

        if (!$post) {
            abort(404);
        }

        $post->delete();

        return redirect()->route('posts.index')
            ->with('success', 'Post deleted');
    }
}
```

## Related Errors

- [CodeIgniter Model Error](/languages/php/codeigniter-model-error)
- [Laravel Route Not Found](/languages/php/laravel-route-not-found)
- [Laravel Validation Error](/languages/php/laravel-validation-error)
- [Symfony Route Error](/languages/php/symfony-route-error)
