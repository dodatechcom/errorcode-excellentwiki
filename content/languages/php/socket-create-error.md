---
title: "[Solution] PHP socket_create() Failed — Cannot Create Socket"
description: "Fix PHP socket_create() failed by checking permissions, verifying protocol family, installing sockets extension, and checking firewall. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 9
---

# PHP socket_create() Failed — Cannot Create Socket

The `socket_create()` function failed to create a new socket resource. This typically occurs when the sockets extension is not installed, invalid parameters are passed, or the system lacks the necessary permissions.

## Common Causes

```php
// Cause 1: Sockets extension not loaded
$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP); // Returns false

// Cause 2: Invalid address family
$sock = socket_create(999, SOCK_STREAM, SOL_TCP); // Unknown family

// Cause 3: Invalid socket type
$sock = socket_create(AF_INET, 999, SOL_TCP); // Unknown type

// Cause 4: Insufficient permissions for raw sockets
$sock = socket_create(AF_INET, SOCK_RAW, SOL_ICMP); // Requires root

// Cause 5: Too many open file descriptors
// System limit reached (ulimit -n)
$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
```

## How to Fix

### Fix 1: Verify Sockets Extension

```php
if (extension_loaded('sockets')) {
    echo 'Sockets extension is loaded.';
} else {
    echo 'Sockets extension is NOT loaded.';
}
```

```bash
# Install sockets extension on Ubuntu/Debian
sudo apt-get install php-sockets

# Install via PECL
pecl install sockets

# Verify installation
php -m | grep sockets
```

### Fix 2: Validate Parameters Before Creating

```php
function safeCreateSocket(int $domain, int $type, int $protocol): ?resource {
    $validDomains = [AF_INET, AF_INET6, AF_UNIX, AF_UNSPEC];
    $validTypes = [SOCK_STREAM, SOCK_DGRAM, SOCK_RAW, SOCK_SEQPACKET];

    if (!in_array($domain, $validDomains)) {
        error_log("Invalid socket domain: {$domain}");
        return null;
    }

    if (!in_array($type, $validTypes)) {
        error_log("Invalid socket type: {$type}");
        return null;
    }

    $sock = socket_create($domain, $type, $protocol);
    if ($sock === false) {
        $error = socket_strerror(socket_last_error());
        error_log("socket_create failed: {$error}");
        return null;
    }

    return $sock;
}
```

### Fix 3: Handle Socket Errors Properly

```php
function createTcpSocket(string $address, int $port): ?resource {
    $sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    if ($sock === false) {
        error_log('socket_create failed: ' . socket_strerror(socket_last_error()));
        return null;
    }

    socket_clear_error($sock);

    $result = @socket_connect($sock, $address, $port);
    if ($result === false) {
        $error = socket_last_error($sock);
        error_log("socket_connect failed: " . socket_strerror($error));
        socket_close($sock);
        return null;
    }

    return $sock;
}
```

## Examples

```php
// Example: Create and configure a TCP client socket
function createTcpClient(string $host, int $timeout = 5): ?resource {
    $sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    if ($sock === false) {
        error_log('Failed to create socket');
        return null;
    }

    // Set options
    socket_set_option($sock, SOL_SOCKET, SO_KEEPALIVE, 1);
    socket_set_option($sock, SOL_SOCKET, SO_RCVTIMEO, ['sec' => $timeout, 'usec' => 0]);
    socket_set_option($sock, SOL_SOCKET, SO_SNDTIMEO, ['sec' => $timeout, 'usec' => 0]);

    $ip = gethostbyname($host);
    if ($ip === $host) {
        error_log("Could not resolve host: {$host}");
        socket_close($sock);
        return null;
    }

    $connected = @socket_connect($sock, $ip, 80);
    if ($connected === false) {
        error_log('Connection failed: ' . socket_strerror(socket_last_error($sock)));
        socket_close($sock);
        return null;
    }

    return $sock;
}
```

## Related Errors

- [socket_bind() failed](/languages/php/socket-bind-error/)
- [socket_connect() failed](/languages/php/socket-connect-error/)
- [socket_listen() failed](/languages/php/socket-listen-error/)
