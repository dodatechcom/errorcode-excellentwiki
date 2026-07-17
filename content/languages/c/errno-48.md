---
title: "[Solution] C errno 48 ENOSR — No STREAMS buffers"
description: "Fix C errno 48 ENOSR (No STREAMS buffers) by reducing STREAMS memory usage, increasing system limits, or using flow control."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno 48 ENOSR — No STREAMS buffers

No STREAMS buffers occurs when a system call fails and sets `errno` to 48. This error indicates that the requested operation cannot be performed due to the specific condition described by ENOSR.

## Common Causes

- Insufficient STREAMS memory buffers for message allocation.
- Too many STREAMS messages queued.
- STREAMS memory exhausted due to high throughput.
- Flow control preventing buffer allocation.

## How to Fix

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int fd = open("/dev/streams/pipe", O_RDONLY);
    if (fd == -1) {
        perror("open");
        return 1;
    }
    char buf[1024];
    ssize_t n = read(fd, buf, sizeof(buf));
    if (n == -1 && errno == ENOSR) {
        fprintf(stderr, "No STREAMS buffers available\n");
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
    FILE *fp = popen("long_running_command", "r");
    if (fp == NULL) {
        perror("popen");
        return 1;
    }
    char buf[256];
    while (fgets(buf, sizeof(buf), fp) != NULL) {
        printf("%s", buf);
    }
    pclose(fp);
    return 0;
}
```

## Related Errors

- [errno-12 ENOMEM]({{< relref "/languages/c/errno-12" >}}) — cannot allocate memory.
- [errno-48 ENOSR]({{< relref "/languages/c/errno-48" >}}) — no STREAMS buffers (self).
- [errno-11 EAGAIN]({{< relref "/languages/c/errno-11" >}}) — resource unavailable.
