---
title: "[Solution] C errno ENOMEM — Cannot allocate memory Fix"
description: "Fix C ENOMEM (Cannot allocate memory) by checking malloc return, adjusting overcommit settings, and reducing memory usage."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ENOMEM — Cannot allocate memory Fix

When `malloc()`, `calloc()`, `realloc()`, or `mmap()` fails because the system cannot allocate the requested memory, the function returns `NULL` (or `MAP_FAILED`) and sets `errno` to `ENOMEM`. This error indicates that the kernel denied the memory allocation due to insufficient physical memory, exceeded overcommit accounting, or process limits.

## Common Causes

- The system is out of physical memory and swap space.
- The process has exceeded its virtual memory limit (`ulimit -v`).
- Overcommit accounting is in strict mode (`vm.overcommit_memory=2`) and `Committed_AS` has reached `CommitLimit`.
- The allocation request is too large for the available contiguous virtual address space.

## How to Fix

Always check the return value of memory allocation functions. If `ENOMEM` occurs, consider reducing the allocation size, freeing unused memory, or adjusting system limits.

```c
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int *arr = malloc(1000000 * sizeof(int));
    if (arr == NULL) {
        fprintf(stderr, "malloc failed: %s (errno %d)\n", strerror(errno), errno);
        return 1;
    }
    // Use the allocated memory...
    free(arr);
    return 0;
}
```

## Examples

The error appears when the kernel refuses a memory request:

```c
#include <sys/mman.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    void *ptr = mmap(NULL, 1ULL << 32, PROT_READ, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (ptr == MAP_FAILED) {
        perror("mmap");  // "mmap: Cannot allocate memory"
        fprintf(stderr, "errno: %d\n", errno);  // 12
    }
    return 0;
}
```

Another common scenario is `fork()` failing due to commit limits:

```c
#include <unistd.h>
#include <stdio.h>

int main(void) {
    pid_t pid = fork();
    if (pid == -1) {
        perror("fork");  // "fork: Cannot allocate memory"
    }
    return 0;
}
```

## Related Errors

- [errno-11 EAGAIN](/languages/c/errno-enomem/) — resource unavailable, try again.
- [errno-28 ENOSPC](/languages/c/errno-enomem/) — no space left on device.
- [errno-12 ENOMEM](/languages/c/errno-enomem/) — cannot allocate memory (self).
