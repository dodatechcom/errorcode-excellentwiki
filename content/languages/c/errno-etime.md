---
title: "[Solution] C errno ETIME — Stream ioctl timeout Fix"
description: "Fix C ETIME (Stream ioctl timeout) by adjusting timeout values and handling STREAMS ioctl timing."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["etime", "stream-ioctl-timeout", "streams", "timeout", "ioctl"]
weight: 5
---

# [Solution] C errno ETIME — Stream ioctl timeout Fix

When a timed STREAMS ioctl operation (such as `I_SETSIG` with a timeout or a polling operation) expires before the requested condition is met, the call sets `errno` to `ETIME`. This error indicates a timeout waiting for a STREAMS event.

## Common Causes

- The timeout for a STREAMS ioctl operation has expired.
- A polling operation on the stream head did not complete within the specified time.
- The STREAMS module did not respond within the expected time frame.
- Network STREAMS experienced delays exceeding the configured timeout.

## How to Fix

Increase timeout values or implement retry logic. On modern Linux, STREAMS support is limited.

```c
#include <stropts.h>
#include <poll.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    struct pollfd pfd;
    pfd.fd = stream_fd;
    pfd.events = POLLIN;

    int ret = poll(&pfd, 1, 5000);  // 5 second timeout
    if (ret == -1) {
        if (errno == ETIME) {
            fprintf(stderr, "STREAMS ioctl timeout\n");
        } else {
            fprintf(stderr, "poll failed: %s\n", strerror(errno));
        }
        return 1;
    }
    if (ret == 0) {
        fprintf(stderr, "Timeout expired — no data\n");
    }
    return 0;
}
```

## Examples

Timed STREAMS operation:

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    // Attempting a timed STREAMS ioctl
    int ret = ioctl(stream_fd, I_SETSIG, S_INPUT);
    if (ret == -1) {
        if (errno == ETIME) {
            fprintf(stderr, "STREAMS ioctl timed out (errno %d)\n", errno);
        } else {
            perror("ioctl");
        }
    }
    return 0;
}
```

## Related Errors

- [errno-62 ETIME](/languages/c/errno-etime/) — stream ioctl timeout (numeric).
- [errno-110 ETIMEDOUT]({{< relref "/languages/c/errno-eTIMEDOUT" >}}) — connection timed out.
- [errno-11 EAGAIN](/languages/c/errno-etime/) — resource unavailable, try again.
