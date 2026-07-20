---
title: "[Solution] PHP MEMCACHED_SERIALIZER_ERROR — Serialization Compatibility Issue"
description: "Fix PHP Memcached serializer compatibility issues with igbinary and json. Use consistent serialization across servers."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 114
---

# PHP MEMCACHED_SERIALIZER_ERROR — Serialization Compatibility Issue

Memcached returns garbage data or `false` when different servers or clients use incompatible serializers. One server stores data with `igbinary`, another reads it with `json`, and the result is a deserialization failure. The `Memcached::RES_PAYLOAD_FAILURE` code indicates a serialization mismatch.

## Common Causes

### Different serializer between writes and reads

```php
<?php
// Writer uses igbinary
$mc1 = new Memcached();
$mc1->setOption(Memcached::OPT_SERIALIZER, Memcached::SERIALIZER_IGBINARY);
$mc1->addServer('server1', 11211);
$mc1->set('key', ['data' => 'value']);

// Reader uses json (default)
$mc2 = new Memcached();
$mc2->setOption(Memcached::OPT_SERIALIZER, Memcached::SERIALIZER_JSON);
$mc2->addServer('server1', 11211);
$value = $mc2->get('key'); // false or garbled data
?>
```

### Extension not installed for chosen serializer

```php
<?php
$mc = new Memcached();
$mc->setOption(Memcached::OPT_SERIALIZER, Memcached::SERIALIZER_IGBINARY);
// igbinary extension not installed
// Memcached::RES_PAYLOAD_FAILURE
?>
```

### Mixed PHP versions across servers

```php
<?php
// PHP 8.1 on server A — serializes with default PHP serializer
// PHP 8.3 on server B — cannot unserialize PHP 8.1 internal format
$mc = new Memcached();
$mc->addServer('server-a', 11211);
$mc->set('complex', new stdClass());

$mc2 = new Memcached();
$mc2->addServer('server-b', 11211);
$value = $mc2->get('complex'); // failure
?>
```

### Stale data after serializer change

```php
<?php
// Changed from json to igbinary — old keys still contain json data
$mc = new Memcached();
$mc->setOption(Memcached::OPT_SERIALIZER, Memcached::SERIALIZER_IGBINARY);
$mc->addServer('server1', 11211);

$value = $mc->get('old_key'); // stored with json — deserialization fails
?>
```

### Userland serializer callback mismatch

```php
<?php
$mc = new Memcached();
$mc->setOption(Memcached::OPT_SERIALIZER, Memcached::SERIALIZER_PHP);
$mc->setOption(Memcached::OPT_PREFIX_KEY, 'app_');

// Custom serialization in one process
$mc->setOption(Memcached::OPT_SERIALIZER, function ($value) {
    return json_encode($value);
});

// Different custom serializer in another process
// Data cannot be deserialized by the reader
?>
```

## How to Fix

### Fix 1: Use a Consistent Serializer Across All Clients

Choose one serializer and use it everywhere.

```php
<?php
function createMemcachedClient(array $servers): Memcached
{
    $mc = new Memcached();
    $mc->setOption(Memcached::OPT_SERIALIZER, Memcached::SERIALIZER_JSON);
    $mc->setOption(Memcached::OPT_PREFIX_KEY, 'myapp_');
    $mc->addServers($servers);
    return $mc;
}

// All clients use the same factory
$writer = createMemcachedServerClient([['127.0.0.1', 11211]]);
$reader = createMemcachedServerClient([['127.0.0.1', 11211]]);

$writer->set('key', ['data' => 'value']);
$value = $reader->get('key'); // works correctly
?>
```

### Fix 2: Check for Serializer Extension Before Use

Validate that the required extension is loaded before selecting a serializer.

```php
<?php
function getBestAvailableSerializer(): int
{
    if (extension_loaded('igbinary')) {
        return Memcached::SERIALIZER_IGBINARY;
    }

    if (extension_loaded('msgpack')) {
        return Memcached::SERIALIZER_MSGPACK;
    }

    return Memcached::SERIALIZER_JSON;
}

$mc = new Memcached();
$serializer = getBestAvailableSerializer();
$mc->setOption(Memcached::OPT_SERIALIZER, $serializer);

echo 'Using serializer: ' . match ($serializer) {
    Memcached::SERIALIZER_IGBINARY => 'igbinary',
    Memcached::SERIALIZER_MSGPACK => 'msgpack',
    Memcached::SERIALIZER_JSON => 'json',
    default => 'php',
};
?>
```

### Fix 3: Migrate Data Between Serializers Safely

Flush old data when changing serializers to avoid deserialization errors.

