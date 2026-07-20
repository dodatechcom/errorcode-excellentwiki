---
title: "[Solution] PHP MONGODB_TIMEOUT_ERROR — MongoDB Operation Timed Out"
description: "Fix PHP MongoDB timeout errors. Increase timeout, check server load, and use read preferences. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 109
---

# PHP MONGODB_TIMEOUT_ERROR — MongoDB Operation Timed Out

A MongoDB operation exceeded the allowed time limit. This error occurs when server selection times out, queries run too long, or network latency causes operations to exceed their configured timeout.

## Common Causes

### Server selection timeout exceeded

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017', [
    'serverSelectionTimeoutMS' => 1000,
]);
$command = new MongoDB\Driver\Command(['ping' => 1]);
$manager->executeCommand('admin', $command);
// MongoDB\Driver\Exception\ConnectionTimeoutException: No suitable servers found
?>
```

### Query timeout on large collections

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');
$filter = ['status' => 'active'];
$query = new MongoDB\Driver\Query($filter, ['allowDiskUse' => false]);
$cursor = $manager->executeQuery('myapp.events', $query);
// Timeout — full collection scan on billions of documents
?>
```

### Replica set election causing delays

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://host1:27017,host2:27017,host3:27017');
$command = new MongoDB\Driver\Command(['ping' => 1]);
$manager->executeCommand('admin', $command);
// Timeout during replica set failover/election
?>
```

### Write operations on overloaded secondaries

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://host1:27017', [
    'readPreference' => MongoDB\Driver\ReadPreference::RP_SECONDARY,
]);
$query = new MongoDB\Driver\Query(['status' => 'active']);
$cursor = $manager->executeQuery('myapp.large_collection', $query);
// Timeout — secondary is lagging or overloaded
?>
```

### ConnectTimeoutMS too low

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://remote-host:27017', [
    'connectTimeoutMS' => 100, // 100ms too low for remote server
]);
$command = new MongoDB\Driver\Command(['ping' => 1]);
$manager->executeCommand('admin', $command);
// ConnectionTimeoutException
?>
```

## How to Fix

### Fix 1: Increase Timeout Values

Configure appropriate timeouts for your environment.

```php
<?php
$uri = 'mongodb://127.0.0.1:27017/?'
    . 'connectTimeoutMS=5000'         // 5s to establish TCP connection
    . '&serverSelectionTimeoutMS=10000' // 10s to find a suitable server
    . '&socketTimeoutMS=30000'          // 30s for read/write operations
    . '&maxPoolSize=50';                // connection pool size

$manager = new MongoDB\Driver\Manager($uri);
$command = new MongoDB\Driver\Command(['ping' => 1]);
$manager->executeCommand('admin', $command);
?>
```

### Fix 2: Optimize Queries with Indexes

Ensure queries use indexes to avoid full collection scans.

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

// Create index for frequently queried fields
$command = new MongoDB\Driver\Command([
    'createIndexes' => 'users',
    'indexes' => [
        [
            'key' => ['status' => 1, 'created_at' => -1],
            'name' => 'status_created_idx',
        ],
        [
            'key' => ['email' => 1],
            'name' => 'email_unique_idx',
            'unique' => true,
        ],
    ],
]);
$manager->executeCommand('myapp', $command);

// Query now uses index
$query = new MongoDB\Driver\Query(
    ['status' => 'active'],
    ['sort' => ['created_at' => -1], 'limit' => 50]
);
$cursor = $manager->executeQuery('myapp.users', $query);
?>
```

### Fix 3: Use Read Preferences for Load Distribution

Distribute reads across replicas to reduce load.

```php
<?php
$uri = 'mongodb://host1:27017,host2:27017,host3:27017/?replicaSet=myrs';

$manager = new MongoDB\Driver\Manager($uri);

// Read from secondary with tag sets
$readPreference = new MongoDB\Driver\ReadPreference(
    MongoDB\Driver\ReadPreference::RP_SECONDARY_PREFERRED,
    [['dc' => 'us-east']] // preferred tags
);

$query = new MongoDB\Driver\Query(['status' => 'active']);
$cursor = $manager->executeQuery('myapp.users', $query, [
    'readPreference' => $readPreference,
]);
?>
```

### Fix 4: Implement Timeout Handling with Retry

```php
<?php
function queryWithTimeout(
    MongoDB\Driver\Manager $manager,
    string $namespace,
    array $filter,
    array $options = [],
    int $maxRetries = 2
): array {
    $lastException = null;

    for ($attempt = 0; $attempt <= $maxRetries; $attempt++) {
        try {
            $query = new MongoDB\Driver\Query($filter, $options);
            $cursor = $manager->executeQuery($namespace, $query);
            return $cursor->toArray();
        } catch (MongoDB\Driver\Exception\ConnectionTimeoutException $e) {
            $lastException = $e;
            error_log("Query timeout on {$namespace} (attempt {$attempt}): " . $e->getMessage());

            if ($attempt < $maxRetries) {
                sleep(pow(2, $attempt));
            }
        }
    }

    throw new RuntimeException("Query failed after {$maxRetries} retries", 0, $lastException);
}

$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');
$results = queryWithTimeout($manager, 'myapp.users', ['status' => 'active']);
?>
```

### Fix 5: Use allowDiskUse for Large Aggregations

Allow MongoDB to use disk for large aggregation results.

```php
<?php
$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$command = new MongoDB\Driver\Command([
    'aggregate' => 'events',
    'pipeline' => [
        ['$match' => ['date' => ['$gte' => new MongoDB\BSON\UTCDateTime(strtotime('-1 year') * 1000)]]],
        ['$group' => ['_id' => '$category', 'count' => ['$sum' => 1]]],
    ],
    'cursor' => (object) [],
    'allowDiskUse' => true, // prevent memory limit errors
]);

$cursor = $manager->executeCommand('myapp', $command);
foreach ($cursor as $document) {
    echo "{$document->_id}: {$document->count}" . PHP_EOL;
}
?>
```

## Examples

### Connection Health Check with Timeout

```php
<?php
function mongodbHealthCheck(string $uri, int $timeoutMs = 5000): array
{
    $start = microtime(true);

    try {
        $manager = new MongoDB\Driver\Manager($uri . '&serverSelectionTimeoutMS=' . $timeoutMs);
        $command = new MongoDB\Driver\Command(['ping' => 1]);
        $result = $manager->executeCommand('admin', $command);
        $latency = round((microtime(true) - $start) * 1000, 2);

        return [
            'status' => 'healthy',
            'latency' => "{$latency}ms",
        ];
    } catch (\Exception $e) {
        return [
            'status' => 'unhealthy',
            'error' => $e->getMessage(),
        ];
    }
}

$result = mongodbHealthCheck('mongodb://127.0.0.1:27017/');
?>
```

## Related Errors

- [MongoDB Connection Error]({{< relref "/languages/php/mongodb-connection-error" >}})
- [MongoDB Query Error]({{< relref "/languages/php/mongodb-query-error" >}})
- [Redis Timeout Error]({{< relref "/languages/php/redis-timeout-error" >}})
