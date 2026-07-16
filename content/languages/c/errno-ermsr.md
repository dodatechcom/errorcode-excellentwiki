---
title: "[Solution] C errno ERMSR — No STREAMS resources Fix"
description: "Fix C ERMSR (No STREAMS resources) by managing STREAMS resource allocation and checking system limits."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["ermsr", "no-streams-resources", "streams", "putmsg", "getmsg"]
weight: 5
---

# [Solution] C errno ERMSR — No STREAMS resources Fix

When a STREAMS-related operation fails because the system has run out of STREAMS resources (message blocks, data buffers, or queue space), the call sets `errno` to `ERMSR`. STREAMS is a legacy IPC mechanism primarily found in Unix System V-derived systems.

## Common Causes

- The system has exhausted its STREAMS message block or data buffer pools.
- High-volume STREAMS I/O has depleted available resources.
- The STREAMS resource limits (configured via `strmod` or kernel parameters) are too low.
- Resource leak in STREAMS-based modules.

## How to Fix

Monitor STREAMS resource usage and increase limits if necessary. On modern Linux, STREAMS support is limited and rarely used.

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int fd = open("/dev/streams/pipe", O_RDWR);
    if (fd == -1) {
        if (errno == ERMSR) {
            fprintf(stderr, "No STREAMS resources available\n");
        } else {
            fprintf(stderr, "open failed: %s\n", strerror(errno));
        }
        return 1;
    }
    close(fd);
    return 0;
}
```

## Examples

STREAMS operations failing due to resource exhaustion:

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    // Attempting a STREAMS operation when resources are exhausted
    struct strbuf ctl, data;
    char cbuf[128], dbuf[1024];
    ctl.buf = cbuf; ctl.maxlen = sizeof(cbuf);
    data.buf = dbuf; data.maxlen = sizeof(dbuf);

    int ret = getmsg(fd, &ctl, &data, NULL);
    if (ret == -1 && errno == ERMSR) {
        fprintf(stderr, " STREAMS resources exhausted\n");
    }
    return 0;
}
```

## Related Errors

- [errno-44 ERMSR](/languages/c/errno-ermsr/) — no STREAMS resources (numeric).
- [errno-46 ENOSR]({{< relref "/languages/c/errno-enosr" >}}) — no STREAMS buffers available.
- [errno-11 EAGAIN](/languages/c/errno-ermsr/) — resource unavailable, try again.
