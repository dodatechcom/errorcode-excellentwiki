---
title: "[Solution] PHP MONGODB_BULKWRITE_ERROR — MongoDB BulkWrite Error"
description: "Fix PHP MongoDB BulkWrite errors. Check operations, handle partial failures, and use ordered/unordered writes. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 111
---

# PHP MONGODB_BULKWRITE_ERROR — MongoDB BulkWrite Error

A MongoDB BulkWrite operation failed or encountered partial errors. This error occurs when operations in a bulk batch are invalid, hit unique constraints, or the bulk request exceeds size limits.

## Common Causes

### Mixed operations with errors in ordered bulk

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$bulk = new MongoDB\Driver\BulkWrite(['ordered' => true]);
$bulk->insert(['email' => 'alice@example.com', 'name' => 'Alice']);
$bulk->insert(['email' => 'alice@example.com', 'name' => 'Bob']); // duplicate
$bulk->insert(['email' => 'charlie@example.com', 'name' => 'Charlie']); // skipped
$manager->executeBulkWrite('myapp.users', $bulk);
// BulkWriteException — stops at duplicate, Charlie never inserted
?>
```

### Empty bulk write

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$bulk = new MongoDB\Driver\BulkWrite;
// No operations added
$manager->executeBulkWrite('myapp.users', $bulk);
// BulkWriteException — nothing to write
?>
```

### Invalid update operation

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->update(
    ['email' => 'alice@example.com'],
    ['name' => 'Alice Updated'], // missing $set operator
    ['multi' => true]
);
$manager->executeBulkWrite('myapp.users', $bulk);
// WriteError — unknown modifier: name (must use $set)
?>
```

### Update with non-existent field path

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->update(
    ['_id' => new MongoDB\BSON\ObjectID('507f1f77bcf86cd799439011')],
    ['$set' => ['nested.deep.field' => 'value']],
    ['multi' => false]
);
$manager->executeBulkWrite('myapp.users', $bulk);
// May fail if document structure doesn't support nested path
?>
```

### Upsert conflict on different fields

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->update(
    ['email' => 'new@example.com'],
    ['$set' => ['name' => 'New User', 'email' => 'new@example.com']],
    ['upsert' => true]
);
$bulk->update(
    ['email' => 'another@example.com'],
    ['$set' => ['name' => 'Another User', 'email' => 'new@example.com']], // duplicate email
    ['upsert' => true]
);
$manager->executeBulkWrite('myapp.users', $bulk);
// E11000 duplicate key error on unique index
?>
```

## How to Fix

### Fix 1: Use Unordered Writes to Continue on Error

Unordered bulk writes continue processing all operations even if some fail.

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$bulk = new MongoDB\Driver\BulkWrite(['ordered' => false]);
$bulk->insert(['email' => 'alice@example.com', 'name' => 'Alice']);
$bulk->insert(['email' => 'alice@example.com', 'name' => 'Bob']); // duplicate
$bulk->insert(['email' => 'charlie@example.com', 'name' => 'Charlie']);

try {
    $result = $manager->executeBulkWrite('myapp.users', $bulk);
    echo "Inserted: {$result->getInsertedCount()}" . PHP_EOL;
} catch (MongoDB\Driver\Exception\BulkWriteException $e) {
    $writeResult = $e->getWriteResult();
    if ($writeResult) {
        echo "Partially succeeded — inserted: {$writeResult->getInsertedCount()}" . PHP_EOL;
    }
    foreach ($e->getWriteErrors() as $error) {
        echo "Error at index {$error->getIndex()}: {$error->getMessage()}" . PHP_EOL;
    }
}
?>
```

### Fix 2: Validate All Operations Before Execution

```php
<?php
function validateBulkOperations(array $operations): array
{
    $valid = [];
    $errors = [];

    foreach ($operations as $index => $op) {
        try {
            if (!isset($op['type'])) {
                throw new InvalidArgumentException('Missing operation type');
            }

            if ($op['type'] === 'insert' && empty($op['document'])) {
                throw new InvalidArgumentException('Empty document for insert');
            }

            if (in_array($op['type'], ['update', 'updateMany']) && !isset($op['update'])) {
                throw new InvalidArgumentException('Missing update operators');
            }

            $valid[] = $op;
        } catch (InvalidArgumentException $e) {
            $errors[$index] = $e->getMessage();
        }
    }

    return ['valid' => $valid, 'errors' => $errors];
}

$operations = [
    ['type' => 'insert', 'document' => ['name' => 'Alice']],
    ['type' => 'insert'], // invalid — no document
    ['type' => 'update', 'filter' => ['name' => 'Bob'], 'update' => ['$set' => ['age' => 30]]],
];

$result = validateBulkOperations($operations);
if (!empty($result['errors'])) {
    foreach ($result['errors'] as $idx => $err) {
        error_log("Operation {$idx}: {$err}");
    }
}
?>
```

### Fix 3: Handle Partial Failures

