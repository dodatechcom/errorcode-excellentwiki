---
title: "[Solution] PHP CASSANDRA_CONNECTION_ERROR — Cassandra Connection Failed"
description: "Fix PHP Cassandra connection failed errors. Check contact points, verify keyspace, and resolve network issues. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 112
---

# PHP CASSANDRA_CONNECTION_ERROR — Cassandra Connection Failed

The Cassandra client failed to connect to the cluster. This error occurs when contact points are unreachable, the port is wrong, the keyspace does not exist, or network connectivity is blocked.

## Common Causes

### Cassandra server is not running

```php
<?php
$cluster = Cassandra::cluster()
    ->withContactPoints('127.0.0.1')
    ->withPort(9042)
    ->build();
$session = $cluster->connect();
// Cassandra\Exception\ConnectionException: Unable to connect
?>
```

### Wrong contact points

```php
<?php
$cluster = Cassandra::cluster()
    ->withContactPoints('wrong-host', '192.168.1.100')
    ->withPort(9042)
    ->build();
$session = $cluster->connect();
// ConnectionException — no hosts available
?>
```

### Wrong port number

```php
<?php
$cluster = Cassandra::cluster()
    ->withContactPoints('127.0.0.1')
    ->withPort(9142) // Cassandra default is 9042
    ->build();
$session = $cluster->connect();
// Connection refused
?>
```

### Keyspace does not exist

```php
<?php
$cluster = Cassandra::cluster()
    ->withContactPoints('127.0.0.1')
    ->withPort(9042)
    ->build();
$session = $cluster->connect('nonexistent_keyspace');
// Cassandra\Exception\InvalidKeyspaceException
?>
```

### Firewall blocking port 9042

```php
<?php
$cluster = Cassandra::cluster()
    ->withContactPoints('10.0.0.50')
    ->withPort(9042)
    ->withConnectTimeout(2000)
    ->build();
$session = $cluster->connect('mykeyspace');
// ConnectionException — timeout
?>
```

## How to Fix

### Fix 1: Verify Cassandra Is Running

Check that the Cassandra service is active before connecting.

```php
<?php
function checkCassandraConnection(string $host, int $port): bool
{
    $socket = @fsockopen($host, $port, $errno, $errstr, 3);
    if (!$socket) {
        error_log("Cassandra unreachable at {$host}:{$port} — {$errstr}");
        return false;
    }
    fclose($socket);
    return true;
}

if (!checkCassandraConnection('127.0.0.1', 9042)) {
    throw new RuntimeException('Cassandra is not running');
}

$cluster = Cassandra::cluster()
    ->withContactPoints('127.0.0.1')
    ->withPort(9042)
    ->build();
$session = $cluster->connect('mykeyspace');
?>
```

### Fix 2: Configure Multiple Contact Points

Use multiple contact points for high availability.

```php
<?php
$cluster = Cassandra::cluster()
    ->withContactPoints('10.0.0.1', '10.0.0.2', '10.0.0.3')
    ->withPort(9042)
    ->withConnectTimeout(5000)
    ->withRetryPolicy(new Cassandra\RetryPolicy\DefaultRetryPolicy())
    ->build();

$session = $cluster->connect('mykeyspace');
echo "Connected to Cassandra cluster" . PHP_EOL;
?>
```

### Fix 3: Set Connection Timeout and Options

Configure appropriate timeout and connection options.

```php
<?php
$cluster = Cassandra::cluster()
    ->withContactPoints('127.0.0.1')
    ->withPort(9042)
    ->withConnectTimeout(10000) // 10 seconds
    ->withRequestTimeout(10000)
    ->withRoundRobinLoadBalancingPolicy()
    ->withProtocolVersion(4)
    ->build();

$session = $cluster->connect('mykeyspace');
?>
```

### Fix 4: Verify Keyspace Exists Before Connecting

```php
<?php
function connectToCassandra(array $contactPoints, int $port, string $keyspace): Cassandra\Session
{
    $cluster = Cassandra::cluster()
        ->withContactPoints(...$contactPoints)
        ->withPort($port)
        ->withConnectTimeout(5000)
        ->build();

    // Connect without keyspace first to create it if needed
    $session = $cluster->connect();

    // Check if keyspace exists
    $rows = $session->execute(new Cassandra\Query\SimpleQuery(
        "SELECT keyspace_name FROM system_schema.keyspaces WHERE keyspace_name = ?",
        [$keyspace]
    ));

    if ($rows->count() === 0) {
        $session->execute(new Cassandra\Query\SimpleQuery(
            "CREATE KEYSPACE IF NOT EXISTS {$keyspace} WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}"
        ));
    }

    // Reconnect with keyspace
    $session->close();
    $session = $cluster->connect($keyspace);
    return $session;
}

$session = connectToCassandra(['127.0.0.1'], 9042, 'myapp');
?>
```

### Fix 5: Handle Connection Failures with Retry

```php
<?php
function cassandraConnectWithRetry(array $contactPoints, string $keyspace, int $maxRetries = 3): Cassandra\Session
{
    $lastException = null;

    for ($attempt = 1; $attempt <= $maxRetries; $attempt++) {
        try {
            $cluster = Cassandra::cluster()
                ->withContactPoints(...$contactPoints)
                ->withPort(9042)
                ->withConnectTimeout(5000)
                ->withRetryPolicy(new Cassandra\RetryPolicy\DefaultRetryPolicy())
                ->build();

            return $cluster->connect($keyspace);
        } catch (Cassandra\Exception\ConnectionException $e) {
            $lastException = $e;
            error_log("Cassandra connection attempt {$attempt} failed: " . $e->getMessage());

            if ($attempt < $maxRetries) {
                sleep(pow(2, $attempt));
            }
        }
    }

    throw new RuntimeException("Cannot connect to Cassandra after {$maxRetries} attempts", 0, $lastException);
}

$session = cassandraConnectWithRetry(['127.0.0.1', '10.0.0.2'], 'mykeyspace');
?>
```

## Examples

### Laravel Cassandra Configuration

```php
<?php
// config/database.php
'cassandra' => [
    'driver' => 'cassandra',
    'name' => env('CASSANDRA_KEYSPACE', 'myapp'),
    'hosts' => explode(',', env('CASSANDRA_HOSTS', '127.0.0.1')),
    'port' => env('CASSANDRA_PORT', 9042),
    'version' => env('CASSANDRA_VERSION', '3.0'),
],
?>
```

## Related Errors

- [Cassandra Query Error]({{< relref "/languages/php/cassandra-query-error" >}})
- [Cassandra Keyspace Error]({{< relref "/languages/php/cassandra-keyspace-error" >}})
- [Cassandra Timeout Error]({{< relref "/languages/php/cassandra-timeout-error" >}})
