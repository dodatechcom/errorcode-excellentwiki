---
title: "[Solution] C errno ESTALE — Stale file handle Fix"
description: "Fix C ESTALE (Stale file handle) by handling NFS stale handles, reopening files, and recovering from filesystem changes."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["estale", "stale-file-handle", "nfs", "file-handle", "reconnect"]
weight: 5
---

# [Solution] C errno ESTALE — Stale file handle Fix

When a file handle becomes stale (typically because the NFS server rebooted or the filesystem was re-exported), any operation on the file fails and sets `errno` to `ESTALE`. This error indicates the file handle is no longer valid.

## Common Causes

- The NFS server rebooted, invalidating all cached file handles.
- The filesystem was unmounted and remounted on the server.
- The file was deleted and recreated with a new inode.
- A file descriptor was kept open across an NFS server restart.

## How to Fix

Reopen the file to obtain a fresh file handle. Avoid caching file handles across long periods.

```c
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <fcntl.h>

int reopen_on_stale(int fd, const char *path) {
    char buf[1024];
    ssize_t n = read(fd, buf, sizeof(buf));
    if (n == -1 && errno == ESTALE) {
        fprintf(stderr, "Stale file handle — reopening %s\n", path);
        close(fd);
        fd = open(path, O_RDONLY);
        if (fd == -1) {
            fprintf(stderr, "reopen failed: %s\n", strerror(errno));
            return -1;
        }
        return fd;
    }
    return fd;
}

int main(void) {
    int fd = open("/mnt/nfs/data.txt", O_RDONLY);
    if (fd == -1) { perror("open"); return 1; }

    fd = reopen_on_stale(fd, "/mnt/nfs/data.txt");
    if (fd == -1) return 1;

    close(fd);
    return 0;
}
```

## Examples

Accessing a file after NFS server restart:

```c
#include <stdio.h>
#include <errno.h>

int main(void) {
    FILE *fp = fopen("/mnt/nfs/data.txt", "r");
    if (fp == NULL) { perror("fopen"); return 1; }

    char buf[256];
    if (fgets(buf, sizeof(buf), fp) == NULL) {
        if (errno == ESTALE) {
            fprintf(stderr, "Stale file handle — NFS server may have rebooted\n");
            fprintf(stderr, "errno: %d (ESTALE)\n", errno);
        }
    }
    fclose(fp);
    return 0;
}
```

## Related Errors

- [errno-116 ESTALE]({{< relref "/languages/c/errno-eSTALE" >}}) — stale file handle (numeric).
- [errno-2 ENOENT](/languages/c/errno-eSTALE/) — no such file or directory.
- [errno-121 EREMOTEIO]({{< relref "/languages/c/errno-eremoteio" >}}) — remote I/O error.
