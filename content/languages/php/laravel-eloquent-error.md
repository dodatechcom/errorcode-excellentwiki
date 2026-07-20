---
title: "[Solution] PHP LARAVEL_ELOQUENT_ERROR — Laravel Eloquent Model Error"
description: "Fix PHP Laravel Eloquent model errors. Check relationships, verify attributes, and handle casting. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 122
---

# PHP LARAVEL_ELOQUENT_ERROR — Laravel Eloquent Model Error

An Eloquent model operation failed. This error occurs when attributes are accessed incorrectly, model casting is misconfigured, relationships are undefined, or the model's table/connection configuration is wrong.

## Common Causes

### Accessing undefined attribute

```php
<?php
class User extends Model {}

$user = User::find(1);
echo $user->nonexistent_field;
// Trying to get property of non-object or null
?>
```

### Wrong cast type

```php
<?php
class User extends Model
{
    protected $casts = [
        'settings' => 'json',
        'active' => 'boolean',
        'price' => 'decimal:2',
    ];
}

$user = User::find(1);
$user->settings = 'not json'; // will fail on decode
// TypeError or JsonException
?>
```

### Model not using correct table

```php
<?php
class BlogPost extends Model
{
    // Missing $table — Laravel infers 'blog_posts' (not 'posts')
}

$posts = BlogPost::all(); // queries 'blog_posts' table
// SQLSTATE[42S02]: Base table or view not found
?>
```

### Accessing property on null model

```php
<?php
$user = User::where('email', 'missing@example.com')->first();
echo $user->name;
// Trying to get property 'name' of non-object
?>
```

### Type mismatch in attribute

```php
<?php
class Order extends Model
{
    protected $casts = [
        'total' => 'decimal:2',
    ];
}

$order = Order::find(1);
$order->total = 'not a number'; // cast fails
?>
```

## How to Fix

### Fix 1: Access Attributes Safely

Check for existence before accessing model properties.

```php
<?php
// Safe access with exists check
$user = User::find(1);
if ($user) {
    echo $user->name;
}

// Use optional helper
$name = optional(User::find(1))->name;

// Null-safe operator (PHP 8+)
$name = User::find(1)?->name;

// Use attribute accessor
class User extends Model
{
    public function getNameAttribute($value)
    {
        return ucfirst($value);
    }

    public function getFullNameAttribute()
    {
        return "{$this->first_name} {$this->last_name}";
    }
}

echo $user->name; // calls accessor
echo $user->full_name; // computed attribute
?>
```

### Fix 2: Define Correct Model Properties

```php
<?php
class Post extends Model
{
    // Table name
    protected $table = 'posts';

    // Primary key
    protected $primaryKey = 'post_id';
    public $incrementing = true;
    protected $keyType = 'int';

    // Timestamps
    public $timestamps = true;
    const CREATED_AT = 'created_at';
    const UPDATED_AT = 'updated_at';

    // Connection
    protected $connection = 'mysql';

    // Fillable attributes
    protected $fillable = ['title', 'content', 'status'];

    // Casts
    protected $casts = [
        'published_at' => 'datetime',
        'metadata' => 'json',
        'is_published' => 'boolean',
    ];
}
?>
```

### Fix 3: Handle Null Models

```php
<?php
// Use find() with null check
$user = User::find($id);
if (!$user) {
    return response()->json(['error' => 'User not found'], 404);
}

// Use firstOrFail() for automatic 404
$user = User::where('email', $email)->firstOrFail();

// Use first() with optional
$name = User::where('email', $email)->first()?->name ?? 'Unknown';

// In controllers, use route model binding (auto 404)
public function show(User $user)
{
    return view('users.show', compact('user'));
}
?>
```

### Fix 4: Validate and Cast Attributes

```php
<?php
class Product extends Model
{
    protected $fillable = ['name', 'price', 'quantity', 'metadata'];

    protected $casts = [
        'price' => 'decimal:2',
        'quantity' => 'integer',
        'metadata' => 'json',
        'is_active' => 'boolean',
        'published_at' => 'datetime',
    ];

    // Attribute mutator
    public function setNameAttribute($value)
    {
        $this->attributes['name'] = strtolower(trim($value));
    }

    public function getNameAttribute($value)
    {
        return ucfirst($value);
    }

    // Custom cast via method
    public function setPriceAttribute($value)
    {
        $this->attributes['price'] = round((float) $value, 2);
    }
}

$product = new Product();
$product->name = '  WIDGET  '; // mutator trims and lowercases
$product->price = '19.999'; // rounds to 19.99
$product->save();
?>
```

### Fix 5: Handle Model Events and Exceptions

```php
<?php
class User extends Model
{
    protected static function booted(): void
    {
        static::creating(function (User $user) {
            if (empty($user->slug)) {
                $user->slug = Str::slug($user->name);
            }
        });

        static::updating(function (User $user) {
            // Prevent updating certain fields
            if ($user->isDirty('role') && !auth()->user()->is_admin) {
                throw new \Exception('Only admins can change roles');
            }
        });
    }
}

// Wrap operations in try-catch
try {
    $user = User::create(['name' => 'Alice', 'email' => 'alice@example.com']);
} catch (\Exception $e) {
    Log::error('User creation failed: ' . $e->getMessage());
    throw $e;
}
?>
```

## Examples

### Complete Eloquent Model

```php
<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;
use Illuminate\Support\Str;

class Product extends Model
{
    use SoftDeletes;

    protected $table = 'products';
    protected $fillable = ['name', 'slug', 'description', 'price', 'category_id'];
    protected $casts = [
        'price' => 'decimal:2',
        'metadata' => 'json',
        'is_active' => 'boolean',
    ];

    public static function boot(): void
    {
        parent::boot();
        static::creating(function ($product) {
            $product->slug = $product->slug ?: Str::slug($product->name);
        });
    }

    public function category()
    {
        return $this->belongsTo(Category::class);
    }

    public function getNameAttribute($value)
    {
        return ucfirst($value);
    }

    public function getFormattedPriceAttribute()
    {
        return '$' . number_format($this->price, 2);
    }
}

$product = Product::with('category')->find(1);
echo $product->name;
echo $product->formatted_price;
?>
```

## Related Errors

- [Laravel Mass Assignment Error]({{< relref "/languages/php/laravel-mass-assignment-error" >}})
- [Laravel Model Not Found]({{< relref "/languages/php/laravel-model-not-found" >}})
- [Laravel Eloquent Relationship Error]({{< relref "/languages/php/laravel-eloquent-relationship-error" >}})
