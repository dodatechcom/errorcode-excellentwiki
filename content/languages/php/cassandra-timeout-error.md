---
title: "[Solution] PHP CASSANDRA_TIMEOUT_ERROR — Cassandra Query Timed Out"
description: "Fix PHP Cassandra timeout errors. Increase timeout, check consistency, and optimize queries. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 114
---

# PHP CASSANDRA_TIMEOUT_ERROR — Cassandra Query Timed Out

A Cassandra query exceeded the configured timeout limit. This error occurs when queries are too slow due to large data scans, high cluster load, network latency, or overly strict consistency levels.

## Common Causes

### Query timeout on large partition

```php
<?php
$statement = new Cassandra\Query\SimpleQuery(
    "SELECT * FROM events WHERE user_id = ?"
);
$result = $session->execute($statement, [
    Cassandra\UUID::uuid1(),
], ['timeout' => 1000]); // 1 second too short for millions of rows
// Cassandra\Exception\ReadTimeoutException
?>
```

### High consistency level causing delays

```php
<?php
$statement = new Cassandra\Query\SimpleQuery(
    "INSERT INTO users (id, name) VALUES (?, ?)"
);
$session->execute($statement, [Cassandra\UUID::uuid1(), 'Alice'], [
    'consistency' => Cassandra\Consistency::ALL, // requires all replicas
]);
// WriteTimeoutException — some replicas are slow
?>
```

### Coordinator node overload

```php
<?php
$statement = new Cassandra\Query\SimpleQuery(
    "SELECT * FROM users WHERE status = 'active' ALLOW FILTERING"
);
$session->execute($statement, [], ['timeout' => 30000]);
// ReadTimeoutException — coordinator overwhelmed
?>
```

### Network latency between datacenter and cluster

```php
<?php
$cluster = Cassandra::cluster()
    ->withContactPoints('us-east.example.com')
    ->withPort(9042)
    ->withConnectTimeout(5000)
    ->withRequestTimeout(2000) // too low for cross-DC
    ->build();
$session = $cluster->connect('mykeyspace');
// Timeout on cross-datacenter operations
?>
```

### Secondary index scan timeout

```php
<?php
$statement = new Cassandra\Query\SimpleQuery(
    "SELECT * FROM users WHERE email = 'test@example.com'"
);
$result = $session->execute($statement, ['timeout' => 5000]);
// ReadTimeoutException — secondary index scan on large table
?>
```

## How to Fix

### Fix 1: Increase Query Timeout

Set appropriate timeout values per query.

```php
<?php
$statement = $session->prepare("SELECT * FROM users WHERE user_id = ?");

// Increase timeout for this specific query
$result = $session->execute($statement, [
    Cassandra\UUID::uuid1(),
], [
    'timeout' => 30000, // 30 seconds
]);
?>
```

### Fix 2: Use Appropriate Consistency Levels

Balance consistency with performance.

```php
<?php
// Write with ONE — fastest, accept eventual consistency
$statement = $session->prepare("INSERT INTO users (id, name) VALUES (?, ?)");
$session->execute($statement, [Cassandra\UUID::uuid1(), 'Alice'], [
    'consistency' => Cassandra\Consistency::ONE,
]);

// Read with QUORUM — balanced consistency
$statement = $session->prepare("SELECT * FROM users WHERE id = ?");
$result = $session->execute($statement, [Cassandra\UUID::uuid1()], [
    'consistency' => Cassandra\Consistency::QUORUM,
]);

// Use LOCAL_ONE for multi-datacenter setups
$session->execute($statement, [Cassandra\UUID::uuid1()], [
    'consistency' => Cassandra\Consistency::LOCAL_ONE,
]);
?>
```

### Fix 3: Optimize Queries to Avoid Timeouts

Design efficient queries that target specific partitions.

