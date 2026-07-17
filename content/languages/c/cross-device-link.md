---
title: "[Solution] C Invalid cross-device link: EXDEV"
description: "Fix C invalid cross-device link (EXDEV). Use copy-and-delete for cross-filesystem renames."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Invalid cross-device link: EXDEV

EXDEV occurs when you try to `rename()` or `link()` a file across different filesystems (e.g., from ext4 to tmpfs). These operations only work within the same filesystem.

## Common Causes

```c
// Cause 1: Cross-device rename
rename("/ext4/file.txt", "/tmpfs/file.txt"); // EXDEV

// Cause 2: Cross-device hard link
link("/ext4/file.txt", "/tmpfs/link.txt"); // EXDEV

// Cause 3: Different mount points
rename("/home/user/file", "/mnt/backup/file"); // EXDEV
```

## How to Fix

### Fix 1: Copy and delete

```c
#include <sys/stat.h>
#include <fcntl.h>

int copy_file(const char *src, const char *dst) {
    struct stat st;
    stat(src, &st);
    
    int fd_in = open(src, O_RDONLY);
    int fd_out = open(dst, O_WRONLY | O_CREAT | O_TRUNC, st.st_mode);
    
    char buf[4096];
    ssize_t n;
    while ((n = read(fd_in, buf, sizeof(buf))) > 0) {
        write(fd_out, buf, n);
    }
    
    close(fd_in);
    close(fd_out);
    unlink(src); // delete original
    return 0;
}
```

### Fix 2: Use same filesystem

```bash
# Check if same filesystem
stat -f -c "%d" /ext4/file.txt /tmpfs/file.txt
```

## Related Errors

- [No such file]({{< relref "/languages/c/no-such-file" >}}) — ENOENT.
- [Permission denied]({{< relref "/languages/c/permission-denied-file" >}}) — EACCES.
- [Read-only file system]({{< relref "/languages/c/read-only-file-system" >}}) — EROFS.
