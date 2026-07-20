---
title: "[Solution] PHP MONGODB_WRITE_ERROR — MongoDB Write Failed"
description: "Fix PHP MongoDB write errors. Check WriteConcern, handle duplicates, and verify document format. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 108
---

# PHP MONGODB_WRITE_ERROR — MongoDB Write Failed

A MongoDB write operation failed. This error occurs when a document violates schema validation, a unique index is violated, the WriteConcern cannot be satisfied, or the document format is invalid.

## Common Causes

### Duplicate key violation

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['email' => 'user@example.com', 'name' => 'Alice']);
$bulk->insert(['email' => 'user@example.com', 'name' => 'Bob']); // duplicate

$manager->executeBulkWrite('myapp.users', $bulk);
// MongoDB\Driver\Exception\BulkWriteException: E11000 duplicate key error
?>
```

### Invalid document structure

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert([
    'name' => new stdClass(),
    'tags' => 'not_an_array', // wrong type
]);

$manager->executeBulkWrite('myapp.users', $bulk);
// Exception — cannot serialize document
?>
```

### WriteConcern not satisfied

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017', [
    'w' => 3, // require acknowledgment from 3 replicas
]);

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['name' => 'Alice']);

$manager->executeBulkWrite('myapp.users', $bulk);
// WriteConcernError — not enough replicas available
?>
```

### Document exceeds 16MB size limit

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['data' => str_repeat('x', 17 * 1024 * 1024)]); // 17MB

$manager->executeBulkWrite('myapp.files', $bulk);
// WriteError — document exceeds 16MB limit
?>
```

### Key too long for index

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['title' => str_repeat('a', 1025)]); // key > 1024 bytes

$manager->executeBulkWrite('myapp.articles', $bulk);
// WriteError — key too long for index
?>
```

## How to Fix

### Fix 1: Handle Duplicate Key Errors

Use upserts or catch duplicate key exceptions.

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

// Option A: Use upsert to handle duplicates
$bulk = new MongoDB\Driver\BulkWrite(['ordered' => false]);
$bulk->update(
    ['email' => 'user@example.com'],
    ['$set' => ['name' => 'Alice', 'updated_at' => new MongoDB\BSON\UTCDateTime()]],
    ['upsert' => true]
);
$manager->executeBulkWrite('myapp.users', $bulk);

// Option B: Catch and handle duplicates
try {
    $bulk = new MongoDB\Driver\BulkWrite;
    $bulk->insert(['email' => 'user@example.com', 'name' => 'Alice']);
    $manager->executeBulkWrite('myapp.users', $bulk);
} catch (MongoDB\Driver\Exception\BulkWriteException $e) {
    if ($e->getCode() === 11000) {
        // Duplicate key — user already exists
        error_log('User already exists: ' . $e->getMessage());
    } else {
        throw $e;
    }
}
?>
```

### Fix 2: Validate Document Before Insert

```php
<?php
function validateUserDocument(array $document): array
{
    $required = ['email', 'name'];
    foreach ($required as $field) {
        if (!isset($document[$field]) || empty($document[$field])) {
            throw new InvalidArgumentException("Missing required field: {$field}");
        }
    }

    if (!filter_var($document['email'], FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException('Invalid email format');
    }

    if (strlen($document['name']) > 255) {
        throw new InvalidArgumentException('Name exceeds 255 characters');
    }

    if (isset($document['age']) && ($document['age'] < 0 || $document['age'] > 150)) {
        throw new InvalidArgumentException('Invalid age');
    }

    return $document;
}

$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');
$doc = validateUserDocument(['email' => 'user@example.com', 'name' => 'Alice', 'age' => 30]);

$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert($doc);
$manager->executeBulkWrite('myapp.users', $bulk);
?>
```

### Fix 3: Use Appropriate WriteConcern

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

// Default write concern (w: 1)
$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['name' => 'Alice']);
$result = $manager->executeBulkWrite('myapp.users', $bulk);

// Acknowledged write with timeout
$writeConcern = new MongoDB\Driver\WriteConcern(1, 5000); // w:1, wTimeout:5s
$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['name' => 'Bob']);
$manager->executeBulkWrite('myapp.users', $bulk, $writeConcern);
?>
```

### Fix 4: Use Ordered vs Unordered Writes

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

// Ordered: stop on first error
$bulk = new MongoDB\Driver\BulkWrite(['ordered' => true]);
$bulk->insert(['name' => 'Alice', 'email' => 'alice@example.com']);
$bulk->insert(['name' => 'Bob', 'email' => 'bob@example.com']);
$manager->executeBulkWrite('myapp.users', $bulk);

// Unordered: continue on error, report all failures
$bulk = new MongoDB\Driver\BulkWrite(['ordered' => false]);
$bulk->insert(['name' => 'Charlie', 'email' => 'charlie@example.com']);
$bulk->insert(['name' => 'Diana', 'email' => 'diana@example.com']);
$result = $manager->executeBulkWrite('myapp.users', $bulk);
echo "Inserted: " . $result->getInsertedCount() . PHP_EOL;
?>
```

### Fix 5: Handle BulkWrite Exceptions

```php
<?php
function safeBulkWrite(MongoDB\Driver\Manager $manager, string $namespace, MongoDB\Driver\BulkWrite $bulk): MongoDB\Driver\BulkWriteResult
{
    try {
        return $manager->executeBulkWrite($namespace, $bulk);
    } catch (MongoDB\Driver\Exception\BulkWriteException $e) {
        $writeResult = $e->getWriteResult();

        if ($writeResult) {
            error_log("Inserted: " . $writeResult->getInsertedCount());
            error_log("Updated: " . $writeResult->getMatchedCount());
            error_log("Modified: " . $writeResult->getModifiedCount());
            error_log("Deleted: " . $writeResult->getDeletedCount());
        }

        $writeErrors = $e->getWriteErrors();
        foreach ($writeErrors as $error) {
            error_log("Write error at index {$error->getIndex()}: {$error->getMessage()}");
        }

        $writeConcernError = $e->getWriteConcernError();
        if ($writeConcernError) {
            error_log("WriteConcern error: {$writeConcernError->getMessage()}");
        }

        throw $e;
    }
}
?>
```

## Examples

### Batch Insert with Error Handling

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$users = [
    ['name' => 'Alice', 'email' => 'alice@example.com'],
    ['name' => 'Bob', 'email' => 'bob@example.com'],
    ['name' => 'Charlie', 'email' => 'charlie@example.com'],
];

$bulk = new MongoDB\Driver\BulkWrite(['ordered' => false]);
foreach ($users as $user) {
    $user['created_at'] = new MongoDB\BSON\UTCDateTime();
    $bulk->insert($user);
}

$result = $manager->executeBulkWrite('myapp.users', $bulk);
echo "Inserted: {$result->getInsertedCount()} documents" . PHP_EOL;
?>
```

## Related Errors

- [MongoDB Query Error]({{< relref "/languages/php/mongodb-query-error" >}})
- [MongoDB Index Error]({{< relref "/languages/php/mongodb-index-error" >}})
- [MongoDB BulkWrite Error]({{< relref "/languages/php/mongodb-bulkwrite-error" >}})
