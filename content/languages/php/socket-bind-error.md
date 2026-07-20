---
title: "[Solution] PHP socket_bind() Failed — Cannot Bind to Address"
description: "Fix PHP socket_bind() failed by checking port availability, verifying permissions, using SO_REUSEADDR, and checking address format. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 10
---

# PHP socket_bind() Failed — Cannot Bind to Address

The `socket_bind()` function failed to bind the socket to the specified address and port. This commonly occurs when the port is already in use, the address format is invalid, or the process lacks sufficient privileges.

## Common Causes

```php
// Cause 1: Port already in use
$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_bind($sock, '0.0.0.0', 80); // Port 80 requires root

// Cause 2: Insufficient permissions for low ports
$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_bind($sock, '0.0.0.0', 80); // EACCES error

// Cause 3: Address in use (TIME_WAIT state)
$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_bind($sock, '127.0.0.1', 8080); // Previous connection still closing

// Cause 4: Invalid address format
$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_bind($sock, '999.999.999.999', 8080);

// Cause 5: Socket already bound
$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_bind($sock, '127.0.0.1', 8080);
socket_bind($sock, '127.0.0.1', 8080); // Already bound
```

## How to Fix

### Fix 1: Check Port Availability

```php
function isPortAvailable(string $address, int $port): bool {
    $sock = @socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    if ($sock === false) {
        return false;
    }

    $result = @socket_bind($sock, $address, $port);
    socket_close($sock);

    return $result !== false;
}

// Usage
if (isPortAvailable('0.0.0.0', 8080)) {
    echo 'Port 8080 is available';
} else {
    echo 'Port 8080 is in use';
}
```

### Fix 2: Use SO_REUSEADDR to Avoid TIME_WAIT

```php
$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($sock === false) {
    error_log('socket_create failed');
    return;
}

// Allow reuse of local addresses
socket_set_option($sock, SOL_SOCKET, SO_REUSEADDR, 1);

$result = socket_bind($sock, '0.0.0.0', 8080);
if ($result === false) {
    $error = socket_last_error($sock);
    error_log('socket_bind failed: ' . socket_strerror($error));
    socket_close($sock);
    return;
}

echo 'Successfully bound to port 8080';
```

### Fix 3: Validate Address Format

```php
function safeBindSocket(string $address, int $port): ?resource {
    if (!filter_var($address, FILTER_VALIDATE_IP)) {
        error_log("Invalid IP address: {$address}");
        return null;
    }

    if ($port < 1 || $port > 65535) {
        error_log("Invalid port: {$port}");
        return null;
    }

    $sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    if ($sock === false) {
        error_log('socket_create failed');
        return null;
    }

    socket_set_option($sock, SOL_SOCKET, SO_REUSEADDR, 1);

    if (!socket_bind($sock, $address, $port)) {
        $error = socket_last_error($sock);
        error_log("socket_bind failed: " . socket_strerror($error));
        socket_close($sock);
        return null;
    }

    return $sock;
}
```

### Fix 4: Run with Appropriate Privileges

```bash
# For ports below 1024, run as root or use capabilities
sudo php server.php

# Or set capabilities on the PHP binary
sudo setcap cap_net_bind_service=+ep $(which php)
```

## Examples

```php
// Example: TCP server with proper binding
function startTcpServer(string $host, int $port, int $backlog = 5): ?resource {
    $sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    if ($sock === false) {
        error_log('socket_create failed');
        return null;
    }

    socket_set_option($sock, SOL_SOCKET, SO_REUSEADDR, 1);
    socket_set_option($sock, SOL_SOCKET, SO_KEEPALIVE, 1);

    if (!socket_bind($sock, $host, $port)) {
        error_log("Cannot bind to {$host}:{$port} — " . socket_strerror(socket_last_error($sock)));
        socket_close($sock);
        return null;
    }

    if (!socket_listen($sock, $backlog)) {
        error_log("Cannot listen — " . socket_strerror(socket_last_error($sock)));
        socket_close($sock);
        return null;
    }

    echo "Server listening on {$host}:{$port}\n";
    return $sock;
}
```

## Related Errors

- [socket_create() failed](/languages/php/socket-create-error/)
- [socket_connect() failed](/languages/php/socket-connect-error/)
- [socket_listen() failed](/languages/php/socket-listen-error/)
