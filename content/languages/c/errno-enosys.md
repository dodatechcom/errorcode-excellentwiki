---
title: "[Solution] C errno ENOSYS — Function not implemented Fix"
description: "Fix C ENOSYS (Function not implemented) by checking kernel support, using alternative APIs, and verifying syscall availability."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enosys", "function-not-implemented", "syscall", "kernel-support"]
weight: 5
---

# [Solution] C errno ENOSYS — Function not implemented Fix

When a system call or library function is not implemented by the kernel or the platform, the call fails and sets `errno` to `ENOSYS`. This error typically occurs when using features not compiled into the kernel or calling system calls on an unsupported architecture.

## Common Causes

- The kernel was compiled without support for the requested system call.
- Calling a system call not available on the current architecture (e.g., 32-bit vs 64-bit).
- Using a feature that requires a newer kernel than the one running.
- The `seccomp` filter is blocking the system call, returning `ENOSYS`.

## How to Fix

Check kernel configuration and use alternative APIs. Use `#ifdef` guards for platform-specific code.

```c
#include <sys/mman.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    void *ptr = mmap(NULL, 4096, PROT_READ, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (ptr == MAP_FAILED) {
        if (errno == ENOSYS) {
            fprintf(stderr, "mmap not supported on this platform\n");
        } else {
            fprintf(stderr, "mmap failed: %s\n", strerror(errno));
        }
        return 1;
    }
    munmap(ptr, 4096);
    return 0;
}
```

## Examples

Calling a system call not implemented by the kernel:

```c
#include <linux/perf_event.h>
#include <sys/ioctl.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct perf_event_attr pe = {0};
    pe.type = PERF_TYPE_HARDWARE;
    pe.size = sizeof(pe);
    pe.config = PERF_COUNT_HW_INSTRUCTIONS;

    int fd = syscall(__NR_perf_event_open, &pe, 0, -1, -1, 0);
    if (fd == -1) {
        if (errno == ENOSYS) {
            fprintf(stderr, "perf_event_open not supported\n");
        } else {
            perror("perf_event_open");
        }
    }
    return 0;
}
```

## Related Errors

- [errno-38 ENOSYS](/languages/c/errno-enosys/) — function not implemented (numeric).
- [errno-22 EINVAL](/languages/c/errno-enosys/) — invalid argument.
- [errno-1 ENOEXEC](/languages/c/errno-enosys/) — exec format error.
