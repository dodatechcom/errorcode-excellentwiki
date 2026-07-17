---
title: "[Solution] C errno EAFNOSUPPORT — Address family not supported Fix"
description: "Fix C EAFNOSUPPORT (Address family not supported) by using supported address families and checking network configuration."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EAFNOSUPPORT — Address family not supported Fix

When `socket()`, `bind()`, or another networking function is used with an address family that is not supported by the kernel or the network stack, the call fails and sets `errno` to `EAFNOSUPPORT`. This error is similar to `EPFNOSUPPORT` but applies to the address family specifically.

## Common Causes

- Using `AF_INET6` on a system without IPv6 support enabled.
- The network stack does not support the requested address family.
- The address family is recognized but not configured on any network interface.
- Using a non-standard or deprecated address family (e.g., `AF_ASH`, `AF_ECONET`).

## How to Fix

Check available address families and use ones supported by the system.

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int families[] = {AF_INET, AF_INET6, AF_UNIX};
    for (int i = 0; i < 3; i++) {
        int sock = socket(families[i], SOCK_STREAM, 0);
        if (sock == -1) {
            if (errno == EAFNOSUPPORT) {
                fprintf(stderr, "Address family %d not supported\n", families[i]);
            }
        } else {
            printf("Address family %d is supported\n", families[i]);
            close(sock);
        }
    }
    return 0;
}
```

## Examples

Binding to an unsupported address family:

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct sockaddr_in6 addr = {0};
    addr.sin6_family = AF_INET6;
    addr.sin6_port = htons(8080);

    int sock = socket(AF_INET6, SOCK_STREAM, 0);
    if (sock == -1) {
        if (errno == EAFNOSUPPORT) {
            fprintf(stderr, "IPv6 not supported on this system\n");
        }
        return 1;
    }
    close(sock);
    return 0;
}
```

## Related Errors

- [errno-97 EAFNOSUPPORT]({{< relref "/languages/c/errno-eAFNOSUPPORT" >}}) — address family not supported (numeric).
- [errno-94 EPFNOSUPPORT]({{< relref "/languages/c/errno-ePFNOSUPPORT" >}}) — protocol family not supported.
- [errno-22 EINVAL](/languages/c/errno-eAFNOSUPPORT/) — invalid argument.
