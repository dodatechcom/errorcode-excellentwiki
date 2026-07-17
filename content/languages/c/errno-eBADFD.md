---
title: "[Solution] C errno EBADFD — File descriptor in bad state Fix"
description: "Fix C EBADFD (File descriptor in bad state) by checking descriptor validity and handling corrupted state."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EBADFD — File descriptor in bad state Fix

When a STREAMS ioctl operation is attempted on a file descriptor that is in an invalid or corrupted state, the call fails and sets `errno` to `EBADFD`. This indicates the file descriptor's internal state is inconsistent.

## Common Causes

- The file descriptor refers to a STREAMS device that has been disconnected or reset.
- A STREAMS module was improperly popped, leaving the stream in an inconsistent state.
- The file descriptor was closed or reused while a STREAMS operation was pending.
- Internal kernel STREAMS state corruption due to a race condition.

## How to Fix

Verify the file descriptor is valid before performing STREAMS operations. Reopen the device if the stream is corrupted.

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int fd = open("/dev/streams/device", O_RDWR);
    if (fd == -1) { perror("open"); return 1; }

    if (ioctl(fd, I_FIND, "module") == -1) {
        if (errno == EBADFD) {
            fprintf(stderr, "File descriptor in bad state — reopening\n");
            close(fd);
            fd = open("/dev/streams/device", O_RDWR);
            if (fd == -1) { perror("reopen"); return 1; }
        }
    }
    close(fd);
    return 0;
}
```

## Examples

Performing ioctl on a corrupted descriptor:

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    // Suppose fd was valid but stream state is corrupted
    if (ioctl(fd, I_PUSH, "badmodule") == -1) {
        if (errno == EBADFD) {
            fprintf(stderr, "File descriptor in bad state (errno %d)\n", errno);
        }
    }
    return 0;
}
```

## Related Errors

- [errno-77 EBADFD]({{< relref "/languages/c/errno-eBADFD" >}}) — file descriptor in bad state (numeric).
- [errno-9 EBADF](/languages/c/errno-eBADFD/) — bad file descriptor.
- [errno-22 EINVAL](/languages/c/errno-eBADFD/) — invalid argument.
