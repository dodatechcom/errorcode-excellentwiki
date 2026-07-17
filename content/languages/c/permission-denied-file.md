---
title: "[Solution] C Permission denied: EACCES"
description: "Fix C permission denied (EACCES). Set correct file permissions for I/O operations."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["eacces", "permission-denied", "file-permissions", "chmod", "errno"]
weight: 5
---

# Permission denied: EACCES

EACCES occurs when you try to access a file without the necessary permissions. The file may not allow read, write, or execute access for your user.

## Common Causes

```c
// Cause 1: No read permission
int fd = open("/etc/shadow", O_RDONLY); // EACCES

// Cause 2: No write permission
int fd = open("/root/file.txt", O_WRONLY); // EACCES

// Cause 3: No execute permission
system("/usr/bin/myprogram"); // EACCES
```

## How to Fix

### Fix 1: Check permissions

```c
#include <sys/stat.h>

struct stat st;
if (stat("file.txt", &st) == -1) {
    perror("stat");
}
```

### Fix 2: Change permissions

```bash
chmod 644 file.txt   # rw-r--r--
chmod 755 script.sh  # rwxr-xr-x
```

### Fix 3: Run with correct user

```bash
sudo ./program
# or
su - user
```

## Examples

```c
#include <stdio.h>
#include <fcntl.h>
#include <errno.h>

int main(void) {
    int fd = open("file.txt", O_WRONLY | O_CREAT, 0644);
    if (fd == -1) {
        if (errno == EACCES) {
            fprintf(stderr, "Permission denied\n");
        }
        perror("open");
        return 1;
    }
    close(fd);
    return 0;
}
```

## Related Errors

- [Read-only file system]({{< relref "/languages/c/read-only-file-system" >}}) — EROFS.
- [No such file]({{< relref "/languages/c/no-such-file" >}}) — ENOENT.
- [Bad file descriptor]({{< relref "/languages/c/bad-file-descriptor" >}}) — EBADF.