```php
<?php
function migrateSerializer(Memcached $oldClient, Memcached $newClient, string $pattern = '*', int $batchSize = 100): int
{
    $count = 0;
    $allItems = [];

    // Read all keys with old serializer
    $serverList = $oldClient->getServerList();
    foreach ($serverList as $server) {
        $stats = $oldClient->getStats();
        // In practice, use SCAN or a known key list
    }

    // Flush old data
    $oldClient->flush();

    return $count;
}

// Before changing serializer, flush the pool
$oldMc = new Memcached();
$oldMc->setOption(Memcached::OPT_SERIALIZER, Memcached::SERIALIZER_JSON);
$oldMc->addServer('127.0.0.1', 11211);
$oldMc->flush();

// Now use new serializer
$newMc = new Memcached();
$newMc->setOption(Memcached::OPT_SERIALIZER, Memcached::SERIALIZER_IGBINARY);
$newMc->addServer('127.0.0.1', 11211);

$newMc->set('key', ['data' => 'value']); // stored with igbinary
echo $newMc->get('key'); // correctly deserialized
?>
```

### Fix 4: Use JSON as the Safest Cross-Platform Serializer

JSON is human-readable and works across PHP versions and languages.

```php
<?php
$mc = new Memcached();
$mc->setOption(Memcached::OPT_SERIALIZER, Memcached::SERIALIZER_JSON);
$mc->addServer('127.0.0.1', 11211);

// Store complex data
$mc->set('user:42', [
    'id'    => 42,
    'name'  => 'Alice',
    'roles' => ['admin', 'editor'],
    'meta'  => ['last_login' => '2026-01-15 10:30:00'],
]);

// Retrieve — always works with JSON serializer
$user = $mc->get('user:42');
echo $user['name']; // Alice
?>
```

### Fix 5: Handle Serializer Failures Gracefully

Catch and log deserialization failures with fallback logic.

```php
<?php
class SafeMemcachedReader
{
    private Memcached $mc;

    public function __construct(Memcached $mc)
    {
        $this->mc = $mc;
    }

    public function get(string $key): mixed
    {
        $value = $this->mc->get($key);
        $code = $this->mc->getResultCode();

        if ($code === Memcached::RES_PAYLOAD_FAILURE) {
            error_log(sprintf(
                'Serializer failure for key "%s" — possible data format mismatch. '
                . 'Flush key or migrate data to current serializer.',
                $key
            ));
            // Delete corrupted key
            $this->mc->delete($key);
            return null;
        }

        if ($code !== Memcached::RES_SUCCESS && $code !== Memcached::RES_NOTFOUND) {
            error_log('Memcached error for key "' . $key . '": ' . $this->mc->getResultMessage());
        }

        return $value;
    }
}

$reader = new SafeMemcachedReader($mc);
$value = $reader->get('possibly_corrupt_key');
?>
```

## Examples

### Serializer Benchmark Comparison

```php
<?php
function benchmarkSerializers(array $data, int $iterations = 10000): array
{
    $results = [];

    $serializers = [
        'json'      => Memcached::SERIALIZER_JSON,
        'igbinary'  => extension_loaded('igbinary') ? Memcached::SERIALIZER_IGBINARY : null,
        'msgpack'   => extension_loaded('msgpack') ? Memcached::SERIALIZER_MSGPACK : null,
    ];

    foreach ($serializers as $name => $serializer) {
        if ($serializer === null) {
            $results[$name] = ['status' => 'extension not installed'];
            continue;
        }

        $mc = new Memcached();
        $mc->setOption(Memcached::OPT_SERIALIZER, $serializer);
        $mc->addServer('127.0.0.1', 11211);

        $start = microtime(true);
        for ($i = 0; $i < $iterations; $i++) {
            $mc->set("bench:{$i}", $data);
            $mc->get("bench:{$i}");
        }
        $elapsed = round(microtime(true) - $start, 4);

        $results[$name] = [
            'iterations' => $iterations,
            'time'       => $elapsed . 's',
            'per_op'     => round(($elapsed / $iterations) * 1000000, 2) . 'µs',
        ];

        $mc->flush();
    }

    return $results;
}

$results = benchmarkSerializers(['users' => range(1, 100), 'meta' => ['version' => '1.0']]);
print_r($results);
?>
```

## Related Errors

- [Memcached Get Error]({{< relref "/languages/php/memcached-get-error" >}})
- [Memcached Connection Error]({{< relref "/languages/php/memcached-connection-error" >}})
- [Redis Pipeline Error]({{< relref "/languages/php/redis-pipeline-error" >}})
