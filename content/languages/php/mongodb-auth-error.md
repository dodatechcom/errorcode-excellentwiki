---
title: "[Solution] PHP MONGODB_AUTH_ERROR — MongoDB Authentication Failed"
description: "Fix PHP MongoDB authentication failed. Check credentials, verify database user, and handle auth database. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 106
---

# PHP MONGODB_AUTH_ERROR — MongoDB Authentication Failed

The MongoDB server rejected the authentication credentials. This error occurs when the username or password is incorrect, the user does not exist in the specified authentication database, or SCRAM authentication fails.

## Common Causes

### Wrong username or password

```php
<?php
$uri = 'mongodb://admin:wrongpassword@127.0.0.1:27017/myapp';
$client = new MongoDB\Driver\Manager($uri);
$command = new MongoDB\Driver\Command(['ping' => 1]);
$client->executeCommand('myapp', $command);
// MongoDB\Driver\Exception\AuthenticationException: Authentication failed
?>
```

### Authentication database mismatch

```php
<?php
// User is defined in admin database but client connects to myapp
$uri = 'mongodb://admin:secret@127.0.0.1:27017/myapp';
$client = new MongoDB\Driver\Manager($uri);
$command = new MongoDB\Driver\Command(['ping' => 1]);
$client->executeCommand('myapp', $command);
// AuthenticationException — authSource defaults to database in URI
?>
```

### User does not have required privileges

```php
<?php
$uri = 'mongodb://reader:secret@127.0.0.1:27017/myapp';
$client = new MongoDB\Driver\Manager($uri);
$command = new MongoDB\Driver\Command([
    'create' => 'new_collection',
]);
$client->executeCommand('myapp', $command);
// AuthenticationException or AuthorizationException — insufficient privileges
?>
```

### SCRAM mechanism mismatch

```php
<?php
$uri = 'mongodb://admin:secret@127.0.0.1:27017/myapp?authMechanism=MONGODB-X509';
$client = new MongoDB\Driver\Manager($uri);
$command = new MongoDB\Driver\Command(['ping' => 1]);
$client->executeCommand('myapp', $command);
// AuthenticationException — wrong auth mechanism
?>
```

### Special characters in password

```php
<?php
// Password contains @, /, or other URI-reserved characters
$uri = 'mongodb://admin:p@ss/w0rd@127.0.0.1:27017/myapp';
// URI is malformed — @ and / break parsing
$client = new MongoDB\Driver\Manager($uri);
// AuthenticationException or connection failure
?>
```

## How to Fix

### Fix 1: Verify Credentials and Auth Database

Ensure the username, password, and authSource are correct.

```php
<?php
$username = 'myuser';
$password = 'correctpassword';
$authDatabase = 'admin';
$host = '127.0.0.1';
$port = 27017;
$database = 'myapp';

// URL-encode special characters in password
$encodedPassword = urlencode($password);
$uri = "mongodb://{$username}:{$encodedPassword}@{$host}:{$port}/{$database}?authSource={$authDatabase}";

$client = new MongoDB\Driver\Manager($uri);
$command = new MongoDB\Driver\Command(['ping' => 1]);
$result = $client->executeCommand($database, $command);
echo 'Connected successfully';
?>
```

### Fix 2: Create User with Correct Privileges

```php
<?php
$client = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$command = new MongoDB\Driver\Command([
    'createUser' => 'myapp_user',
    'pwd' => 'securepassword',
    'roles' => [
        ['role' => 'readWrite', 'db' => 'myapp'],
        ['role' => 'read', 'db' => 'reporting'],
    ],
    'mechanisms' => ['SCRAM-SHA-256'],
]);

$result = $client->executeCommand('admin', $command);
?>
```

### Fix 3: Use authSource Parameter

Explicitly set the authentication database in the connection string.

```php
<?php
// User exists in admin database
$uri = 'mongodb://admin:secret@127.0.0.1:27017/myapp?authSource=admin';
$client = new MongoDB\Driver\Manager($uri);

// User exists in custom auth database
$uri = 'mongodb://appuser:secret@127.0.0.1:27017/myapp?authSource=authdb';
$client = new MongoDB\Driver\Manager($uri);
?>
```

### Fix 4: Handle Password Special Characters

```php
<?php
$username = 'admin';
$password = 'p@ss/w0rd!#$';
$host = '127.0.0.1';
$port = 27017;
$database = 'myapp';

// Always URL-encode credentials
$encodedUser = rawurlencode($username);
$encodedPass = rawurlencode($password);

$uri = "mongodb://{$encodedUser}:{$encodedPass}@{$host}:{$port}/{$database}?authSource=admin";
$client = new MongoDB\Driver\Manager($uri);
?>
```

### Fix 5: Handle Authentication Exceptions Gracefully

```php
<?php
function authenticateMongoDB(string $uri, string $database): MongoDB\Driver\Manager
{
    try {
        $client = new MongoDB\Driver\Manager($uri);
        $command = new MongoDB\Driver\Command(['ping' => 1]);
        $client->executeCommand($database, $command);
        return $client;
    } catch (\MongoDB\Driver\Exception\AuthenticationException $e) {
        error_log('MongoDB auth failed: ' . $e->getMessage());
        throw new RuntimeException('Database authentication failed. Check credentials and auth database.', 0, $e);
    } catch (\MongoDB\Driver\Exception\Exception $e) {
        error_log('MongoDB error: ' . $e->getMessage());
        throw $e;
    }
}

$client = authenticateMongoDB(
    'mongodb://admin:secret@127.0.0.1:27017/myapp?authSource=admin',
    'myapp'
);
?>
```

## Examples

### Environment-Based MongoDB Authentication

```php
<?php
function createMongoDBClient(): MongoDB\Driver\Manager
{
    $host = getenv('MONGODB_HOST') ?: '127.0.0.1';
    $port = getenv('MONGODB_PORT') ?: '27017';
    $user = getenv('MONGODB_USERNAME');
    $pass = getenv('MONGODB_PASSWORD');
    $database = getenv('MONGODB_DATABASE');
    $authDb = getenv('MONGODB_AUTH_DATABASE') ?: 'admin';

    $encodedUser = rawurlencode($user);
    $encodedPass = rawurlencode($pass);

    $uri = "mongodb://{$encodedUser}:{$encodedPass}@{$host}:{$port}/{$database}?authSource={$authDb}";

    $client = new MongoDB\Driver\Manager($uri);

    // Verify connection
    $command = new MongoDB\Driver\Command(['ping' => 1]);
    $client->executeCommand('admin', $command);

    return $client;
}
?>
```

## Related Errors

- [MongoDB Connection Error]({{< relref "/languages/php/mongodb-connection-error" >}})
- [MongoDB Query Error]({{< relref "/languages/php/mongodb-query-error" >}})
- [Redis Auth Error]({{< relref "/languages/php/redis-auth-error" >}})
