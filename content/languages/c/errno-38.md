---
title: "[Solution] C errno 38 ENOSYS — Function not implemented"
description: "Fix C errno 38 ENOSYS (Function not implemented) by checking kernel version, using alternative APIs, or enabling syscall support."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno 38 ENOSYS — Function not implemented

Function not implemented occurs when a system call fails and sets `errno` to 38. This error indicates that the requested operation cannot be performed due to the specific condition described by ENOSYS.

## Common Causes

- Calling a system call that is not supported by the kernel.
- Using features not compiled into the kernel.
- Attempting to use a syscall on an older kernel version.
- Trying to use a feature on a minimal or embedded system.

## How to Fix

```c
#include <sys/mman.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    void *ptr = mmap(NULL, 4096, PROT_READ, MAP_PRIVATE | MAP_ANONYMOUS | MAP_POPULATE, -1, 0);
    if (ptr == MAP_FAILED) {
        fprintf(stderr, "mmap failed: %s (errno %d)\n", strerror(errno), errno);
    }
    return 0;
}
```

## Examples

```c
#include <unistd.h>
#include <stdio.h>
#include <sys/syscall.h>

int main(void) {
    long ret = syscall(SYS_gettid);
    if (ret == -1 && errno == ENOSYS) {
        fprintf(stderr, "gettid syscall not implemented\n");
    }
    return 0;
}
```

## Related Errors

- [errno-13 EACCES]({{< relref "/languages/c/errno-13" >}}) — permission denied.
- [errno-38 ENOSYS]({{< relref "/languages/c/errno-38" >}}) — function not implemented (self).
- [errno-12 ENOMEM]({{< relref "/languages/c/errno-12" >}}) — cannot allocate memory.
