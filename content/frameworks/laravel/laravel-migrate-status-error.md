---
title: "[Solution] Laravel Migration Status Error"
description: "Fix Laravel migrate status shows not found or wrong database. Resolve migration tracking inconsistencies in Laravel."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when `php artisan migrate:status` shows migrations as not run even though the tables exist, or shows incorrect status.

## Common Causes

- Migrations were run on a different database connection than the one being checked
- `migrations` table was deleted or corrupted
- Multiple environments share the same database
- Migration file was renamed after being run
- Database prefix mismatch between config and actual database

## How to Fix

1. Specify the correct connection:

```bash
php artisan migrate:status --database=mysql
```

2. Recreate the migrations table manually:

```php
Schema::create('migrations', function (Blueprint $table) {
    $table->id();
    $table->string('migration');
    $table->integer('batch');
    $table->timestamp('migration_run_at')->nullable();
});
```

3. Mark specific migrations as complete:

```php
DB::table('migrations')->insert([
    'migration' => '2024_01_15_create_orders_table',
    'batch' => 1,
    'migration_run_at' => now(),
]);
```

4. Use a consistent database connection in `.env`:

```text
DB_CONNECTION=mysql
DB_DATABASE=laravel_app
```

## Examples

```bash
# Status shows all migrations as pending despite tables existing
$ php artisan migrate:status
| Migration                | Ran? |
|--------------------------|------|
| 2024_01_01_create_users  | No   |   # but users table exists!

# Fix: insert into migrations table
DB::table('migrations')->insert([
    'migration' => '2024_01_01_create_users_table',
    'batch' => 1,
]);
```