```php
<?php
function executeBulkSafely(MongoDB\Driver\Manager $manager, string $namespace, MongoDB\Driver\BulkWrite $bulk): array
{
    try {
        $result = $manager->executeBulkWrite($namespace, $bulk);
        return [
            'success' => true,
            'inserted' => $result->getInsertedCount(),
            'matched' => $result->getMatchedCount(),
            'modified' => $result->getModifiedCount(),
            'deleted' => $result->getDeletedCount(),
            'upserted' => $result->getUpsertedCount(),
        ];
    } catch (MongoDB\Driver\Exception\BulkWriteException $e) {
        $result = $e->getWriteResult();
        $errors = [];
        foreach ($e->getWriteErrors() as $error) {
            $errors[] = [
                'index' => $error->getIndex(),
                'code' => $error->getCode(),
                'message' => $error->getMessage(),
            ];
        }

        return [
            'success' => false,
            'partial' => true,
            'inserted' => $result ? $result->getInsertedCount() : 0,
            'errors' => $errors,
        ];
    }
}

$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');
$bulk = new MongoDB\Driver\BulkWrite(['ordered' => false]);
$bulk->insert(['name' => 'Alice', 'email' => 'alice@example.com']);
$bulk->insert(['name' => 'Bob', 'email' => 'bob@example.com']);
$result = executeBulkSafely($manager, 'myapp.users', $bulk);
print_r($result);
?>
```

### Fix 4: Use Correct Update Operators

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$bulk = new MongoDB\Driver\BulkWrite(['ordered' => false]);

// Update with $set
$bulk->update(
    ['email' => 'alice@example.com'],
    ['$set' => ['name' => 'Alice Updated', 'updated_at' => new MongoDB\BSON\UTCDateTime()]],
    ['multi' => false]
);

// Update with $inc
$bulk->update(
    ['email' => 'bob@example.com'],
    ['$inc' => ['login_count' => 1]],
    ['multi' => false]
);

// Update with $push
$bulk->update(
    ['email' => 'charlie@example.com'],
    ['$push' => ['tags' => ['new_tag']]],
    ['multi' => false]
);

// Update with $unset
$bulk->update(
    ['email' => 'diana@example.com'],
    ['$unset' => ['temp_field' => '']],
    ['multi' => false]
);

try {
    $result = $manager->executeBulkWrite('myapp.users', $bulk);
    echo "Updated: {$result->getModifiedCount()} documents" . PHP_EOL;
} catch (MongoDB\Driver\Exception\BulkWriteException $e) {
    foreach ($e->getWriteErrors() as $error) {
        error_log("BulkWrite error: {$error->getMessage()}");
    }
}
?>
```

### Fix 5: Batch Large Operations

Split large bulk operations into smaller batches.

```php
<?php
function batchBulkWrite(
    MongoDB\Driver\Manager $manager,
    string $namespace,
    array $documents,
    int $batchSize = 1000
): array {
    $totalInserted = 0;
    $allErrors = [];

    $batches = array_chunk($documents, $batchSize);

    foreach ($batches as $batchIndex => $batch) {
        $bulk = new MongoDB\Driver\BulkWrite(['ordered' => false]);

        foreach ($batch as $doc) {
            $bulk->insert($doc);
        }

        try {
            $result = $manager->executeBulkWrite($namespace, $bulk);
            $totalInserted += $result->getInsertedCount();
        } catch (MongoDB\Driver\Exception\BulkWriteException $e) {
            $result = $e->getWriteResult();
            $totalInserted += $result ? $result->getInsertedCount() : 0;

            foreach ($e->getWriteErrors() as $error) {
                $allErrors[] = "Batch {$batchIndex}: " . $error->getMessage();
            }
        }
    }

    return ['inserted' => $totalInserted, 'errors' => $allErrors];
}

$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');
$documents = [];
for ($i = 0; $i < 5000; $i++) {
    $documents[] = ['name' => "User {$i}", 'email' => "user{$i}@example.com"];
}

$result = batchBulkWrite($manager, 'myapp.users', $documents, 1000);
echo "Inserted: {$result['inserted']} documents" . PHP_EOL;
echo "Errors: " . count($result['errors']) . PHP_EOL;
?>
```

## Examples

### Complete Bulk CRUD Operation

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$bulk = new MongoDB\Driver\BulkWrite(['ordered' => false]);

// Inserts
$bulk->insert(['email' => 'alice@example.com', 'name' => 'Alice', 'age' => 30]);
$bulk->insert(['email' => 'bob@example.com', 'name' => 'Bob', 'age' => 25]);

// Updates
$bulk->update(['email' => 'alice@example.com'], ['$set' => ['age' => 31]]);
$bulk->update(['name' => 'Bob'], ['$set' => ['status' => 'active']], ['multi' => true]);

// Upserts
$bulk->update(
    ['email' => 'charlie@example.com'],
    ['$set' => ['name' => 'Charlie', 'age' => 28]],
    ['upsert' => true]
);

// Delete
$bulk->delete(['email' => 'old@example.com']);

try {
    $result = $manager->executeBulkWrite('myapp.users', $bulk);
    echo "Inserted: {$result->getInsertedCount()}, ";
    echo "Matched: {$result->getMatchedCount()}, ";
    echo "Modified: {$result->getModifiedCount()}, ";
    echo "Deleted: {$result->getDeletedCount()}, ";
    echo "Upserted: {$result->getUpsertedCount()}" . PHP_EOL;
} catch (MongoDB\Driver\Exception\BulkWriteException $e) {
    error_log('BulkWrite failed: ' . $e->getMessage());
}
?>
```

## Related Errors

- [MongoDB Write Error]({{< relref "/languages/php/mongodb-write-error" >}})
- [MongoDB Index Error]({{< relref "/languages/php/mongodb-index-error" >}})
- [MongoDB Query Error]({{< relref "/languages/php/mongodb-query-error" >}})
