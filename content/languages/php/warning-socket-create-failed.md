---
title: "[Solution] PHP Warning: socket_create() — Unable to create socket"
description: "Fix PHP Warning: socket_create() Unable to create socket. Check permissions, verify protocol, use correct socket type."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 114
---

# PHP Warning: socket_create() — Unable to create socket

This warning means `socket_create()` failed to create a new socket resource. It can happen due to missing sockets extension, invalid parameters, insufficient permissions, or system resource limits being reached.

## Common Causes

```php
// Cause 1: sockets extension not loaded
<?php
if (!extension_loaded('sockets')) {
    die("sockets extension is not available");
}
$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
?>
```

```php
// Cause 2: Invalid socket type or protocol
<?php
$sock = socket_create(AF_INET, 999, 0);
// Warning: unable to create socket
?>
```

```php
// Cause 3: Insufficient permissions
<?php
// Trying to create raw socket without root
$sock = socket_create(AF_INET, SOCK_RAW, IPPROTO_ICMP);
// Warning: permission denied
?>
```

```php
// Cause 4: Too many open file descriptors
<?php
$sockets = [];
for ($i = 0; $i < 10000; $i++) {
    $sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    if ($sock === false) break;
    $sockets[] = $sock;
}
// Warning: unable to create socket (resource limit)
?>
```

## How to Fix

### Fix 1: Check the sockets Extension

Verify the sockets extension is installed and enabled.

```php
<?php
if (!extension_loaded('sockets')) {
    echo "sockets extension is not loaded.\n";
    echo "Install with: sudo apt-get install php-sockets\n";
    echo "Then restart your web server.";
    exit(1);
}

// Check available socket functions
$functions = get_defined_functions();
$socketFuncs = array_filter($functions['internal'], function ($f) {
    return str_starts_with($f, 'socket_');
});
echo "Available socket functions: " . count($socketFuncs) . "\n";
?>
```

### Fix 2: Use Correct Socket Type and Protocol

Use the appropriate constants for your use case.

```php
<?php
// TCP socket (most common)
$tcpSocket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($tcpSocket === false) {
    echo "Failed to create TCP socket: " . socket_strerror(socket_last_error()) . "\n";
}

// UDP socket
$udpSocket = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);
if ($udpSocket === false) {
    echo "Failed to create UDP socket: " . socket_strerror(socket_last_error()) . "\n";
}

// Unix domain socket
$unixSocket = socket_create(AF_UNIX, SOCK_STREAM, 0);
if ($unixSocket === false) {
    echo "Failed to create Unix socket: " . socket_strerror(socket_last_error()) . "\n";
}
?>
```

### Fix 3: Check Permissions for Raw Sockets

Raw sockets require elevated privileges on most systems.

```php
<?php
// Raw socket requires root or CAP_NET_RAW
$rawSocket = socket_create(AF_INET, SOCK_RAW, IPPROTO_ICMP);
if ($rawSocket === false) {
    $error = socket_last_error();
    if ($error === SOCKET_EACCES) {
        echo "Permission denied. Raw sockets require root privileges.\n";
        echo "Run with: sudo php script.php\n";
    } else {
        echo "Socket error: " . socket_strerror($error) . "\n";
    }
}
?>
```

### Fix 4: Handle Resource Limits

Clean up sockets properly and check system limits.

```php
<?php
function createSocket(int $domain, int $type, int $protocol): resource
{
    $sock = @socket_create($domain, $type, $protocol);

    if ($sock === false) {
        $error = socket_last_error();
        $message = socket_strerror($error);

        if ($error === SOCKET_EMFILE || $error === SOCKET_ENFILE) {
            throw new \RuntimeException(
                "Too many open files. Close unused sockets."
            );
        }

        throw new \RuntimeException("Socket creation failed: {$message}");
    }

    // Set socket options
    socket_set_option($sock, SOL_SOCKET, SO_REUSEADDR, 1);

    return $sock;
}

try {
    $sock = createSocket(AF_INET, SOCK_STREAM, SOL_TCP);
    echo "Socket created successfully\n";
    socket_close($sock);
} catch (\RuntimeException $e) {
    echo "Error: " . $e->getMessage();
}
?>
```

## Examples

```php
<?php
// Complete TCP client with error handling
function createTcpConnection(string $host, int $port, int $timeout = 5): resource
{
    if (!extension_loaded('sockets')) {
        throw new \RuntimeException("sockets extension required");
    }

    $sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    if ($sock === false) {
        throw new \RuntimeException(
            "Failed to create socket: " . socket_strerror(socket_last_error())
        );
    }

    socket_set_option($sock, SOL_SOCKET, SO_RCVTIMEO, ['sec' => $timeout, 'usec' => 0]);
    socket_set_option($sock, SOL_SOCKET, SO_SNDTIMEO, ['sec' => $timeout, 'usec' => 0]);

    if (!socket_connect($sock, $host, $port)) {
        $error = socket_last_error($sock);
        socket_close($sock);
        throw new \RuntimeException(
            "Connection failed: " . socket_strerror($error)
        );
    }

    return $sock;
}

try {
    $sock = createTcpConnection("127.0.0.1", 8080);
    socket_write($sock, "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n");
    $response = socket_read($sock, 1024);
    echo $response;
    socket_close($sock);
} catch (\RuntimeException $e) {
    echo "Error: " . $e->getMessage();
}
?>
```

```php
<?php
// Non-blocking socket server example
function createServerSocket(string $host, int $port): resource
{
    $server = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    if ($server === false) {
        throw new \RuntimeException("Cannot create server socket");
    }

    socket_set_option($server, SOL_SOCKET, SO_REUSEADDR, 1);

    if (!socket_bind($server, $host, $port)) {
        socket_close($server);
        throw new \RuntimeException("Cannot bind to {$host}:{$port}");
    }

    if (!socket_listen($server, 5)) {
        socket_close($server);
        throw new \RuntimeException("Cannot listen on socket");
    }

    socket_set_nonblock($server);
    return $server;
}
?>
```

## Related Errors

- [PHP Warning: socket_bind() Failed](/languages/php/warning-socket-create-failed)
- [PHP Warning: curl_exec() Failed](/languages/php/warning-curl-failed)
- [PHP Memory Limit Error](/languages/php/memory-limit-error)
