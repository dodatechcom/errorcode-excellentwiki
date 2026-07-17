---
title: "[Solution] C errno ETOOMANYREFS — Too many references Fix"
description: "Fix C ETOOMANYREFS (Too many references) by reducing file descriptor usage and handling reference limits."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ETOOMANYREFS — Too many references Fix

When a system call encounters too many internal references (such as file descriptor references or connection states), the call fails and sets `errno` to `ETOOMANYREFS`. This error typically occurs when the kernel's reference count for file descriptors or connections exceeds internal limits.

## Common Causes

- Too many file descriptors are open in the system, preventing new socket connections.
- The `dup2()` or `sendmsg()` with `SCM_RIGHTS` has created excessive fd references.
- A process is leaking file descriptors through repeated `fork()` without closing extras.
- The kernel's internal file structure reference count is exhausted.

## How to Fix

Close unused file descriptors and reduce the number of simultaneous connections. Check system-wide fd limits.

```c
#include <sys/resource.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct rlimit rl;
    getrlimit(RLIMIT_NOFILE, &rl);
    printf("Current fd limit: %lu\n", rl.rlim_cur);

    // Increase if possible
    rl.rlim_cur = 65536;
    if (setrlimit(RLIMIT_NOFILE, &rl) == -1) {
        if (errno == ETOOMANYREFS) {
            fprintf(stderr, "Cannot increase fd limit — too many references\n");
        } else {
            perror("setrlimit");
        }
    }
    return 0;
}
```

## Examples

Exhausting references through fd passing:

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sv[2];
    socketpair(AF_UNIX, SOCK_STREAM, 0, sv);

    // Simulated: passing too many fds via SCM_RIGHTS
    struct msghdr msg = {0};
    // ... fill msg with excessive fd references ...

    if (sendmsg(sv[0], &msg, 0) == -1) {
        if (errno == ETOOMANYREFS) {
            fprintf(stderr, "Too many references (errno %d)\n", errno);
        }
    }
    close(sv[0]);
    close(sv[1]);
    return 0;
}
```

## Related Errors

- [errno-24 EMFILE]({{< relref "/languages/c/errno-emfile" >}}) — too many open files (per-process).
- [errno-23 ENFILE]({{< relref "/languages/c/errno-enfile" >}}) — too many open files in system.
- [errno-24 EMFILE]({{< relref "/languages/c/errno-emfile" >}}) — too many open files.
