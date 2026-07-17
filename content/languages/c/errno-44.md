---
title: "[Solution] C errno 44 ERMSR — No STREAMS resources"
description: "Fix C errno 44 ERMSR (No STREAMS resources) by reducing STREAMS usage, increasing system limits, or waiting for resources to become available."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno 44 ERMSR — No STREAMS resources

No STREAMS resources occurs when a system call fails and sets `errno` to 44. This error indicates that the requested operation cannot be performed due to the specific condition described by ERMSR.

## Common Causes

- System has insufficient STREAMS memory resources.
- Too many STREAMS queues or heads allocated.
- Attempting to open a STREAMS device when resources are exhausted.
- STREAMS modules not being properly cleaned up.

## How to Fix

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int fd = open("/dev/streams/pipe", O_RDONLY);
    if (fd == -1) {
        fprintf(stderr, "open failed: %s (errno %d)\n", strerror(errno), errno);
        return 1;
    }
    close(fd);
    return 0;
}
```

## Examples

```c
#include <stdio.h>
#include <errno.h>

int main(void) {
    FILE *fp = popen("echo test", "r");
    if (fp == NULL) {
        perror("popen");
        return 1;
    }
    pclose(fp);
    return 0;
}
```

## Related Errors

- [errno-48 ENOSR]({{< relref "/languages/c/errno-48" >}}) — no STREAMS buffers.
- [errno-44 ERMSR]({{< relref "/languages/c/errno-44" >}}) — no STREAMS resources (self).
- [errno-12 ENOMEM]({{< relref "/languages/c/errno-12" >}}) — cannot allocate memory.
