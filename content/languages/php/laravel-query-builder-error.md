---
title: "[Solution] PHP LARAVEL_QUERY_BUILDER_ERROR — Laravel QueryBuilder Error"
description: "Fix PHP Laravel QueryBuilder errors. Check SQL syntax, verify table names, and handle bindings. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 121
---

# PHP LARAVEL_QUERY_BUILDER_ERROR — Laravel QueryBuilder Error

A Laravel QueryBuilder operation failed due to invalid SQL, missing tables, incorrect column references, or binding mismatches. This error is thrown by the database layer when the generated SQL is rejected by the database server.

## Common Causes

### Column does not exist

```php
<?php
$users = DB::table('users')
    ->where('nonexistent_column', 'value')
    ->get();
// SQLSTATE[42S22]: Column not found: 1054 Unknown column 'nonexistent_column'
?>
```

### Table does not exist

```php
<?php
$users = DB::table('nonexistent_table')
    ->where('id', 1)
    ->get();
// SQLSTATE[42S02]: Base table or view not found: 1146 Table doesn't exist
?>
```

### Raw expression with wrong binding count

```php
<?php
$users = DB::select(
    'SELECT * FROM users WHERE id = ? AND status = ?',  // 2 placeholders
    [1]  // only 1 binding
);
// PDOException: SQLSTATE[HY093]: Invalid parameter number
?>
```

### Wrong join syntax

```php
<?php
$users = DB::table('users')
    ->join('posts', 'users.id', '=', 'posts.user_id', 'AND')
    ->get();
// SQL syntax error near 'AND'
?>
```

### Union with mismatched columns

```php
<?php
$admins = DB::table('admins')->select('id', 'name');
$users = DB::table('users')->select('id', 'email');
$result = $admins->union($users)->get();
// Column count mismatch — different number of columns in SELECT
?>
```

## How to Fix

### Fix 1: Verify Column and Table Names

Check database schema before querying.

```php
<?php
// Check if column exists
$hasColumn = Schema::hasColumn('users', 'email');
if (!$hasColumn) {
    throw new RuntimeException("Column 'email' does not exist in users table");
}

// Check if table exists
$hasTable = Schema::hasTable('users');
if (!$hasTable) {
    throw new RuntimeException("Table 'users' does not exist");
}

// List all columns in table
$columns = Schema::getColumnListing('users');
echo implode(', ', $columns);
?>
```

### Fix 2: Use Parameterized Queries

Always use bindings to prevent SQL errors and injection.

```php
<?php
// Correct — parameterized
$users = DB::table('users')
    ->where('id', '=', 1)
    ->where('status', '=', 'active')
    ->get();

// Correct — multiple conditions
$users = DB::table('users')
    ->where('age', '>=', 18)
    ->where('email', 'LIKE', '%@example.com')
    ->whereNull('deleted_at')
    ->get();

// Wrong — string interpolation
$email = 'test@example.com';
$users = DB::table('users')
    ->whereRaw("email = '{$email}'") // SQL injection risk
    ->get();
?>
```

### Fix 3: Handle Binding Mismatches

Ensure binding count matches placeholder count.

```php
<?php
// Correct — raw query with proper bindings
$results = DB::select(
    'SELECT * FROM users WHERE id = ? AND status = ?',
    [1, 'active']
);

// Correct — use named bindings
$results = DB::select(
    'SELECT * FROM users WHERE id = :id AND status = :status',
    ['id' => 1, 'status' => 'active']
);

// Correct — use DB::raw for expressions
$users = DB::table('users')
    ->select(DB::raw('COUNT(*) as total, status'))
    ->groupBy('status')
    ->get();
?>
```

### Fix 4: Write Correct Joins

```php
<?php
// Simple join
$users = DB::table('users')
    ->join('posts', 'users.id', '=', 'posts.user_id')
    ->select('users.name', 'posts.title')
    ->get();

// Left join
$users = DB::table('users')
    ->leftJoin('posts', 'users.id', '=', 'posts.user_id')
    ->select('users.name', DB::raw('COUNT(posts.id) as post_count'))
    ->groupBy('users.id', 'users.name')
    ->get();

// Cross join
$products = DB::table('colors')
    ->crossJoin('sizes')
    ->get();

// Join with multiple conditions
$orders = DB::table('orders')
    ->join('order_items', function ($join) {
        $join->on('orders.id', '=', 'order_items.order_id')
             ->where('order_items.quantity', '>', 0);
    })
    ->get();
?>
```

### Fix 5: Use Aggregate Methods Safely

```php
<?php
// Count
$count = DB::table('users')->where('status', 'active')->count();

// Sum
$total = DB::table('orders')->where('user_id', $userId)->sum('amount');

// Average
$avg = DB::table('reviews')->where('product_id', $productId)->avg('rating');

// Group by with having
$results = DB::table('orders')
    ->select('user_id', DB::raw('COUNT(*) as order_count'))
    ->groupBy('user_id')
    ->having('order_count', '>=', 5)
    ->get();
?>
```

## Examples

### Complete Query Example

```php
<?php
function searchUsers(array $filters): \Illuminate\Support\Collection
{
    $query = DB::table('users')
        ->select('users.*', DB::raw('COUNT(orders.id) as order_count'))
        ->leftJoin('orders', 'users.id', '=', 'orders.user_id')
        ->groupBy('users.id');

    if (!empty($filters['status'])) {
        $query->where('users.status', $filters['status']);
    }

    if (!empty($filters['min_orders'])) {
        $query->having('order_count', '>=', $filters['min_orders']);
    }

    if (!empty($filters['search'])) {
        $query->where(function ($q) use ($filters) {
            $q->where('users.name', 'LIKE', "%{$filters['search']}%")
              ->orWhere('users.email', 'LIKE', "%{$filters['search']}%");
        });
    }

    return $query->orderByDesc('order_count')->paginate(20);
}

$users = searchUsers(['status' => 'active', 'min_orders' => 3]);
?>
```

## Related Errors

- [Laravel Eloquent Error]({{< relref "/languages/php/laravel-eloquent-error" >}})
- [Laravel Model Not Found]({{< relref "/languages/php/laravel-model-not-found" >}})
- [PDO Connection Error]({{< relref "/languages/php/pdo-connection-error" >}})
