---
title: "[Solution] C errno 13 EACCES — Permission denied"
description: "Fix C errno 13 EACCES (Permission denied) by checking file permissions, running as appropriate user, and setting correct umask."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno 13 EACCES — Permission denied

Permission denied occurs when a system call fails and sets `errno` to 13. This error indicates that the requested operation cannot be performed due to the specific condition described by EACCES.

## Common Causes

- Attempting to open a file without proper read/write permissions.
- Running the program as a user who does not own the file and lacks group permissions.
- Trying to execute a file without execute permission.
- Attempting to write to a read-only file system or directory.

## How to Fix

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int fd = open("/etc/shadow", O_RDONLY);
    if (fd == -1) {
        fprintf(stderr, "open failed: %s (errno %d)\n", strerror(errno), errno);
        return 1;
    }
    close(fd);
    return 0;
}
```

## Examples

```c
#include <stdio.h>
#include <sys/stat.h>
#include <errno.h>

int main(void) {
    struct stat st;
    if (stat("/etc/shadow", &st) == -1) {
        perror("stat");
        return 1;
    }
    printf("File mode: %o\n", st.st_mode & 0777);
    return 0;
}
```

## Related Errors

- [errno-17 EEXIST]({{< relref "/languages/c/errno-17" >}}) — file exists.
- [errno-13 EACCES]({{< relref "/languages/c/errno-13" >}}) — permission denied (self).
- [errno-30 EROFS]({{< relref "/languages/c/errno-30" >}}) — read-only file system.
