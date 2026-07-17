---
title: "[Solution] C errno 45 EBADMSG — Not a STREAMS message"
description: "Fix C errno 45 EBADMSG (Not a STREAMS message) by validating message format, checking STREAMS alignment, and using proper message types."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno 45 EBADMSG — Not a STREAMS message

Not a STREAMS message occurs when a system call fails and sets `errno` to 45. This error indicates that the requested operation cannot be performed due to the specific condition described by EBADMSG.

## Common Causes

- Received a corrupted or invalid STREAMS message.
- Message received at STREAM head is malformed.
- Using ioctl() with invalid STREAMS command.
- STREAMS module sent an error message.

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
    int ret = ioctl(fd, I_FIND, "nonexistent_module");
    if (ret == -1 && errno == EBADMSG) {
        fprintf(stderr, "Bad STREAMS message\n");
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
    FILE *fp = fopen("/dev/null", "r");
    if (fp == NULL) {
        perror("fopen");
        return 1;
    }
    char buf[100];
    size_t n = fread(buf, 1, sizeof(buf), fp);
    if (n == 0 && ferror(fp)) {
        fprintf(stderr, "Read error\n");
    }
    fclose(fp);
    return 0;
}
```

## Related Errors

- [errno-28 ENOSPC]({{< relref "/languages/c/errno-28" >}}) — no space left on device.
- [errno-45 EBADMSG]({{< relref "/languages/c/errno-45" >}}) — not a STREAMS message (self).
- [errno-13 EACCES]({{< relref "/languages/c/errno-13" >}}) — permission denied.
