---
title: "[Solution] PHP CASSANDRA_WRITE_TIMEOUT_ERROR — Cassandra WriteTimeoutException"
description: "Fix PHP Cassandra WriteTimeoutException. Check consistency level, verify replica count, and handle hints. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 118
---

# PHP CASSANDRA_WRITE_TIMEOUT_ERROR — Cassandra WriteTimeoutException

A Cassandra write operation timed out before reaching the required number of replicas. This error occurs when write consistency levels cannot be met due to slow or down replicas, hint-based delivery failures, or coordinator overload.

## Common Causes

### Write timeout with HIGH consistency level

```php
<?php
$statement = new Cassandra\Query\SimpleQuery(
    "INSERT INTO users (id, name) VALUES (?, ?)"
);
$session->execute($statement, [Cassandra\UUID::uuid1(), 'Alice'], [
    'consistency' => Cassandra\Consistency::ALL,
]);
// Cassandra\Exception\WriteTimeoutException: Timeout writing to system.peers
?>
```

### Coordinator node overloaded

```php
<?php
$statement = $session->prepare("INSERT INTO users (id, name) VALUES (?, ?)");
for ($i = 0; $i < 10000; $i++) {
    $session->execute($statement, [Cassandra\UUID::uuid1(), "User {$i}"], [
        'timeout' => 1000,
    ]);
}
// WriteTimeoutException — coordinator cannot handle throughput
?>
```

### Hint handoff failure

```php
<?php
$statement = new Cassandra\Query\SimpleQuery(
    "INSERT INTO events (id, data) VALUES (?, ?)"
);
$session->execute($statement, [Cassandra\UUID::uuid1(), 'data'], [
    'consistency' => Cassandra\Consistency::QUORUM,
]);
// WriteTimeoutException — hint handoff to down node timed out
?>
```

### Large write with slow disk

```php
<?php
$statement = $session->prepare("INSERT INTO logs (id, content) VALUES (?, ?)");
$session->execute($statement, [
    Cassandra\UUID::uuid1(),
    str_repeat('x', 1000000), // 1MB payload
], ['timeout' => 2000]);
// WriteTimeoutException — large write exceeds timeout
?>
```

### Cassandra commit log fsync delay

```php
<?php
$batch = new Cassandra\Query\BatchStatement();
// Many inserts in a batch
for ($i = 0; $i < 100; $i++) {
    $batch->add(new Cassandra\Query\SimpleQuery(
        "INSERT INTO users (id, name) VALUES (uuid(), 'User {$i}')"
    ));
}
$session->execute($batch, [], [
    'consistency' => Cassandra\Consistency::QUORUM,
]);
// WriteTimeoutException — commit log fsync too slow
?>
```

## How to Fix

### Fix 1: Use Appropriate Write Consistency Level

Match write consistency to your durability requirements.

```php
<?php
$statement = $session->prepare("INSERT INTO users (id, name) VALUES (?, ?)");

// Fastest — acknowledge after single node write
$session->execute($statement, [Cassandra\UUID::uuid1(), 'Alice'], [
    'consistency' => Cassandra\Consistency::ONE,
]);

// Balanced — majority of replicas must acknowledge
$session->execute($statement, [Cassandra\UUID::uuid1(), 'Bob'], [
    'consistency' => Cassandra\Consistency::QUORUM,
]);

// Local — majority in local datacenter
$session->execute($statement, [Cassandra\UUID::uuid1(), 'Charlie'], [
    'consistency' => Cassandra\Consistency::LOCAL_QUORUM,
]);
?>
```

### Fix 2: Optimize Write Performance

Batch writes appropriately and avoid oversized mutations.

```php
<?php
// Good — small batches (under 5KB total)
$batch = new Cassandra\Query\BatchStatement();

$stmt1 = $session->prepare("INSERT INTO users (id, name) VALUES (?, ?)");
$stmt2 = $session->prepare("INSERT INTO user_profiles (id, bio) VALUES (?, ?)");

$userId = Cassandra\UUID::uuid1();
$batch->add($stmt1, [$userId, 'Alice']);
$batch->add($stmt2, [$userId, 'Bio text']);
$session->execute($batch, ['consistency' => Cassandra\Consistency::QUORUM]);

// Bad — large batch across many partitions
$batch = new Cassandra\Query\BatchStatement();
for ($i = 0; $i < 1000; $i++) {
    $batch->add(new Cassandra\Query\SimpleQuery(
        "INSERT INTO events (id, data) VALUES (uuid(), '{$i}')"
    ));
}
// This batch is too large and spans too many partitions
?>
```

