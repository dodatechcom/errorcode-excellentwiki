---
title: "[Solution] C errno ENODATA — No data available Fix"
description: "Fix C ENODATA (No data available) by handling empty STREAMS read operations and checking data availability."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enodata", "no-data-available", "streams", "getmsg", "ioctl"]
weight: 5
---

# [Solution] C errno ENODATA — No data available Fix

When `getmsg()` or a STREAMS read operation is called but no data (neither data messages nor expedited data) is available on the stream, the call sets `errno` to `ENODATA`. This error indicates the STREAMS read queue is empty.

## Common Causes

- Calling `getmsg()` when no messages are available on the stream.
- The STREAMS module has not yet delivered any data.
- The read queue was drained by a previous read operation.
- The peer process has not yet sent any data on the STREAMS pipe.

## How to Fix

Check data availability using `poll()` or `ioctl(I_RXSQ_LEN)` before reading. Use blocking mode to wait for data.

```c
#include <stropts.h>
#include <poll.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct pollfd pfd;
    pfd.fd = stream_fd;
    pfd.events = POLLIN;

    int ret = poll(&pfd, 1, 5000);
    if (ret > 0 && (pfd.revents & POLLIN)) {
        // Data is available — safe to call getmsg()
        struct strbuf data;
        char buf[1024];
        data.buf = buf;
        data.maxlen = sizeof(buf);
        getmsg(stream_fd, NULL, &data, NULL);
    } else if (ret == 0) {
        fprintf(stderr, "No data available (timeout)\n");
    }
    return 0;
}
```

## Examples

Reading from a stream with no data:

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct strbuf data;
    char buf[256];
    data.buf = buf;
    data.maxlen = sizeof(buf);

    if (getmsg(stream_fd, NULL, &data, NULL) == -1) {
        if (errno == ENODATA) {
            fprintf(stderr, "No data available on stream (errno %d)\n", errno);
        }
    }
    return 0;
}
```

## Related Errors

- [errno-61 ENODATA](/languages/c/errno-enodata/) — no data available (numeric).
- [errno-11 EAGAIN](/languages/c/errno-enodata/) — resource unavailable, try again.
- [errno-11 EWOULDBLOCK](/languages/c/errno-enodata/) — operation would block.
