---
title: "[Solution] C errno 46 ENOSTR — No stream head"
description: "Fix C errno 46 ENOSTR (No stream head) by ensuring file descriptor is associated with a STREAMS device, not a regular file."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno 46 ENOSTR — No stream head

No stream head occurs when a system call fails and sets `errno` to 46. This error indicates that the requested operation cannot be performed due to the specific condition described by ENOSTR.

## Common Causes

- Trying to perform STREAMS operations on a non-STREAMS file descriptor.
- Using ioctl() on a regular file or pipe.
- Attempting to push a STREAMS module onto a non-STREAMS device.
- Using I_FIND on a file descriptor that isn't a STREAM.

## How to Fix

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int fd = open("/tmp/test.txt", O_RDONLY);
    if (fd == -1) {
        perror("open");
        return 1;
    }
    int ret = ioctl(fd, I_FIND, "some_module");
    if (ret == -1 && errno == ENOSTR) {
        fprintf(stderr, "Not a STREAM: %s (errno %d)\n", strerror(errno), errno);
    }
    close(fd);
    return 0;
}
```

## Examples

```c
#include <sys/ioctl.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int fd = open("/dev/null", O_RDONLY);
    if (fd == -1) {
        perror("open");
        return 1;
    }
    if (isastream(fd) == 0) {
        printf("File descriptor %d is not a STREAM\n", fd);
    }
    close(fd);
    return 0;
}
```

## Related Errors

- [errno-13 EACCES]({{< relref "/languages/c/errno-13" >}}) — permission denied.
- [errno-46 ENOSTR]({{< relref "/languages/c/errno-46" >}}) — no stream head (self).
- [errno-38 ENOSYS]({{< relref "/languages/c/errno-38" >}}) — function not implemented.
