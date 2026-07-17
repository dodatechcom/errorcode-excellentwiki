---
title: "[Solution] std::system_error Socket Error Fix"
description: "Fix std::system_error socket errors. Handle network socket failures, connection errors, and platform-specific error codes."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# std::system_error Socket Error

Fix std::system_error socket errors. Handle network socket failures, connection errors, and platform-specific error codes.

## What This Error Means

`std::system_error` wraps OS-level socket errors:

```
std::system_error: Error code 111: Connection refused
std::system_error: Error code 113: No route to host
```

## Common Causes

```cpp
// Cause 1: Server not listening on target port
// Cause 2: Firewall blocking connection
// Cause 3: Socket already in use (TIME_WAIT)
// Cause 4: File descriptor limit reached
// Cause 5: Network unreachable
```

## How to Fix

### Fix 1: Handle specific error codes

```cpp
#include <system_error>
#include <iostream>

void handle_socket_error(const std::system_error& e) {
    switch (e.code().value()) {
        case ECONNREFUSED:
            std::cerr << "Connection refused - server not running" << std::endl;
            break;
        case EADDRINUSE:
            std::cerr << "Address already in use" << std::endl;
            break;
        case ETIMEDOUT:
            std::cerr << "Connection timed out" << std::endl;
            break;
        default:
            std::cerr << "Socket error: " << e.what() << std::endl;
    }
}
```

### Fix 2: Use SO_REUSEADDR to avoid TIME_WAIT issues

```cpp
#include <sys/socket.h>
#include <netinet/in.h>

int create_server_socket(int port) {
    int fd = socket(AF_INET, SOCK_STREAM, 0);
    int opt = 1;
    setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);
    addr.sin_addr.s_addr = INADDR_ANY;

    bind(fd, reinterpret_cast<sockaddr*>(&addr), sizeof(addr));
    listen(fd, 128);
    return fd;
}
```

### Fix 3: Increase file descriptor limits

```cpp
#include <sys/resource.h>

void increase_fd_limit() {
    rlimit rl{};
    getrlimit(RLIMIT_NOFILE, &rl);
    rl.rlim_cur = rl.rlim_max;
    setrlimit(RLIMIT_NOFILE, &rl);
}
```

## Examples

```cpp
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <system_error>
#include <iostream>

int connect_to_server(const char* host, int port) {
    int fd = socket(AF_INET, SOCK_STREAM, 0);
    if (fd < 0) {
        throw std::system_error(errno, std::system_category(), "socket");
    }

    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);
    inet_pton(AF_INET, host, &addr.sin_addr);

    if (connect(fd, reinterpret_cast<sockaddr*>(&addr), sizeof(addr)) < 0) {
        int err = errno;
        close(fd);
        throw std::system_error(err, std::system_category(), "connect");
    }

    return fd;
}

int main() {
    try {
        int fd = connect_to_server("127.0.0.1", 8080);
        std::cout << "Connected!" << std::endl;
        close(fd);
    } catch (const std::system_error& e) {
        std::cerr << e.what() << " (code: " << e.code().value() << ")" << std::endl;
    }
    return 0;
}
```

## Related Errors

- [System Error]({{< relref "/languages/cpp/system-error" >}}) — system error
- [System Error Generic]({{< relref "/languages/cpp/system-error-generic" >}}) — generic system error
- [SystemError]({{< relref "/languages/cpp/systemerror" >}}) — system error
