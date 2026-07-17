---
title: "[Solution] C errno 99 EADDRNOTAVAIL — Address Not Available Fix"
description: "Fix C errno 99 EADDRNOTAVAIL by checking IP binding, network interface status, port availability, and local address configuration."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 40
---

# [Solution] C errno 99 EADDRNOTAVAIL — Address Not Available Fix

When `bind()`, `connect()`, or `sendto()` fails with `errno` set to `EADDRNOTAVAIL` (99 on Linux), it means the requested IP address or port is not available on the local system. This happens when you try to bind to an IP that does not exist on any local network interface, or when the system has run out of available ephemeral ports.

## What You'll See

```c
int sockfd = socket(AF_INET, SOCK_STREAM, 0);
struct sockaddr_in addr = {
    .sin_family = AF_INET,
    .sin_port = htons(8080),
    .sin_addr.s_addr = inet_addr("192.168.1.100"),  // may not exist on this machine
};

if (bind(sockfd, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
    perror("bind");  // "bind: Cannot assign requested address"
    fprintf(stderr, "errno: %d\n", errno);  // errno: 99
}
```

## Common Causes

- Binding to an IP that is not assigned to any local network interface.
- The network interface is down or has been reconfigured.
- The requested port is already in use (though this usually gives `EADDRINUSE`).
- Running out of ephemeral ports (high port exhaustion under heavy connection load).
- Connecting to a remote address from a source IP that does not exist locally.

## Wrong: Hardcoding a specific IP for bind

```c
// WRONG — binds to a specific IP that may not exist
struct sockaddr_in addr;
addr.sin_family = AF_INET;
addr.sin_port = htons(8080);
addr.sin_addr.s_addr = inet_addr("192.168.1.50");  // may not be on this machine

if (bind(sockfd, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
    perror("bind");  // EADDRNOTAVAIL
}
```

## Correct: Bind to INADDR_ANY

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_port = htons(8080),
        .sin_addr.s_addr = htonl(INADDR_ANY),  // bind to all interfaces
    };

    if (bind(sockfd, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        perror("bind");
        close(sockfd);
        return 1;
    }

    printf("Bound to port 8080 on all interfaces\n");
    close(sockfd);
    return 0;
}
```

## Correct: Verify the local IP exists before binding

```c
#include <ifaddrs.h>
#include <arpa/inet.h>
#include <string.h>
#include <stdio.h>

int ip_exists_on_local(const char *target_ip) {
    struct ifaddrs *ifaddr, *ifa;

    if (getifaddrs(&ifaddr) == -1) return 0;

    for (ifa = ifaddr; ifa != NULL; ifa = ifa->ifa_next) {
        if (ifa->ifa_addr == NULL) continue;
        if (ifa->ifa_addr->sa_family != AF_INET) continue;

        struct sockaddr_in *sa = (struct sockaddr_in *)ifa->ifa_addr;
        char ip[INET_ADDRSTRLEN];
        inet_ntop(AF_INET, &sa->sin_addr, ip, sizeof(ip));

        if (strcmp(ip, target_ip) == 0) {
            freeifaddrs(ifaddr);
            return 1;
        }
    }

    freeifaddrs(ifaddr);
    return 0;
}

// Usage
int main(void) {
    const char *bind_ip = "192.168.1.50";

    if (!ip_exists_on_local(bind_ip)) {
        fprintf(stderr, "IP %s does not exist on any local interface\n", bind_ip);
        return 1;
    }

    // Safe to bind
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_port = htons(8080),
    };
    inet_pton(AF_INET, bind_ip, &addr.sin_addr);

    if (bind(sockfd, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        perror("bind");
        return 1;
    }

    close(sockfd);
    return 0;
}
```

## Fix: Reduce Ephemeral Port Exhaustion

```c
#include <sys/socket.h>
#include <netinet/in.h>

// Enable address reuse
int sockfd = socket(AF_INET, SOCK_STREAM, 0);
int optval = 1;
setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &optval, sizeof(optval));
setsockopt(sockfd, SOL_SOCKET, SO_REUSEPORT, &optval, sizeof(optval));

// Check current ephemeral port range
// Read from: /proc/sys/net/ipv4/ip_local_port_range
// Widen it if needed:
// echo "1024 65535" > /proc/sys/net/ipv4/ip_local_port_range
```

## Debugging EADDRNOTAVAIL

```bash
# List all local IP addresses
ip addr show

# Check if the network interface is up
ip link show

# Check ephemeral port range
cat /proc/sys/net/ipv4/ip_local_port_range

# Count connections in TIME_WAIT state (port exhaustion)
ss -s

# Check listening sockets
ss -tlnp
```

## Summary

| Fix | When to Use |
|---|---|
| Bind to `INADDR_ANY` | When you don't need a specific interface |
| Verify IP with `getifaddrs()` | When binding to a specific IP |
| Set `SO_REUSEADDR` | When restarting a server quickly after crash |
| Widen ephemeral port range | When experiencing port exhaustion under load |
| Check interface status | When the network was reconfigured |

## Related Errors

- [errno-110 ETIMEDOUT](errno-110) — connection timed out.
- [errno-115 EINPROGRESS](errno-115) — operation in progress.
- [errno-32 EPIPE](errno-32) — broken pipe.
