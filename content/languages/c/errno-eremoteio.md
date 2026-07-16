---
title: "[Solution] C errno EREMOTEIO — Remote I/O error Fix"
description: "Fix C EREMOTEIO (Remote I/O error) by handling network storage failures and checking remote filesystem health."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["eremoteio", "remote-io-error", "nfs", "network-storage", "io-error"]
weight: 5
---

# [Solution] C errno EREMOTEIO — Remote I/O error Fix

When an I/O operation fails on a remote filesystem (such as NFS, CIFS, or other network-mounted filesystems) due to a remote server error, the system call fails and sets `errno` to `EREMOTEIO`. This error indicates the remote server returned an I/O error.

## Common Causes

- The NFS server encountered a disk error or I/O failure.
- The network connection to the remote storage was interrupted during I/O.
- The remote filesystem has run out of space.
- Authentication or authorization expired on the remote server.

## How to Fix

Check the remote server's health and logs. Implement retry logic for transient remote I/O errors.

```c
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>

#define MAX_RETRIES 3

int read_with_retry(int fd, void *buf, size_t count) {
    for (int i = 0; i < MAX_RETRIES; i++) {
        ssize_t n = read(fd, buf, count);
        if (n != -1) return n;
        if (errno != EREMOTEIO) return -1;
        fprintf(stderr, "Remote I/O error — retrying (%d/%d)\n", i + 1, MAX_RETRIES);
        usleep(100000 * (i + 1));  // Backoff: 100ms, 200ms, 300ms
    }
    return -1;
}

int main(void) {
    int fd = open("/mnt/nfs/data.bin", O_RDONLY);
    if (fd == -1) { perror("open"); return 1; }

    char buf[4096];
    ssize_t n = read_with_retry(fd, buf, sizeof(buf));
    if (n == -1) {
        fprintf(stderr, "Read failed after retries: %s\n", strerror(errno));
    }
    close(fd);
    return 0;
}
```

## Examples

I/O on an unreachable NFS mount:

```c
#include <stdio.h>
#include <errno.h>

int main(void) {
    FILE *fp = fopen("/mnt/nfs/data.txt", "r");
    if (fp == NULL) {
        perror("fopen");
        if (errno == EREMOTEIO) {
            fprintf(stderr, "Remote I/O error — check NFS server\n");
        }
        return 1;
    }
    fclose(fp);
    return 0;
}
```

## Related Errors

- [errno-121 EREMOTEIO]({{< relref "/languages/c/errno-eremoteio" >}}) — remote I/O error (numeric).
- [errno-5 EIO](/languages/c/errno-eremoteio/) — input/output error.
- [errno-113 EHOSTUNREACH]({{< relref "/languages/c/errno-eHOSTUNREACH" >}}) — no route to host.
