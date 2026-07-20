---
title: "[Solution] PHP socket_connect() Failed — Cannot Connect to Remote Host"
description: "Fix PHP socket_connect() failed by verifying host/port, checking firewall, verifying network connectivity, and using correct socket type. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 11
---

# PHP socket_connect() Failed — Cannot Connect to Remote Host

The `socket_connect()` function failed to establish a connection to the specified remote host and port. This may be caused by an unreachable host, closed port, firewall blocking, or incorrect socket type.

## Common Causes

```php
// Cause 1: Host is unreachable
$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_connect($sock, '192.168.99.99', 80); // Host does not exist

// Cause 2: Port not listening
$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_connect($sock, '127.0.0.1', 9999); // No service on that port

// Cause 3: Firewall blocking connection
$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_connect($sock, '10.0.0.1', 443); // Firewall drops packets

// Cause 4: DNS resolution failure
$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_connect($sock, 'nonexistent.invalid', 80);

// Cause 5: Wrong socket type for protocol
$sock = socket_create(AF_INET, SOCK_DGRAM, SOL_TCP); // Mismatched type/protocol
socket_connect($sock, '127.0.0.1', 80);
```

## How to Fix

### Fix 1: Verify Host and Port Before Connecting

```php
function verifyHost(string $host, int $port, int $timeout = 3): bool {
    $ip = @gethostbyname($host);
    if ($ip === $host) {
        error_log("DNS resolution failed for: {$host}");
        return false;
    }

    $sock = @socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    if ($sock === false) {
        return false;
    }

    socket_set_option($sock, SOL_SOCKET, SO_SNDTIMEO, ['sec' => $timeout, 'usec' => 0]);
    socket_set_option($sock, SOL_SOCKET, SO_RCVTIMEO, ['sec' => $timeout, 'usec' => 0]);

    $connected = @socket_connect($sock, $ip, $port);
    socket_close($sock);

    return $connected !== false;
}
```

### Fix 2: Set Connection Timeout

```php
function connectWithTimeout(string $host, int $port, int $timeoutSec = 5): ?resource {
    $ip = gethostbyname($host);
    if ($ip === $host) {
        error_log("Cannot resolve host: {$host}");
        return null;
    }

    $sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    if ($sock === false) {
        error_log('socket_create failed: ' . socket_strerror(socket_last_error()));
        return null;
    }

    socket_set_option($sock, SOL_SOCKET, SO_SNDTIMEO, ['sec' => $timeoutSec, 'usec' => 0]);
    socket_set_option($sock, SOL_SOCKET, SO_RCVTIMEO, ['sec' => $timeoutSec, 'usec' => 0]);

    $result = @socket_connect($sock, $ip, $port);
    if ($result === false) {
        $error = socket_last_error($sock);
        error_log("Connection to {$host}:{$port} failed: " . socket_strerror($error));
        socket_close($sock);
        return null;
    }

    return $sock;
}
```

### Fix 3: Use Correct Socket Type

```php
// TCP connection
$tcpSock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);

// UDP connection
$udpSock = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);

// IPv6 connection
$ipv6Sock = socket_create(AF_INET6, SOCK_STREAM, SOL_TCP);
socket_connect($ipv6Sock, '::1', 8080);

// Unix domain socket
$unixSock = socket_create(AF_UNIX, SOCK_STREAM, 0);
socket_connect($unixSock, '/var/run/myapp.sock');
```

## Examples

```php
// Example: TCP client with retry logic
function connectToServer(string $host, int $port, int $maxRetries = 3, int $delayMs = 1000): ?resource {
    for ($attempt = 1; $attempt <= $maxRetries; $attempt++) {
        $sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
        if ($sock === false) {
            error_log("Attempt {$attempt}: socket_create failed");
            sleep((int)($delayMs / 1000));
            continue;
        }

        socket_set_option($sock, SOL_SOCKET, SO_SNDTIMEO, ['sec' => 5, 'usec' => 0]);
        socket_set_option($sock, SOL_SOCKET, SO_RCVTIMEO, ['sec' => 5, 'usec' => 0]);

        $connected = @socket_connect($sock, $host, $port);
        if ($connected !== false) {
            return $sock;
        }

        $error = socket_last_error($sock);
        error_log("Attempt {$attempt}: Connection failed — " . socket_strerror($error));
        socket_close($sock);

        if ($attempt < $maxRetries) {
            usleep($delayMs * 1000);
        }
    }

    return null;
}
```

## Related Errors

- [socket_create() failed](/languages/php/socket-create-error/)
- [socket_bind() failed](/languages/php/socket-bind-error/)
- [socket_listen() failed](/languages/php/socket-listen-error/)
