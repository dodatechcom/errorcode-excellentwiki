---
title: "[Solution] C errno ENOSR — No STREAMS resources (alternate) Fix"
description: "Fix C ENOSR (No STREAMS resources) by managing STREAMS resource pools and handling allocation failures."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enosr", "no-streams-resources", "streams", "resource-exhaustion"]
weight: 5
---

# [Solution] C errno ENOSR — No STREAMS resources (alternate) Fix

This is an alternate variant of `ENOSR` indicating that STREAMS resources (message blocks, not data buffers) are exhausted. When `putmsg()` or other STREAMS operations require a message block and none are available, `errno` is set to `ENOSR`.

## Common Causes

- The STREAMS message block pool is exhausted.
- Multiple STREAMS connections are consuming all available message blocks.
- STREAMS modules are not properly releasing message blocks.
- System-wide STREAMS resource limits are too low.

## How to Fix

Reduce STREAMS usage, increase resource limits, or implement backpressure mechanisms.

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>

int safe_putmsg(int fd, struct strbuf *ctl, struct strbuf *data, int flags) {
    int ret = putmsg(fd, ctl, data, flags);
    if (ret == -1 && errno == ENOSR) {
        fprintf(stderr, "STREAMS resources exhausted — applying backpressure\n");
        // Implement backpressure: sleep and retry
        usleep(10000);
        ret = putmsg(fd, ctl, data, flags);
    }
    return ret;
}

int main(void) {
    struct strbuf data;
    char buf[] = "hello";
    data.buf = buf;
    data.len = 5;

    if (safe_putmsg(stream_fd, NULL, &data, 0) == -1) {
        fprintf(stderr, "putmsg failed: ENOSR\n");
        return 1;
    }
    return 0;
}
```

## Examples

 STREAMS resource exhaustion under load:

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct strbuf data;
    char buf[512];
    data.buf = buf;

    int failures = 0;
    for (int i = 0; i < 1000; i++) {
        data.len = sprintf(buf, "Message %d", i);
        if (putmsg(stream_fd, NULL, &data, 0) == -1) {
            if (errno == ENOSR) {
                failures++;
                if (failures > 10) {
                    fprintf(stderr, "Too many STREAMS resource failures\n");
                    break;
                }
            }
        }
    }
    return 0;
}
```

## Related Errors

- [errno-46 ENOSR]({{< relref "/languages/c/errno-enosr" >}}) — no STREAMS resources (numeric).
- [errno-44 ERMSR]({{< relref "/languages/c/errno-ermsr" >}}) — no STREAMS resources (numeric alt).
- [errno-11 EAGAIN](/languages/c/errno-enosr-2/) — resource unavailable, try again.