```php
<?php
// Good — queries by partition key, limited result set
$statement = $session->prepare(
    "SELECT name, email FROM users WHERE user_id = ? LIMIT 100"
);
$result = $session->execute($statement, [Cassandra\UUID::uuid1()]);

// Good — uses clustering key for range queries
$statement = $session->prepare(
    "SELECT * FROM events WHERE user_id = ? AND event_date >= ? AND event_date <= ? ORDER BY event_date DESC LIMIT 50"
);
$result = $session->execute($statement, [
    Cassandra\UUID::uuid1(),
    new Cassandra\Timestamp(strtotime('-7 days')),
    new Cassandra\Timestamp(),
]);

// Bad — full table scan without partition key
$statement = new Cassandra\Query\SimpleQuery(
    "SELECT * FROM events WHERE event_type = 'login'" // no partition key
);
?>
```

### Fix 4: Use Paging for Large Result Sets

```php
<?php
$statement = $session->prepare(
    "SELECT * FROM events WHERE user_id = ?"
);

$pageSize = 1000;
$options = [
    'fetch_size' => $pageSize,
];

$result = $session->execute($statement, [Cassandra\UUID::uuid1()], $options);

$totalRows = 0;
foreach ($result as $row) {
    $totalRows++;
    // Process each row
}

echo "Fetched {$totalRows} rows with paging" . PHP_EOL;
?>
```

### Fix 5: Handle Timeout Exceptions with Retry

```php
<?php
function cassandraQueryWithTimeout(
    Cassandra\Session $session,
    string $cql,
    array $arguments = [],
    int $timeoutMs = 10000,
    int $maxRetries = 2
): Cassandra\Rows {
    $lastException = null;

    for ($attempt = 0; $attempt <= $maxRetries; $attempt++) {
        try {
            $statement = new Cassandra\Query\SimpleQuery($cql);
            return $session->execute($statement, $arguments, ['timeout' => $timeoutMs]);
        } catch (Cassandra\Exception\ReadTimeoutException $e) {
            $lastException = $e;
            error_log("Cassandra timeout (attempt {$attempt}): " . $e->getMessage());
            if ($attempt < $maxRetries) {
                sleep(pow(2, $attempt));
            }
        } catch (Cassandra\Exception\WriteTimeoutException $e) {
            $lastException = $e;
            error_log("Cassandra write timeout (attempt {$attempt}): " . $e->getMessage());
            if ($attempt < $maxRetries) {
                sleep(pow(2, $attempt));
            }
        }
    }

    throw new RuntimeException("Cassandra query failed after {$maxRetries} retries", 0, $lastException);
}

$result = cassandraQueryWithTimeout(
    $session,
    "SELECT * FROM users WHERE user_id = ?",
    [Cassandra\UUID::uuid1()],
    15000
);
?>
```

## Examples

### Monitor Query Performance

```php
<?php
function profileQuery(Cassandra\Session $session, string $cql, array $params = []): array
{
    $start = microtime(true);
    try {
        $statement = new Cassandra\Query\SimpleQuery($cql);
        $result = $session->execute($statement, $params, ['timeout' => 30000]);
        $elapsed = round((microtime(true) - $start) * 1000, 2);
        return [
            'status' => 'success',
            'latency_ms' => $elapsed,
            'row_count' => $result->count(),
        ];
    } catch (\Exception $e) {
        $elapsed = round((microtime(true) - $start) * 1000, 2);
        return [
            'status' => 'error',
            'latency_ms' => $elapsed,
            'error' => $e->getMessage(),
        ];
    }
}

$result = profileQuery($session, "SELECT * FROM users WHERE user_id = ?", [Cassandra\UUID::uuid1()]);
print_r($result);
?>
```

## Related Errors

- [Cassandra Connection Error]({{< relref "/languages/php/cassandra-connection-error" >}})
- [Cassandra Query Error]({{< relref "/languages/php/cassandra-query-error" >}})
- [Cassandra WriteTimeout Error]({{< relref "/languages/php/cassandra-write-timeout-error" >}})
