---
title: "[Solution] C errno ENOSR — No STREAMS buffers available Fix"
description: "Fix C ENOSR (No STREAMS buffers available) by managing STREAMS buffer allocation and increasing pool sizes."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enosr", "no-streams-buffers", "streams", "data-buffers", "putmsg"]
weight: 5
---

# [Solution] C errno ENOSR — No STREAMS buffers available Fix

When `putmsg()` or `putpmsg()` is called and the system cannot allocate a STREAMS data buffer because the buffer pool is exhausted, the call fails and sets `errno` to `ENOSR`. This error indicates the STREAMS data buffer pool is empty.

## Common Causes

- The STREAMS data buffer pool has been exhausted by high-volume I/O.
- STREAMS buffers are leaked by modules that fail to free them.
- The system-wide STREAMS buffer limit is too low for the workload.
- Multiple STREAMS-based connections are consuming all available buffers.

## How to Fix

Reduce STREAMS buffer usage, increase buffer pool limits, or wait and retry.

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    struct strbuf data;
    char buf[1024];
    data.buf = buf;
    data.len = sizeof(buf);

    int ret = putmsg(fd, NULL, &data, 0);
    if (ret == -1) {
        if (errno == ENOSR) {
            fprintf(stderr, "No STREAMS buffers available — retrying\n");
            // Wait and retry
        } else {
            fprintf(stderr, "putmsg failed: %s\n", strerror(errno));
        }
        return 1;
    }
    return 0;
}
```

## Examples

 STREAMS buffer exhaustion:

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct strbuf data;
    char buf[4096];
    data.buf = buf;
    data.len = sizeof(buf);

    for (int i = 0; i < 10000; i++) {
        if (putmsg(fd, NULL, &data, 0) == -1) {
            if (errno == ENOSR) {
                fprintf(stderr, "STREAMS buffer pool exhausted at iteration %d\n", i);
                break;
            }
        }
    }
    return 0;
}
```

## Related Errors

- [errno-46 ENOSR]({{< relref "/languages/c/errno-enosr" >}}) — no STREAMS buffers available (numeric).
- [errno-44 ERMSR]({{< relref "/languages/c/errno-ermsr" >}}) — no STREAMS resources.
- [errno-11 EAGAIN](/languages/c/errno-enosr/) — resource unavailable, try again.
