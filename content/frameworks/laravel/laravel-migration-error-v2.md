---
title: "Database migration failed"
description: "Laravel database migration fails during execution due to SQL errors, constraint violations, or schema conflicts"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when a Laravel database migration fails during `php artisan migrate`. The underlying database rejects the migration SQL due to schema conflicts, missing dependencies, or constraint violations.

## Common Causes

- Column or table already exists when creating it
- Foreign key references a table that has not been created yet
- Column type mismatch with existing data
- Missing database permissions to alter tables
- Migration file contains invalid SQL syntax

## How to Fix

1. Check migration status before retrying:

```bash
php artisan migrate:status
```

2. Use `Schema::hasTable()` and `Schema::hasColumn()` to avoid duplicate creation:

```php
Schema::create('users', function (Blueprint $table) {
    if (!Schema::hasTable('users')) {
        $table->id();
        $table->string('email')->unique();
        $table->timestamps();
    }
});
```

3. Ensure dependent tables are created first by ordering migrations:

```php
Schema::create('posts', function (Blueprint $table) {
    $table->id();
    $table->foreignId('user_id')->constrained();
    $table->string('title');
    $table->timestamps();
});
```

4. Wrap risky migrations in try-catch for better error handling:

```php
use Illuminate\Database\QueryException;

try {
    Schema::table('orders', function (Blueprint $table) {
        $table->foreign('payment_id')->references('id')->on('payments');
    });
} catch (QueryException $e) {
    Log::error('Migration failed: ' . $e->getMessage());
}
```

5. Rollback and retry after fixing the migration:

```bash
php artisan migrate:rollback
php artisan migrate
```

## Examples

```php
// Migration referencing a table that doesn't exist yet
Schema::table('orders', function (Blueprint $table) {
    $table->foreignId('payment_id')->constrained();
    // QueryException if 'payments' table doesn't exist
});

// Adding a column that already exists
Schema::table('users', function (Blueprint $table) {
    $table->string('email')->unique();
    // QueryException if 'email' column already exists
});
```

## Related Errors

- [Model not found]({{< relref "/frameworks/laravel/laravel-model-not-found-v2" >}})
- [Service container resolution error]({{< relref "/frameworks/laravel/laravel-service-container-v2" >}})
