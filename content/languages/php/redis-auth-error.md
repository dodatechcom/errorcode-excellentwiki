---
title: "[Solution] PHP REDIS_AUTH_ERROR — Redis Authentication Failed"
description: "Fix PHP Redis NOAUTH and ERR invalid password errors. Handle Redis authentication with ACL and AUTH commands."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 107
---

# PHP REDIS_AUTH_ERROR — Redis Authentication Failed

Redis returns `NOAUTH Authentication required` or `ERR invalid password` when you attempt to run commands on a protected server without valid credentials. This error occurs when the Redis instance has `requirepass` or ACL-based authentication enabled and the PHP code does not authenticate or uses wrong credentials.

## Common Causes

### No authentication provided

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->get('mykey');
// RedisException: NOAUTH Authentication required
?>
```

### Wrong password

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->auth('wrong_password_here');
// RedisException: ERR invalid password
?>
```

### Authentication after persistent connection

```php
<?php
$redis = new Redis();
$redis->pconnect('127.0.0.1', 6379); // may already be authenticated from previous session
$redis->auth('my_password');
// RedisException: ERR Client sent AUTH, but no password is set
?>
```

### ACL user mismatch

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->auth('limited_user'); // user exists but lacks required permissions
// RedisException: NOPERM this user has no permissions to run 'get' command
?>
```

### Password loaded from wrong environment

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->auth(getenv('REDIS_PASSWORD')); // returns empty string
// RedisException: ERR invalid password
?>
```

## How to Fix

### Fix 1: Authenticate After Connection

Always call `auth()` immediately after `connect()` when Redis requires authentication.

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$password = getenv('REDIS_PASSWORD');
if ($password === false || $password === '') {
    throw new RuntimeException('REDIS_PASSWORD environment variable is not set');
}

$redis->auth($password);
$redis->ping(); // +PONG
?>
```

### Fix 2: Use Connection URLs for Authentication

Pass credentials as part of a DSN URL to simplify configuration.

```php
<?php
$redis = new Redis();

// Parse DSN: redis://user:password@host:port/db
$dsn = getenv('REDIS_URL') ?: 'redis://default:secret@127.0.0.1:6379/0';
$parsed = parse_url($dsn);

$redis->connect($parsed['host'], $parsed['port'] ?? 6379);
if (isset($parsed['pass'])) {
    $redis->auth($parsed['pass']);
}
if (isset($parsed['path'])) {
    $redis->select((int) substr($parsed['path'], 1));
}
?>
```

### Fix 3: Handle Authentication Errors Gracefully

Use try-catch to detect and recover from auth failures.

```php
<?php
class RedisAuthManager
{
    private Redis $redis;
    private string $host;
    private int $port;

    public function __construct(string $host, int $port = 6379)
    {
        $this->redis = new Redis();
        $this->host = $host;
        $this->port = $port;
    }

    public function authenticate(string $password): void
    {
        $this->redis->connect($this->host, $this->port);

        try {
            $this->redis->auth($password);
        } catch (RedisException $e) {
            $this->redis->close();
            if (str_contains($e->getMessage(), 'NOAUTH')) {
                throw new RuntimeException('Redis server requires authentication but no password was provided', 0, $e);
            }
            if (str_contains($e->getMessage(), 'invalid password')) {
                throw new RuntimeException('Redis authentication failed — invalid password', 0, $e);
            }
            throw $e;
        }
    }

    public function getRedis(): Redis
    {
        return $this->redis;
    }
}
?>
```

### Fix 4: Check Redis ACL Permissions

For Redis 6+ with ACL, verify the user has the required command permissions.

```bash
# Check user permissions in Redis CLI
ACL LIST
ACL GETUSER myuser

# Grant permissions
ACL SETUSER myuser on >password ~* &* +get +set +del
```

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->auth('myuser', 'mypassword'); // Redis 6+ supports user:password auth

// Verify permissions
$perm = $redis->acl('whoami');
?>
```

### Fix 5: Use Environment Variables with Validation

Load Redis credentials from environment variables and validate them at startup.

```php
<?php
function createAuthenticatedRedis(): Redis
{
    $host = $_ENV['REDIS_HOST'] ?? '127.0.0.1';
    $port = (int) ($_ENV['REDIS_PORT'] ?? 6379);
    $password = $_ENV['REDIS_PASSWORD'] ?? '';

    if ($password === '') {
        throw new RuntimeException(
            'REDIS_PASSWORD must be set in environment variables. '
            . 'Check your .env file or server configuration.'
        );
    }

    $redis = new Redis();
    $redis->connect($host, $port, 3.0);
    $redis->auth($password);
    return $redis;
}
?>
```

## Examples

### Redis Connection with Auth in Laravel

```php
<?php
// .env
// REDIS_HOST=127.0.0.1
// REDIS_PASSWORD=secret
// REDIS_PORT=6379

// config/database.php
'redis' => [
    'client' => env('REDIS_CLIENT', 'phpredis'),
    'default' => [
        'host' => env('REDIS_HOST', '127.0.0.1'),
        'password' => env('REDIS_PASSWORD'),
        'port' => env('REDIS_PORT', '6379'),
        'database' => 0,
    ],
],
?>
```

### Multi-DB Auth Setup

```php
<?php
function createMultiDbRedis(array $databases): array
{
    $connections = [];

    foreach ($databases as $name => $config) {
        $redis = new Redis();
        $redis->connect($config['host'], $config['port']);
        $redis->auth($config['password']);
        $redis->select($config['database']);
        $connections[$name] = $redis;
    }

    return $connections;
}

$dbs = createMultiDbRedis([
    'cache' => ['host' => '127.0.0.1', 'port' => 6379, 'password' => 'secret', 'database' => 0],
    'queue' => ['host' => '127.0.0.1', 'port' => 6379, 'password' => 'secret', 'database' => 1],
    'session' => ['host' => '127.0.0.1', 'port' => 6379, 'password' => 'secret', 'database' => 2],
]);
?>
```

## Related Errors

- [Redis Connection Error]({{< relref "/languages/php/redis-connection-error" >}})
- [Redis Timeout Error]({{< relref "/languages/php/redis-timeout-error" >}})
- [Memcached Connection Error]({{< relref "/languages/php/memcached-connection-error" >}})
