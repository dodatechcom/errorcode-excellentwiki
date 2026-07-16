---
title: "Eloquent query error"
description: "Laravel Eloquent throws QueryException when a database query fails due to syntax errors or constraint violations"
frameworks: ["laravel"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["eloquent", "query", "database", "orm", "query-builder"]
weight: 5
---

This error occurs when an Eloquent query or Query Builder method fails, typically due to SQL syntax errors, column not found, or constraint violations.

## Common Causes

- Query references a column that does not exist in the database
- Unique or foreign key constraint violation
- Invalid SQL syntax in raw queries
- Model not migrated (table does not exist)

## How to Fix

1. Check the SQL being generated with `toSql()`:

```php
$query = User::where('email', 'test@example.com');
echo $query->toSql();  // Debug the query
echo $query->count();  // Execute
```

2. Use `try-catch` to handle query exceptions:

```php
use Illuminate\Database\QueryException;

try {
    User::create(['email' => 'test@example.com', 'name' => 'Alice']);
} catch (QueryException $e) {
    if ($e->getCode() === '23000') {
        return response()->json(['error' => 'Email already exists'], 409);
    }
    throw $e;
}
```

3. Use `DB::beginTransaction()` for complex operations:

```php
use Illuminate\Support\Facades\DB;

DB::beginTransaction();
try {
    Account::where('id', 1)->decrement('balance', 100);
    Account::where('id', 2)->increment('balance', 100);
    DB::commit();
} catch (\Exception $e) {
    DB::rollBack();
    throw $e;
}
```

## Examples

```php
// Column does not exist
User::where('emal', 'test@example.com')->first();
// QueryException: SQLSTATE[42S22]: Column not found: 1054 Unknown column 'emal'
```

## Related Errors

- [Method not found on instance]({{< relref "/frameworks/laravel/method-not-found" >}})
