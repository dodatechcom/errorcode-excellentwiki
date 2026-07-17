---
title: "[Solution] C errno ENOTEMPTY — Directory not empty Fix"
description: "Fix C ENOTEMPTY (Directory not empty) by removing all entries before calling rmdir or unlink."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ENOTEMPTY — Directory not empty Fix

When `rmdir()` is called on a directory that still contains files or subdirectories, the call fails and sets `errno` to `ENOTEMPTY`. The POSIX standard requires that only empty directories can be removed with `rmdir()`.

## Common Causes

- Calling `rmdir()` on a directory that still contains files or subdirectories.
- Hidden files (dotfiles) like `.` or `..` are present — though `.` and `..` are not counted.
- The directory contains hidden files (e.g., `.hidden_file`) that were overlooked.
- Symbolic links or special entries remain in the directory.

## How to Fix

Remove all files and subdirectories before calling `rmdir()`. Use `unlink()` for files and recursively delete subdirectories.

```c
#include <dirent.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <sys/stat.h>

int remove_directory(const char *path) {
    DIR *dir = opendir(path);
    if (dir == NULL) return -1;

    struct dirent *entry;
    char fullpath[PATH_MAX];

    while ((entry = readdir(dir)) != NULL) {
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
            continue;
        snprintf(fullpath, sizeof(fullpath), "%s/%s", path, entry->d_name);
        if (entry->d_type == DT_DIR) {
            remove_directory(fullpath);
        } else {
            unlink(fullpath);
        }
    }
    closedir(dir);
    return rmdir(path);
}
```

## Examples

Trying to remove a non-empty directory:

```c
#include <unistd.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    if (rmdir("/tmp/mydir") == -1) {
        if (errno == ENOTEMPTY) {
            fprintf(stderr, "Directory is not empty\n");
            fprintf(stderr, "errno: %d (ENOTEMPTY)\n", errno);
        } else {
            perror("rmdir");
        }
    }
    return 0;
}
```

## Related Errors

- [errno-39 ENOTEMPTY](/languages/c/errno-enotempty/) — directory not empty (numeric).
- [errno-2 ENOENT](/languages/c/errno-enotempty/) — no such file or directory.
- [errno-20 ENOTDIR](/languages/c/errno-enotempty/) — not a directory.
