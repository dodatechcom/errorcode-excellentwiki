---
title: "[Solution] PHP MONGODB_INDEX_ERROR — MongoDB Index Error"
description: "Fix PHP MongoDB index errors. Check index specification, handle duplicate keys, and rebuild indexes. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 110
---

# PHP MONGODB_INDEX_ERROR — MongoDB Index Error

A MongoDB index operation failed. This error occurs when index creation fails due to duplicate key violations, invalid index specifications, excessive index size, or conflicts with existing indexes.

## Common Causes

### Duplicate key error during insert

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

// Create unique index
$command = new MongoDB\Driver\Command([
    'createIndexes' => 'users',
    'indexes' => [
        ['key' => ['email' => 1], 'unique' => true, 'name' => 'email_unique'],
    ],
]);
$manager->executeCommand('myapp', $command);

// Insert duplicate
$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['email' => 'test@example.com', 'name' => 'Alice']);
$bulk->insert(['email' => 'test@example.com', 'name' => 'Bob']); // duplicate
$manager->executeBulkWrite('myapp.users', $bulk);
// E11000 duplicate key error
?>
```

### Invalid index specification

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$command = new MongoDB\Driver\Command([
    'createIndexes' => 'users',
    'indexes' => [
        ['key' => ['name' => 1], 'name' => ''],
    ],
]);
$manager->executeCommand('myapp', $command);
// Index name cannot be empty
?>
```

### Too many indexes on collection

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

// Collection already has 64 indexes (MongoDB limit)
$command = new MongoDB\Driver\Command([
    'createIndexes' => 'users',
    'indexes' => [
        ['key' => ['field65' => 1], 'name' => 'idx_65'],
    ],
]);
$manager->executeCommand('myapp', $command);
// Cannot create index — too many indexes
?>
```

### Index key size exceeds limit

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$command = new MongoDB\Driver\Command([
    'createIndexes' => 'users',
    'indexes' => [
        ['key' => ['largeField' => 1], 'name' => 'large_idx'],
    ],
]);
$manager->executeCommand('myapp', $command);
// Index key exceeds 1024 byte limit
?>
```

### Collation conflict

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$command = new MongoDB\Driver\Command([
    'createIndexes' => 'users',
    'indexes' => [
        [
            'key' => ['name' => 1],
            'name' => 'name_collation',
            'collation' => ['locale' => 'en', 'strength' => 2],
        ],
    ],
]);
$manager->executeCommand('myapp', $command);
// Conflicts with existing index on same field without collation
?>
```

## How to Fix

### Fix 1: Handle Duplicate Key Errors

Check for existing documents before inserting unique values.

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

// Check if document exists first
$query = new MongoDB\Driver\Query(['email' => 'test@example.com'], ['limit' => 1]);
$cursor = $manager->executeQuery('myapp.users', $query);
$existing = $cursor->toArray();

if (!empty($existing)) {
    throw new RuntimeException('User with this email already exists');
}

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['email' => 'test@example.com', 'name' => 'Alice']);
$manager->executeBulkWrite('myapp.users', $bulk);
?>
```

### Fix 2: Create Indexes Safely

Use `createIndex` with proper specifications.

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$command = new MongoDB\Driver\Command([
    'createIndexes' => 'users',
    'indexes' => [
        [
            'key' => ['email' => 1],
            'unique' => true,
            'name' => 'email_unique_idx',
            'background' => true,
        ],
        [
            'key' => ['status' => 1, 'created_at' => -1],
            'name' => 'status_created_idx',
            'sparse' => true,
        ],
        [
            'key' => ['name' => 'text', 'bio' => 'text'],
            'name' => 'text_search_idx',
            'weights' => ['name' => 10, 'bio' => 5],
        ],
    ],
]);

$result = $manager->executeCommand('myapp', $command);
echo "Indexes created successfully" . PHP_EOL;
?>
```

### Fix 3: Drop and Recreate Problematic Indexes

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

// List existing indexes
$listCommand = new MongoDB\Driver\Command(['listIndexes' => 'users']);
$cursor = $manager->executeCommand('myapp', $listCommand);
foreach ($cursor as $index) {
    echo "Index: {$index->name}" . PHP_EOL;
}

// Drop specific index
$dropCommand = new MongoDB\Driver\Command([
    'dropIndexes' => 'users',
    'index' => 'old_email_idx',
]);
$manager->executeCommand('myapp', $dropCommand);

// Recreate with correct specification
$createCommand = new MongoDB\Driver\Command([
    'createIndexes' => 'users',
    'indexes' => [
        [
            'key' => ['email' => 1],
            'unique' => true,
            'name' => 'email_unique_idx',
        ],
    ],
]);
$manager->executeCommand('myapp', $createCommand);
?>
```

### Fix 4: Use Sparse and Partial Indexes

Reduce index size with sparse or partial index filters.

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$command = new MongoDB\Driver\Command([
    'createIndexes' => 'users',
    'indexes' => [
        // Sparse index — only index documents where field exists
        [
            'key' => ['phone' => 1],
            'name' => 'phone_sparse',
            'sparse' => true,
        ],
        // Partial index — only index documents matching filter
        [
            'key' => ['email' => 1],
            'name' => 'active_email_idx',
            'partialFilterExpression' => [
                'status' => 'active',
            ],
        ],
    ],
]);
$manager->executeCommand('myapp', $command);
?>
```

### Fix 5: Rebuild Indexes

Rebuild indexes to defragment and optimize.

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

// Rebuild all indexes on a collection
$command = new MongoDB\Driver\Command([
    'reIndex' => 'users',
]);
$result = $manager->executeCommand('myapp', $command);
echo "Index rebuild complete" . PHP_EOL;

// Check index stats
$statsCommand = new MongoDB\Driver\Command([
    'collStats' => 'users',
    'indexDetails' => true,
]);
$stats = $manager->executeCommand('myapp', $statsCommand);
$statsDoc = current($stats->toArray());

if (isset($statsDoc->indexSizes)) {
    foreach ($statsDoc->indexSizes as $name => $size) {
        echo "Index {$name}: " . round($size / 1024, 2) . " KB" . PHP_EOL;
    }
}
?>
```

## Examples

### Monitor Index Usage

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$command = new MongoDB\Driver\Command([
    'aggregate' => 'users',
    'pipeline' => [
        ['$indexStats' => (object) []],
    ],
    'cursor' => (object) [],
]);

$cursor = $manager->executeCommand('myapp', $command);
foreach ($cursor as $stat) {
    echo "Index: {$stat->name}" . PHP_EOL;
    echo "  Accesses: {$stat->accesses->ops}" . PHP_EOL;
    echo "  Since: " . $stat->accesses->since . PHP_EOL;
}
?>
```

## Related Errors

- [MongoDB Write Error]({{< relref "/languages/php/mongodb-write-error" >}})
- [MongoDB BulkWrite Error]({{< relref "/languages/php/mongodb-bulkwrite-error" >}})
- [MongoDB Query Error]({{< relref "/languages/php/mongodb-query-error" >}})
