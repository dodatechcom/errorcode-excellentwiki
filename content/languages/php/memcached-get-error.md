---
title: "[Solution] PHP MEMCACHED_GET_ERROR — Memcached::get() Failed"
description: "Fix PHP Memcached::get() returning false with resultCode() errors. Handle connection checks and key lookups."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 112
---

# PHP MEMCACHED_GET_ERROR — Memcached::get() Failed

`Memcached::get()` returns `false` and `resultCode()` reports `Memcached::RES_NOTFOUND`, `Memcached::RES_NOTCONNECTED`, or `Memcached::RES_UNKNOWN_READ_FAILURE`. This can mean the key does not exist, the server is disconnected, or an internal error occurred. Distinguishing between "key not found" and "connection error" is critical.

## Common Causes

### Assuming false means "key not found"

```php
<?php
$mc = new Memcached();
$mc->addServer('127.0.0.1', 11211);

$value = $mc->get('mykey');
if ($value === false) {
    // WRONG: this also triggers on connection errors
    echo 'Key not found';
}
?>
```

### Server disconnected before get

```php
<?php
$mc = new Memcached();
$mc->addServer('127.0.0.1', 11211);
// server goes down after addServer
$value = $mc->get('mykey');
var_dump($mc->getResultCode()); // Memcached::RES_NOTCONNECTED
?>
```

### Result code not checked

```php
<?php
$mc = new Memcached();
$mc->addServer('127.0.0.1', 11211);

$count = $mc->getByKey('user_1', 'counter');
// If server is down, $count is false — but code treats it as 0
echo (int) $count; // 0 — silently wrong
?>
```

### Using false as a sentinel value

```php
<?php
$mc = new Memcached();
$mc->addServer('127.0.0.1', 11211);

// Store a value that happens to be false or empty
$mc->set('flag', false);
$value = $mc->get('flag');
// $value is false — indistinguishable from error
?>
```

### Multi-server get with mixed results

```php
<?php
$mc = new Memcached();
$mc->addServer('server1', 11211);
$mc->addServer('server2', 11211);

$results = $mc->getMulti(['key1', 'key2', 'key3']);
// server2 is down — some keys return, others don't
var_dump($mc->getResultCode()); // mixed codes
?>
```

## How to Fix

### Fix 1: Always Check resultCode After get()

Distinguish between "not found" and actual errors using `getResultCode()`.

```php
<?php
$mc = new Memcached();
$mc->addServer('127.0.0.1', 11211);

$value = $mc->get('mykey');
$code = $mc->getResultCode();

switch ($code) {
    case Memcached::RES_SUCCESS:
        echo "Found: {$value}";
        break;
    case Memcached::RES_NOTFOUND:
        echo "Key does not exist";
        break;
    case Memcached::RES_NOTCONNECTED:
        echo "Server is not connected";
        break;
    default:
        echo "Error: " . $mc->getResultMessage();
        break;
}
?>
```

### Fix 2: Use getResultMessage() for Diagnostics

Get a human-readable error message for logging and debugging.

```php
<?php
function memcachedGet(Memcached $mc, string $key): mixed
{
    $value = $mc->get($key);
    $code = $mc->getResultCode();

    if ($code !== Memcached::RES_SUCCESS && $code !== Memcached::RES_NOTFOUND) {
        error_log(sprintf(
            'Memcached get failed for key "%s": code=%d message=%s',
            $key,
            $code,
            $mc->getResultMessage()
        ));
    }

    return $value;
}

$mc = new Memcached();
$mc->addServer('127.0.0.1', 11211);

$result = memcachedGet($mc, 'session_abc');
?>
```

### Fix 3: Use a Wrapper That Handles All Error States

Create a helper that returns a typed result for safe handling.

