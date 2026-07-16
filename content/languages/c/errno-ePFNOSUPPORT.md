---
title: "[Solution] C errno EPFNOSUPPORT — Protocol family not supported Fix"
description: "Fix C EPFNOSUPPORT (Protocol family not supported) by using supported protocol families and checking kernel configuration."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["epfnosupport", "protocol-family-not-supported", "socket", "af-inet", "af-local"]
weight: 5
---

# [Solution] C errno EPFNOSUPPORT — Protocol family not supported Fix

When `socket()` is called with a protocol family (address family) that is not supported by the kernel, the call fails and sets `errno` to `EPFNOSUPPORT`. This error indicates the entire protocol family is not compiled into the kernel.

## Common Causes

- The kernel was compiled without support for the requested protocol family (e.g., `AF_IPX`).
- Using a deprecated or non-standard protocol family.
- The protocol family module is not loaded.
- Attempting to use `AF_INET6` on a system without IPv6 support.

## How to Fix

Use supported protocol families. Check available families with `socket()` probing.

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    // Try to create an IPv6 socket
    int sock = socket(AF_INET6, SOCK_STREAM, 0);
    if (sock == -1) {
        if (errno == EPFNOSUPPORT) {
            fprintf(stderr, "IPv6 (AF_INET6) not supported\n");
        } else {
            perror("socket");
        }
        return 1;
    }
    close(sock);
    return 0;
}
```

## Examples

Using a deprecated protocol family:

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    // AF_IPX is not supported on most modern Linux systems
    int sock = socket(AF_IPX, SOCK_STREAM, 0);
    if (sock == -1) {
        if (errno == EPFNOSUPPORT) {
            fprintf(stderr, "Protocol family AF_IPX not supported (errno %d)\n", errno);
        }
    }
    return 0;
}
```

## Related Errors

- [errno-94 EPFNOSUPPORT]({{< relref "/languages/c/errno-ePFNOSUPPORT" >}}) — protocol family not supported (numeric).
- [errno-97 EAFNOSUPPORT]({{< relref "/languages/c/errno-eAFNOSUPPORT" >}}) — address family not supported.
- [errno-93 ESOCKTNOSUPPORT]({{< relref "/languages/c/errno-eSOCKTNOSUPPORT" >}}) — socket type not supported.
