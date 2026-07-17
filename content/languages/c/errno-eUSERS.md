---
title: "[Solution] C errno EUSERS — Too many users Fix"
description: "Fix C EUSERS (Too many users) by reducing concurrent sessions, increasing limits, and managing user quotas."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EUSERS — Too many users Fix

When the system has reached the maximum number of concurrent user sessions or user records, a new login, `setuid()`, or user-related operation fails and sets `errno` to `EUSERS`. This error indicates the per-system user limit has been exceeded.

## Common Causes

- The system has reached the maximum number of concurrent logged-in users.
- Too many user records are loaded in the kernel's utmp/wtmp accounting.
- The system's `ULIMIT` or `NPROC` per-user limit is reached.
- Resource accounting structures are full due to user session accumulation.

## How to Fix

Increase system user limits and clean up stale sessions.

```bash
# Check current user limits
cat /proc/sys/kernel/threads-max
ulimit -u

# Increase the limit
sysctl -w kernel.threads-max=16384
```

```c
#include <sys/resource.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct rlimit rl;
    if (getrlimit(RLIMIT_NPROC, &rl) == -1) {
        perror("getrlimit");
        return 1;
    }
    printf("Current NPROC limit: %lu\n", rl.rlim_cur);
    printf("Max NPROC: %lu\n", rl.rlim_max);

    // Attempt to increase
    rl.rlim_cur = 8192;
    if (setrlimit(RLIMIT_NPROC, &rl) == -1) {
        if (errno == EUSERS) {
            fprintf(stderr, "Too many users on system\n");
        } else {
            perror("setrlimit");
        }
    }
    return 0;
}
```

## Examples

Checking for the EUSERS condition:

```c
#include <utmpx.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    setutxent();
    struct utmpx *ut;
    int count = 0;
    while ((ut = getutxent()) != NULL) {
        if (ut->ut_type == USER_PROCESS) count++;
    }
    endutxent();
    printf("Active user sessions: %d\n", count);
    return 0;
}
```

## Related Errors

- [errno-87 EUSERS]({{< relref "/languages/c/errno-eUSERS" >}}) — too many users (numeric).
- [errno-11 EAGAIN](/languages/c/errno-eUSERS/) — resource unavailable, try again.
- [errno-24 EMFILE]({{< relref "/languages/c/errno-emfile" >}}) — too many open files.
