---
title: "[Solution] C errno EOPNOTSUPP — Operation not supported Fix"
description: "Fix C EOPNOTSUPP (Operation not supported) by checking feature availability and using supported alternatives."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["eopnotsupp", "operation-not-supported", "socket-options", "feature-availability"]
weight: 5
---

# [Solution] C errno EOPNOTSUPP — Operation not supported Fix

When a system call attempts an operation that is not supported for the given object type or protocol, the call fails and sets `errno` to `EOPNOTSUPP`. This error is common with socket options, filesystem operations, and ioctl commands.

## Common Causes

- The socket option is not supported for the socket type (e.g., `SO_KEEPALIVE` on UDP).
- The `ioctl()` command is not supported by the device driver.
- `sendmsg()` with `MSG_OOB` on a socket that does not support out-of-band data.
- The filesystem does not support the requested operation (e.g., `fallocate()` on NFS).

## How to Fix

Check feature support before using it. Use `getsockopt()` to verify options or probe with `ioctl()`.

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_DGRAM, 0);

    int val = 1;
    if (setsockopt(sock, SOL_SOCKET, SO_KEEPALIVE, &val, sizeof(val)) == -1) {
        if (errno == EOPNOTSUPP) {
            fprintf(stderr, "SO_KEEPALIVE not supported on UDP sockets\n");
        } else {
            perror("setsockopt");
        }
    }
    close(sock);
    return 0;
}
```

## Examples

Unsupported ioctl on a device:

```c
#include <sys/ioctl.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int fd = open("/dev/some_device", O_RDWR);
    if (fd == -1) { perror("open"); return 1; }

    if (ioctl(fd, SOME_IOCTL_CMD, NULL) == -1) {
        if (errno == EOPNOTSUPP) {
            fprintf(stderr, "ioctl command not supported by device\n");
        } else {
            perror("ioctl");
        }
    }
    close(fd);
    return 0;
}
```

## Related Errors

- [errno-95 EOPNOTSUPP]({{< relref "/languages/c/errno-eOPNOTSUPP" >}}) — operation not supported (numeric).
- [errno-22 EINVAL](/languages/c/errno-eOPNOTSUPP/) — invalid argument.
- [errno-25 ENOTTY](/languages/c/errno-eOPNOTSUPP/) — inappropriate ioctl for device.
