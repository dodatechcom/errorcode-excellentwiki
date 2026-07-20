---
title: "[Solution] PHP CASSANDRA_UNAVAILABLE_ERROR — Cassandra UnavailableException"
description: "Fix PHP Cassandra UnavailableException. Check cluster health, verify replication factor, and handle node failures. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 117
---

# PHP CASSANDRA_UNAVAILABLE_ERROR — Cassandra UnavailableException

Cassandra cannot satisfy the requested consistency level because not enough replicas are available. This error occurs when nodes are down, the replication factor is too high for the current cluster size, or a network partition isolates nodes.

## Common Causes

### Not enough replicas for consistency level

```php
<?php
$statement = new Cassandra\Query\SimpleQuery(
    "INSERT INTO users (id, name) VALUES (?, ?)"
);
$session->execute($statement, [Cassandra\UUID::uuid1(), 'Alice'], [
    'consistency' => Cassandra\Consistency::ALL,
]);
// Cassandra\Exception\UnavailableException: Not enough replica available
?>
```

### All nodes in cluster are down

```php
<?php
$cluster = Cassandra::cluster()
    ->withContactPoints('10.0.0.1', '10.0.0.2', '10.0.0.3')
    ->withPort(9042)
    ->build();
$session = $cluster->connect('mykeyspace');
$session->execute(new Cassandra\Query\SimpleQuery("SELECT * FROM users LIMIT 1"));
// UnavailableException — no live nodes
?>
```

### Replication factor exceeds available nodes

```php
<?php
$session->execute(new Cassandra\Query\SimpleQuery("
    CREATE KEYSPACE test WITH replication = {
        'class': 'SimpleStrategy', 'replication_factor': 5
    }
"));
// UnavailableException — cluster has fewer than 5 nodes
?>
```

### Datacenter-aware replication mismatch

```php
<?php
$statement = new Cassandra\Query\SimpleQuery(
    "INSERT INTO users (id, name) VALUES (?, ?)"
);
$session->execute($statement, [Cassandra\UUID::uuid1(), 'Alice'], [
    'consistency' => Cassandra\Consistency::LOCAL_QUORUM,
]);
// UnavailableException — not enough local replicas
?>
```

### Node failure during write

```php
<?php
$batch = new Cassandra\Query\BatchStatement();
// Large batch — one replica dies mid-operation
$session->execute($batch, [], [
    'consistency' => Cassandra\Consistency::QUORUM,
]);
// UnavailableException — insufficient replicas during batch
?>
```

## How to Fix

### Fix 1: Use Appropriate Consistency Levels

Choose consistency levels that match your cluster size.

```php
<?php
// For 3-node cluster with RF=3
$session->execute($statement, $args, [
    'consistency' => Cassandra\Consistency::ONE, // 1 replica — always available
]);

$session->execute($statement, $args, [
    'consistency' => Cassandra\Consistency::QUORUM, // 2 of 3 — balanced
]);

// For single-node dev environment
$session->execute($statement, $args, [
    'consistency' => Cassandra\Consistency::ONE,
]);

// Avoid ALL unless you have many nodes
$session->execute($statement, $args, [
    'consistency' => Cassandra\Consistency::ALL, // requires ALL replicas up
]);
?>
```

### Fix 2: Monitor Cluster Health

```php
<?php
function checkClusterHealth(Cassandra\Session $session): array
{
    $result = $session->execute(new Cassandra\Query\SimpleQuery(
        "SELECT data_center, rack, host_id, state FROM system.peers"
    ));

    $nodes = [];
    foreach ($result as $row) {
        $nodes[] = [
            'datacenter' => $row['data_center'],
            'rack' => $row['rack'],
            'host_id' => (string) $row['host_id'],
            'state' => $row['state'],
        ];
    }

    // Also check local node
    $local = $session->execute(new Cassandra\Query\SimpleQuery(
        "SELECT data_center, rack, host_id, state FROM system.local"
    ));
    $localRow = $local->first();
    $nodes[] = [
        'datacenter' => $localRow['data_center'],
        'rack' => $localRow['rack'],
        'host_id' => (string) $localRow['host_id'],
        'state' => $localRow['state'],
        'local' => true,
    ];

    $liveNodes = count(array_filter($nodes, fn($n) => $n['state'] === 'UN'));
    return [
        'total_nodes' => count($nodes),
        'live_nodes' => $liveNodes,
        'nodes' => $nodes,
    ];
}

$health = checkClusterHealth($session);
echo "Live nodes: {$health['live_nodes']}/{$health['total_nodes']}" . PHP_EOL;
?>
```

