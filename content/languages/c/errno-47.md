---
title: "[Solution] C errno 47 ETIME — Stream ioctl timeout"
description: "Fix C errno 47 ETIME (Stream ioctl timeout) by adjusting timeout values, using non-blocking operations, or checking STREAMS status."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["etime", "errno-47", "stream", "ioctl", "timeout"]
weight: 5
---

# [Solution] C errno 47 ETIME — Stream ioctl timeout

Stream ioctl timeout occurs when a system call fails and sets `errno` to 47. This error indicates that the requested operation cannot be performed due to the specific condition described by ETIME.

## Common Causes

- STREAMS ioctl operation timed out waiting for acknowledgment.
- Downstream module didn't respond within timeout period.
- Using I_STR ioctl with insufficient timeout.
- Network STREAMS experiencing delays.

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
    struct strioctl ctl;
    ctl.ic_cmd = 0;
    ctl.ic_timout = 5;  // 5 second timeout
    ctl.ic_len = 0;
    ctl.ic_dp = NULL;
    int ret = ioctl(fd, I_STR, &ctl);
    if (ret == -1 && errno == ETIME) {
        fprintf(stderr, "STREAMS ioctl timed out\n");
    }
    close(fd);
    return 0;
}
```

## Examples

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int fd = open("/dev/streams/pipe", O_RDONLY);
    if (fd == -1) {
        perror("open");
        return 1;
    }
    // Set a longer timeout
    int timeout = 30;  // seconds
    if (ioctl(fd, I_SETSIG, 0) == -1) {
        perror("ioctl");
    }
    close(fd);
    return 0;
}
```

## Related Errors

- [errno-110 ETIMEDOUT]({{< relref "/languages/c/errno-110" >}}) — connection timed out.
- [errno-47 ETIME]({{< relref "/languages/c/errno-47" >}}) — stream ioctl timeout (self).
- [EIO]({{< relref "/languages/c/errno-99" >}}) — input/output error.