### Fix 3: Handle WriteTimeout with Retry

```php
<?php
function cassandraWriteWithRetry(
    Cassandra\Session $session,
    string $cql,
    array $args,
    int $maxRetries = 2
): void {
    $lastException = null;

    for ($attempt = 0; $attempt <= $maxRetries; $attempt++) {
        try {
            $statement = new Cassandra\Query\SimpleQuery($cql);
            $session->execute($statement, $args, [
                'consistency' => Cassandra\Consistency::LOCAL_ONE,
                'timeout' => 10000,
            ]);
            return;
        } catch (Cassandra\Exception\WriteTimeoutException $e) {
            $lastException = $e;
            error_log("Write timeout (attempt {$attempt}): " . $e->getMessage());

            if ($attempt < $maxRetries) {
                // Reduce consistency level on retry
                sleep(pow(2, $attempt));
            }
        }
    }

    throw new RuntimeException(
        "Write failed after {$maxRetries} retries",
        0,
        $lastException
    );
}

cassandraWriteWithRetry(
    $session,
    "INSERT INTO users (id, name) VALUES (?, ?)",
    [Cassandra\UUID::uuid1(), 'Alice']
);
?>
```

### Fix 4: Use Idempotent Writes

Make writes safe to retry without side effects.

```php
<?php
// Idempotent — using INSERT with IF NOT EXISTS
$statement = $session->prepare(
    "INSERT INTO users (id, name, email) VALUES (?, ?, ?) IF NOT EXISTS"
);
$session->execute($statement, [
    Cassandra\UUID::uuid1(),
    'Alice',
    'alice@example.com',
], ['consistency' => Cassandra\Consistency::LOCAL_QUORUM]);

// Idempotent — using UPDATE with specific value (not increment)
$statement = $session->prepare(
    "UPDATE users SET name = ? WHERE id = ? IF EXISTS"
);
$session->execute($statement, ['Alice Updated', $userId], [
    'consistency' => Cassandra\Consistency::LOCAL_ONE,
]);

// Non-idempotent — avoid on retry paths
$statement = $session->prepare(
    "UPDATE users SET login_count = login_count + 1 WHERE id = ?"
);
?>
```

### Fix 5: Tune Write Timeout at Cluster Level

```php
<?php
$cluster = Cassandra::cluster()
    ->withContactPoints('127.0.0.1', '10.0.0.2', '10.0.0.3')
    ->withPort(9042)
    ->withRequestTimeout(30000) // 30s request timeout
    ->withConnectTimeout(10000) // 10s connect timeout
    ->withRetryPolicy(new Cassandra\RetryPolicy\DefaultRetryPolicy())
    ->build();

$session = $cluster->connect('mykeyspace');

// Override timeout per query when needed
$session->execute(new Cassandra\Query\SimpleQuery(
    "INSERT INTO large_table (id, data) VALUES (?, ?)"
), [
    Cassandra\UUID::uuid1(),
    str_repeat('x', 500000),
], [
    'timeout' => 30000, // 30s for large write
    'consistency' => Cassandra\Consistency::ONE,
]);
?>
```

## Examples

### Write Performance Monitor

```php
<?php
function profileWrite(
    Cassandra\Session $session,
    string $cql,
    array $args,
    int $consistency = Cassandra\Consistency::ONE
): array {
    $start = microtime(true);
    try {
        $statement = new Cassandra\Query\SimpleQuery($cql);
        $session->execute($statement, $args, [
            'consistency' => $consistency,
            'timeout' => 30000,
        ]);
        $latency = round((microtime(true) - $start) * 1000, 2);
        return ['status' => 'success', 'latency_ms' => $latency];
    } catch (\Exception $e) {
        $latency = round((microtime(true) - $start) * 1000, 2);
        return ['status' => 'error', 'latency_ms' => $latency, 'error' => $e->getMessage()];
    }
}

$result = profileWrite(
    $session,
    "INSERT INTO users (id, name) VALUES (?, ?)",
    [Cassandra\UUID::uuid1(), 'Alice'],
    Cassandra\Consistency::LOCAL_QUORUM
);
print_r($result);
?>
```

## Related Errors

- [Cassandra Timeout Error]({{< relref "/languages/php/cassandra-timeout-error" >}})
- [Cassandra Unavailable Error]({{< relref "/languages/php/cassandra-unavailable-error" >}})
- [Cassandra Connection Error]({{< relref "/languages/php/cassandra-connection-error" >}})