```php
<?php
class MemcachedReader
{
    private Memcached $mc;

    public function __construct(Memcached $mc)
    {
        $this->mc = $mc;
    }

    public function get(string $key): array
    {
        $value = $this->mc->get($key);
        $code = $this->mc->getResultCode();

        return match ($code) {
            Memcached::RES_SUCCESS => ['found' => true, 'value' => $value, 'code' => $code],
            Memcached::RES_NOTFOUND => ['found' => false, 'value' => null, 'code' => $code],
            default => [
                'found' => false,
                'value' => null,
                'code' => $code,
                'error' => $this->mc->getResultMessage(),
            ],
        };
    }
}

$reader = new MemcachedReader($mc);
$result = $reader->get('mykey');

if (!$result['found']) {
    if (isset($result['error'])) {
        error_log('Connection error: ' . $result['error']);
    } else {
        echo 'Key not found — setting default';
        $mc->set('mykey', 'default_value');
    }
}
?>
```

### Fix 4: Use Memcached::RES_NOTFOUND as Sentinel

Check for `NOTFOUND` specifically instead of relying on `false`.

```php
<?php
$mc = new Memcached();
$mc->addServer('127.0.0.1', 11211);

$value = $mc->get('mykey');
$code = $mc->getResultCode();

if ($code === Memcached::RES_NOTFOUND) {
    $value = computeDefaultValue();
    $mc->set('mykey', $value, 3600);
} elseif ($code !== Memcached::RES_SUCCESS) {
    throw new RuntimeException('Memcached error: ' . $mc->getResultMessage());
}

echo $value;
?>
```

### Fix 5: Handle Multi-Get with Per-Key Error Checking

Use `getMulti()` with `Memcached::GET_PRESERVE_ORDER` and check each result.

```php
<?php
$mc = new Memcached();
$mc->addServer('127.0.0.1', 11211);
$mc->setOption(Memcached::OPT_GET_PRESERVE_ORDER, true);

$keys = ['session:a', 'session:b', 'session:c'];
$results = $mc->getMulti($keys, Memcached::GET_PRESERVE_ORDER);

$code = $mc->getResultCode();
if ($code !== Memcached::RES_SUCCESS) {
    error_log('getMulti failed: ' . $mc->getResultMessage());
}

foreach ($keys as $i => $key) {
    $val = $results[$key] ?? null;
    $found = $mc->getResultCode() === Memcached::RES_SUCCESS;

    if ($found) {
        echo "{$key}: {$val}" . PHP_EOL;
    } else {
        echo "{$key}: NOT FOUND" . PHP_EOL;
    }
}
?>
```

## Examples

### Session Handler with Proper Error Handling

```php
<?php
class MemcachedSessionReader
{
    private Memcached $mc;
    private string $prefix;

    public function __construct(Memcached $mc, string $prefix = 'sess_')
    {
        $this->mc = $mc;
        $this->prefix = $prefix;
    }

    public function read(string $id): string|false
    {
        $key = $this->prefix . $id;
        $data = $this->mc->get($key);
        $code = $this->mc->getResultCode();

        return match ($code) {
            Memcached::RES_SUCCESS => $data,
            Memcached::RES_NOTFOUND => '',
            default => false,
        };
    }
}
?>
```

### Cache-Aside Pattern with Fallback

```php
<?php
function cacheAside(Memcached $mc, string $key, callable $computation, int $ttl = 3600): mixed
{
    $value = $mc->get($key);
    $code = $mc->getResultCode();

    if ($code === Memcached::RES_SUCCESS) {
        return $value;
    }

    if ($code !== Memcached::RES_NOTFOUND) {
        error_log('Memcached read error: ' . $mc->getResultMessage());
    }

    // Compute and store
    $value = $computation();
    $mc->set($key, $value, $ttl);
    return $value;
}

$mc = new Memcached();
$mc->addServer('127.0.0.1', 11211);

$user = cacheAside($mc, 'user:42', fn() => fetchUserFromDB(42));
?>
```

## Related Errors

- [Memcached Connection Error]({{< relref "/languages/php/memcached-connection-error" >}})
- [Memcached Server Mark Bad]({{< relref "/languages/php/memcached-server-mark-bad" >}})
- [Memcached Serializer Error]({{< relref "/languages/php/memcached-serializer-error" >}})
