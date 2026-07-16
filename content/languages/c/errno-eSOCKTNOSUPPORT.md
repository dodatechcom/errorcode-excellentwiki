---
title: "[Solution] C errno ESOCKTNOSUPPORT — Socket type not supported Fix"
description: "Fix C ESOCKTNOSUPPORT (Socket type not supported) by checking kernel socket support and using supported socket types."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["esocktnosupport", "socket-type-not-supported", "socket", "af-inet"]
weight: 5
---

# [Solution] C errno ESOCKTNOSUPPORT — Socket type not supported Fix

When `socket()` is called with a socket type that is not supported by the kernel or the specified protocol family, the call fails and sets `errno` to `ESOCKTNOSUPPORT`. This error indicates the requested socket type combination is not available.

## Common Causes

- The requested socket type (e.g., `SOCK_RAW`) is not supported for the given protocol family.
- The kernel was compiled without support for the requested socket type.
- `SOCK_DGRAM` or `SOCK_RAW` used with an unsupported address family.
- The `seccomp` filter blocks the `socket()` syscall for the requested type.

## How to Fix

Use supported socket types. Check kernel configuration for socket support.

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
    if (sock == -1) {
        if (errno == ESOCKTNOSUPPORT) {
            fprintf(stderr, "SOCK_RAW not supported for AF_INET\n");
        } else {
            fprintf(stderr, "socket failed: %s\n", strerror(errno));
        }
        return 1;
    }
    close(sock);
    return 0;
}
```

## Examples

Using an unsupported socket type:

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    // SOCK_SEQPACKET may not be supported for all families
    int sock = socket(AF_INET, SOCK_SEQPACKET, 0);
    if (sock == -1) {
        if (errno == ESOCKTNOSUPPORT) {
            fprintf(stderr, "Socket type not supported (errno %d)\n", errno);
        }
    }
    return 0;
}
```

## Related Errors

- [errno-93 ESOCKTNOSUPPORT]({{< relref "/languages/c/errno-eSOCKTNOSUPPORT" >}}) — socket type not supported (numeric).
- [errno-94 EPFNOSUPPORT]({{< relref "/languages/c/errno-ePFNOSUPPORT" >}}) — protocol family not supported.
- [errno-97 EAFNOSUPPORT]({{< relref "/languages/c/errno-eAFNOSUPPORT" >}}) — address family not supported.
