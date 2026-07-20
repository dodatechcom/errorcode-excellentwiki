---
title: "[Solution] PHP LARAVEL_MIGRATION_ERROR — Migration Failed"
description: "Fix PHP LARAVEL_MIGRATION_ERROR by checking migration syntax, verifying column types, and handling database constraints. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 122
---

# PHP LARAVEL_MIGRATION_ERROR — Migration Failed

A migration operation failed in Laravel. This error occurs when migration syntax is incorrect, column types are invalid, or database constraints prevent the operation.

## Common Causes

```php
// Wrong column type
$table->string('age'); // should be integer for age
$table->integer('email'); // should be string for email
```

```php
// Adding column that already exists
$table->string('name');
$table->string('name'); // duplicate column
```

```php
// Missing foreign key reference
$table->foreignId('user_id');
$table->foreign('user_id')->references('id')->on('users');
// But users table doesn't exist yet
```

```php
// Invalid migration class name
class create_users_table extends Migration // should be CreateUsersTable
```

```php
// Down method tries to drop non-existent column
public function down()
{
    $table->dropColumn('nonexistent_column');
}
```

## How to Fix

### Fix 1: Check Migration Syntax

```php
// Correct migration structure
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('email')->unique();
            $table->timestamp('email_verified_at')->nullable();
            $table->string('password');
            $table->rememberToken();
            $table->timestamps();
            $table->softDeletes();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('users');
    }
};
```

### Fix 2: Use Correct Column Types

```php
// Available column types
$table->id(); // auto-incrementing big integer
$table->bigIncrements('id'); // same as id()
$table->integer('age');
$table->smallInteger('count');
$table->tinyInteger('status');
$table->unsignedBigInteger('user_id');
$table->decimal('price', 8, 2);
$table->float('rating');
$table->double('latitude', 10, 7);
$table->boolean('active');
$table->string('name', 100); // varchar(100)
$table->text('description');
$table->longText('content');
$table->json('metadata');
$table->date('birth_date');
$table->time('start_time');
$table->datetime('created_at');
$table->timestamp('updated_at');
$table->binary('data');
$table->uuid('uuid');
$table->foreignUuid('user_id')->constrained();
$table->morphs('commentable'); // creates type and id columns
$table->nullableMorphs('taggable');
$table->enum('status', ['draft', 'published', 'archived']);
$table->ipAddress('ip_address');
$table->macAddress('mac_address');
$table->year('birth_year');

// Modifiers
$table->string('name')->nullable();
$table->string('name')->default('unknown');
$table->string('name')->unique();
$table->string('name')->index();
$table->string('name')->collation('utf8mb4_unicode_ci');
$table->string('name')->charset('utf8mb4');
$table->string('email')->after('name'); // column position
$table->string('first_name')->first(); // first column
```

### Fix 3: Handle Foreign Key Constraints

```php
// Create tables in correct order
// First create referenced tables, then tables with foreign keys

Schema::create('users', function (Blueprint $table) {
    $table->id();
    $table->string('name');
    $table->string('email')->unique();
    $table->timestamps();
});

Schema::create('posts', function (Blueprint $table) {
    $table->id();
    $table->foreignId('user_id')
          ->constrained('users')
          ->onDelete('cascade')
          ->onUpdate('cascade');
    $table->string('title');
    $table->text('body');
    $table->timestamps();
});

// Drop foreign keys before dropping tables
Schema::dropIfExists('posts');
Schema::dropIfExists('users');
```

### Fix 4: Safe Migration Operations

```php
// Wrap in transaction
public function up(): void
{
    Schema::create('orders', function (Blueprint $table) {
        $table->id();
        $table->foreignId('user_id')->constrained();
        $table->decimal('total', 10, 2);
        $table->timestamps();
    });
}

// Check if column exists before adding
public function up(): void
{
    Schema::table('users', function (Blueprint $table) {
        if (!Schema::hasColumn('users', 'phone')) {
            $table->string('phone')->nullable()->after('email');
        }
    });
}

// Check if table exists
public function up(): void
{
    if (!Schema::hasTable('settings')) {
        Schema::create('settings', function (Blueprint $table) {
            $table->id();
            $table->string('key')->unique();
            $table->text('value')->nullable();
            $table->timestamps();
        });
    }
}
```

## Examples

```php
// Complete migration example
return new class extends Migration
{
    public function up(): void
    {
        Schema::create('products', function (Blueprint $table) {
            $table->id();
            $table->foreignId('category_id')
                  ->constrained('categories')
                  ->onDelete('restrict');
            $table->string('name');
            $table->string('slug')->unique();
            $table->text('description')->nullable();
            $table->decimal('price', 10, 2);
            $table->integer('stock')->default(0);
            $table->boolean('is_active')->default(true);
            $table->json('attributes')->nullable();
            $table->timestamps();
            $table->softDeletes();

            $table->index(['category_id', 'is_active']);
            $table->fullText(['name', 'description']);
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('products');
    }
};

// Rollback migration
// php artisan migrate:rollback
// php artisan migrate:rollback --step=5
// php artisan migrate:fresh --seed
```

## Related Errors

- [PDO Error](/languages/php/pdo-error)
- [PDO Connection Error](/languages/php/pdo-connection-error)
- [CodeIgniter Database Error](/languages/php/codeigniter-database-error)
- [Doctrine Migration Error](/languages/php/doctrine-migration)
