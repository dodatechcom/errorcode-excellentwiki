---
title: "[Solution] PHP MONGODB_CONNECTION_ERROR — MongoDB Connection Failed"
description: "Fix PHP MongoDB connection failed errors. Check connection string, verify MongoDB is running, and handle network issues. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 105
---

# PHP MONGODB_CONNECTION_ERROR — MongoDB Connection Failed

The MongoDB client failed to connect to the server. This error occurs when the connection string is invalid, MongoDB is not running, network access is blocked, or DNS resolution fails for the host.

## Common Causes

### MongoDB server is not running

```php
<?php
$client = new MongoDB\Driver\Manager("mongodb://127.0.0.1:27017");
$command = new MongoDB\Driver\Command(['ping' => 1]);
$client->executeCommand('admin', $command);
// MongoDB\Driver\Exception\ConnectionTimeoutException: No suitable servers found
?>
```

### Invalid connection string

```php
<?php
$client = new MongoDB\Driver\Manager("mongodb://wrong-host:27017");
$command = new MongoDB\Driver\Command(['ping' => 1]);
$client->executeCommand('admin', $command);
// ConnectionTimeoutException: No suitable servers found
?>
```

### Wrong port number

```php
<?php
$client = new MongoDB\Driver\Manager("mongodb://127.0.0.1:27018");
$command = new MongoDB\Driver\Command(['ping' => 1]);
$client->executeCommand('admin', $command);
// Connection refused — MongoDB listens on 27017 by default
?>
```

### DNS resolution failure

```php
<?php
$client = new MongoDB\Driver\Manager("mongodb://nonexistent-host.internal:27017");
$command = new MongoDB\Driver\Command(['ping' => 1]);
$client->executeCommand('admin', $command);
// ConnectionTimeoutException: DNS resolution failed
?>
```

### Firewall blocking MongoDB port

```php
<?php
$client = new MongoDB\Driver\Manager("mongodb://192.168.1.100:27017");
$command = new MongoDB\Driver\Command(['ping' => 1]);
$client->executeCommand('admin', $command);
// Connection timed out — port blocked by firewall
?>
```

## How to Fix

### Fix 1: Verify MongoDB Is Running

Check that the MongoDB service is active before attempting to connect.

```php
<?php
function checkMongoDBConnection(string $uri): bool
{
    try {
        $client = new MongoDB\Driver\Manager($uri);
        $command = new MongoDB\Driver\Command(['ping' => 1]);
        $result = $client->executeCommand('admin', $command);
        $response = current($result->toArray());
        return ($response->ok ?? 0) === 1;
    } catch (\MongoDB\Driver\Exception\Exception $e) {
        error_log('MongoDB connection failed: ' . $e->getMessage());
        return false;
    }
}

if (!checkMongoDBConnection('mongodb://127.0.0.1:27017')) {
    throw new RuntimeException('MongoDB is not running or unreachable');
}
?>
```

### Fix 2: Validate Connection String Format

Ensure the MongoDB connection URI follows the correct format.

```php
<?php
$host = '127.0.0.1';
$port = 27017;
$database = 'myapp';
$username = 'admin';
$password = 'secret';

// Single server
$uri = "mongodb://{$username}:{$password}@{$host}:{$port}/{$database}";

// Replica set
$uri = "mongodb://{$username}:{$password}@host1:27017,host2:27017,host3:27017/{$database}?replicaSet=myrs";

// DNS seedlist
$uri = "mongodb+srv://{$username}:{$password}@cluster0.example.com/{$database}";

$client = new MongoDB\Driver\Manager($uri);
?>
```

### Fix 3: Increase Connection Timeout

Set appropriate timeouts for slow or distant servers.

```php
<?php
// Default options with timeout
$uri = 'mongodb://127.0.0.1:27017/?connectTimeoutMS=5000&serverSelectionTimeoutMS=5000';
$client = new MongoDB\Driver\Manager($uri);

// With SSL
$uri = 'mongodb://127.0.0.1:27017/?connectTimeoutMS=5000&ssl=true&tlsCAFile=/etc/ssl/certs/ca-certificates.crt';
$client = new MongoDB\Driver\Manager($uri);
?>
```

### Fix 4: Check Network and Firewall Configuration

Verify network connectivity and firewall rules.

```php
<?php
function testMongoDBConnectivity(string $host, int $port): bool
{
    $socket = @fsockopen($host, $port, $errno, $errstr, 5);
    if (!$socket) {
        error_log("Cannot reach MongoDB at {$host}:{$port} — {$errstr} (errno: {$errno})");
        return false;
    }
    fclose($socket);
    return true;
}

if (!testMongoDBConnectivity('127.0.0.1', 27017)) {
    // Check firewall: sudo ufw status | iptables -L -n
    // Check MongoDB bindIp: cat /etc/mongod.conf
    throw new RuntimeException('MongoDB port is not reachable');
}
?>
```

### Fix 5: Configure Connection with Retry Logic

Wrap connection attempts with retry for transient failures.

```php
<?php
function getMongoDBClient(string $uri, int $maxRetries = 3): MongoDB\Driver\Manager
{
    $lastException = null;

    for ($attempt = 1; $attempt <= $maxRetries; $attempt++) {
        try {
            $client = new MongoDB\Driver\Manager($uri);
            $command = new MongoDB\Driver\Command(['ping' => 1]);
            $client->executeCommand('admin', $command);
            return $client;
        } catch (\MongoDB\Driver\Exception\Exception $e) {
            $lastException = $e;
            error_log("MongoDB connection attempt {$attempt} failed: " . $e->getMessage());

            if ($attempt < $maxRetries) {
                sleep(pow(2, $attempt));
            }
        }
    }

    throw new RuntimeException(
        "MongoDB connection failed after {$maxRetries} attempts",
        0,
        $lastException
    );
}

$client = getMongoDBClient('mongodb://127.0.0.1:27017/myapp');
?>
```

## Examples

### MongoDB Connection with Laravel Configuration

```php
<?php
// config/database.php
'mongodb' => [
    'driver' => 'mongodb',
    'host' => env('MONGODB_HOST', '127.0.0.1'),
    'port' => env('MONGODB_PORT', 27017),
    'database' => env('MONGODB_DATABASE'),
    'username' => env('MONGODB_USERNAME'),
    'password' => env('MONGODB_PASSWORD'),
    'options' => [
        'authSource' => env('MONGODB_AUTH_DATABASE', 'admin'),
        'replicaSet' => env('MONGODB_REPLICA_SET'),
        'ssl' => env('MONGODB_SSL', false),
    ],
],
?>
```

## Related Errors

- [MongoDB Auth Error]({{< relref "/languages/php/mongodb-auth-error" >}})
- [MongoDB Query Error]({{< relref "/languages/php/mongodb-query-error" >}})
- [MongoDB Timeout Error]({{< relref "/languages/php/mongodb-timeout-error" >}})
