---
title: "[Solution] PHP MONGODB_QUERY_ERROR — MongoDB Query Error"
description: "Fix PHP MongoDB query errors. Check query syntax, verify collection, and handle BSON types. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 107
---

# PHP MONGODB_QUERY_ERROR — MongoDB Query Error

A MongoDB query failed due to invalid syntax, a missing collection, unsupported BSON types, or operator misuse. This error typically occurs when the query document is malformed or references non-existent fields.

## Common Causes

### Invalid query operator

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');
$filter = ['age' => ['$invalidOp' => 25]];
$query = new MongoDB\Driver\Query($filter);
$manager->executeQuery('myapp.users', $query);
// Syntax error in query operator
?>
```

### Missing collection

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');
$filter = ['status' => 'active'];
$query = new MongoDB\Driver\Query($filter);
$manager->executeQuery('myapp.nonexistent_collection', $query);
// Returns empty result set — collection does not exist
?>
```

### Unsupported BSON type in query

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');
$resource = fopen('php://memory', 'r');
$filter = ['file' => $resource]; // resource is not a valid BSON type
$query = new MongoDB\Driver\Query($filter);
$manager->executeQuery('myapp.files', $query);
// Exception — resource cannot be serialized to BSON
?>
```

### Wrong field type comparison

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');
$filter = ['_id' => '507f1f77bcf86cd799439011']; // string instead of ObjectId
$query = new MongoDB\Driver\Query($filter);
$cursor = $manager->executeQuery('myapp.users', $query);
// Returns empty — comparing string to ObjectId
?>
```

### Malformed aggregation pipeline

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');
$pipeline = [
    ['$group' => ['_id' => '$_id']], // missing dollar sign for accumulator
];
$command = new MongoDB\Driver\Command([
    'aggregate' => 'users',
    'pipeline' => $pipeline,
    'cursor' => (object) [],
]);
$manager->executeCommand('myapp', $command);
// Aggregation error — invalid pipeline stage
?>
```

## How to Fix

### Fix 1: Validate Query Syntax

Use the MongoDB library's BSON document for safe query construction.

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

// Use correct operators
$filter = ['age' => ['$gte' => 18, '$lte' => 65]];
$options = [
    'projection' => ['name' => 1, 'email' => 1, '_id' => 0],
    'sort' => ['name' => 1],
    'limit' => 50,
];

$query = new MongoDB\Driver\Query($filter, $options);
$cursor = $manager->executeQuery('myapp.users', $query);

foreach ($cursor as $document) {
    echo $document->name . PHP_EOL;
}
?>
```

### Fix 2: Use Correct BSON Types

Convert PHP types to their MongoDB equivalents for queries.

```php
<?php
use MongoDB\BSON\ObjectId;
use MongoDB\BSON\UTCDateTime;

$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

// Correct ObjectId
$filter = ['_id' => new ObjectId('507f1f77bcf86cd799439011')];
$query = new MongoDB\Driver\Query($filter);
$cursor = $manager->executeQuery('myapp.users', $query);

// Date range query
$filter = [
    'created_at' => [
        '$gte' => new UTCDateTime(strtotime('-30 days') * 1000),
        '$lte' => new UTCDateTime(),
    ],
];
$query = new MongoDB\Driver\Query($filter);
$cursor = $manager->executeQuery('myapp.users', $query);
?>
```

### Fix 3: Check Collection Exists Before Querying

```php
<?php
function collectionExists(MongoDB\Driver\Manager $manager, string $database, string $collection): bool
{
    $command = new MongoDB\Driver\Command([
        'listCollections' => 1,
        'filter' => ['name' => $collection],
    ]);
    $cursor = $manager->executeCommand($database, $command);
    $result = current($cursor->toArray());
    return isset($result->cursor->firstBatch) && count($result->cursor->firstBatch) > 0;
}

$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

if (!collectionExists($manager, 'myapp', 'users')) {
    throw new RuntimeException('Collection users does not exist');
}

$query = new MongoDB\Driver\Query(['status' => 'active']);
$manager->executeQuery('myapp.users', $query);
?>
```

### Fix 4: Validate Aggregation Pipelines

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$pipeline = [
    ['$match' => ['status' => 'active']],
    ['$group' => [
        '_id' => '$department',
        'count' => ['$sum' => 1],
        'avgAge' => ['$avg' => '$age'],
    ]],
    ['$sort' => ['count' => -1]],
    ['$limit' => 10],
];

$command = new MongoDB\Driver\Command([
    'aggregate' => 'users',
    'pipeline' => $pipeline,
    'cursor' => (object) [],
]);

$cursor = $manager->executeCommand('myapp', $command);
foreach ($cursor as $document) {
    echo "{$document->_id}: {$document->count} users" . PHP_EOL;
}
?>
```

### Fix 5: Handle Query Errors with Try-Catch

```php
<?php
function safeQuery(MongoDB\Driver\Manager $manager, string $namespace, array $filter, array $options = []): array
{
    try {
        $query = new MongoDB\Driver\Query($filter, $options);
        $cursor = $manager->executeQuery($namespace, $query);
        return $cursor->toArray();
    } catch (\MongoDB\Driver\Exception\Exception $e) {
        error_log("Query failed on {$namespace}: " . $e->getMessage());
        return [];
    }
}

$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');
$results = safeQuery($manager, 'myapp.users', ['email' => 'test@example.com']);
?>
```

## Examples

### Complex Query with Multiple Conditions

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$filter = [
    '$and' => [
        ['status' => 'active'],
        ['age' => ['$gte' => 18]],
        ['$or' => [
            ['role' => 'admin'],
            ['verified' => true],
        ]],
    ],
];

$options = [
    'projection' => ['name' => 1, 'email' => 1, 'role' => 1],
    'sort' => ['created_at' => -1],
    'limit' => 20,
];

$query = new MongoDB\Driver\Query($filter, $options);
$cursor = $manager->executeQuery('myapp.users', $query);

foreach ($cursor as $user) {
    echo "{$user->name} ({$user->role})" . PHP_EOL;
}
?>
```

## Related Errors

- [MongoDB Write Error]({{< relref "/languages/php/mongodb-write-error" >}})
- [MongoDB Timeout Error]({{< relref "/languages/php/mongodb-timeout-error" >}})
- [MongoDB Index Error]({{< relref "/languages/php/mongodb-index-error" >}})