### Fix 3: Set Replication Factor Appropriately

Match replication factor to available nodes.

```php
<?php
function getSafeReplicationFactor(Cassandra\Session $session, string $datacenter = ''): int
{
    $result = $session->execute(new Cassandra\Query\SimpleQuery(
        "SELECT data_center FROM system.peers"
    ));

    $dcCount = [];
    $dcCount['local'] = 1; // local node

    foreach ($result as $row) {
        $dc = $row['data_center'];
        $dcCount[$dc] = ($dcCount[$dc] ?? 0) + 1;
    }

    // Safe RF is at most the number of nodes in the datacenter
    if ($datacenter && isset($dcCount[$datacenter])) {
        return min(3, $dcCount[$datacenter]);
    }

    $totalNodes = array_sum($dcCount);
    return min(3, $totalNodes);
}

|RF = {$safeRf}" . PHP_EOL;
?>
```

### Fix 4: Handle UnavailableException with Retry

```php
<?php
function cassandraWithFallback(
    Cassandra\Session $session,
    string $cql,
    array $args = [],
    int $maxRetries = 2
): Cassandra\Rows {
    $lastException = null;

    for ($attempt = 0; $attempt <= $maxRetries; $attempt++) {
        try {
            $statement = new Cassandra\Query\SimpleQuery($cql);
            return $session->execute($statement, $args, [
                'consistency' => Cassandra\Consistency::ONE,
                'timeout' => 10000,
            ]);
        } catch (Cassandra\Exception\UnavailableException $e) {
            $lastException = $e;
            error_log("UnavailableException (attempt {$attempt}): " . $e->getMessage());

            if ($attempt < $maxRetries) {
                sleep(pow(2, $attempt));
            }
        }
    }

    throw new RuntimeException(
        "Cassandra unavailable after {$maxRetries} retries",
        0,
        $lastException
    );
}

$result = cassandraWithFallback(
    $session,
    "SELECT * FROM users WHERE user_id = ?",
    [Cassandra\UUID::uuid1()]
);
?>
```

### Fix 5: Use Token-Aware Routing

Direct queries to the correct replica node.

```php
<?php
$cluster = Cassandra::cluster()
    ->withContactPoints('127.0.0.1', '10.0.0.2', '10.0.0.3')
    ->withPort(9042)
    ->withLoadBalancingPolicy(
        new Cassandra\LoadBalancingPolicy\TokenAware(
            new Cassandra\LoadBalancingPolicy\DCAwareRoundRobin('us-east')
        )
    )
    ->build();

$session = $cluster->connect('mykeyspace');
?>
```

## Examples

### Graceful Degradation

```php
<?php
function readWithFallback(Cassandra\Session $session, string $cql, array $args): array
{
    $levels = [
        Cassandra\Consistency::LOCAL_QUORUM,
        Cassandra\Consistency::LOCAL_ONE,
        Cassandra\Consistency::ONE,
    ];

    foreach ($levels as $level) {
        try {
            $statement = new Cassandra\Query\SimpleQuery($cql);
            $result = $session->execute($statement, $args, [
                'consistency' => $level,
                'timeout' => 10000,
            ]);
            return $result->toArray();
        } catch (Cassandra\Exception\UnavailableException $e) {
            error_log("Consistency {$level} unavailable, trying lower");
            continue;
        }
    }

    throw new RuntimeException('All consistency levels failed');
}

$data = readWithFallback($session, "SELECT * FROM users WHERE user_id = ?", [Cassandra\UUID::uuid1()]);
?>
```

## Related Errors

- [Cassandra Connection Error]({{< relref "/languages/php/cassandra-connection-error" >}})
- [Cassandra Timeout Error]({{< relref "/languages/php/cassandra-timeout-error" >}})
- [Cassandra WriteTimeout Error]({{< relref "/languages/php/cassandra-write-timeout-error" >}})
