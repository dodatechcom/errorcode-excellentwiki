---
title: "[Solution] C errno ETOOMANYREFS — Too many references (variant) Fix"
description: "Fix C ETOOMANYREFS (Too many references variant) by managing file descriptor references and reducing fd passing."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["etoomanyrefs", "too-many-references-variant", "fd-passing", "scm-rights"]
weight: 5
---

# [Solution] C errno ETOOMANYREFS — Too many references (variant) Fix

An alternate manifestation of `ETOOMANYREFS` occurring specifically during `sendmsg()` with `SCM_RIGHTS` (file descriptor passing) when the total number of referenced file descriptors exceeds the kernel's internal limits.

## Common Causes

- Passing too many file descriptors via `SCM_RIGHTS` in a single `sendmsg()` call.
- Accumulated file descriptor references from multiple `sendmsg()` calls.
- The receiving process has not consumed/duplicated the passed file descriptors.
- Internal kernel fd reference counting exceeds the maximum.

## How to Fix

Limit the number of file descriptors passed per message. Consume passed fds promptly on the receiving side.

```c
#include <sys/socket.h>
#include <sys/un.h>
#include <stdio.h>
#include <errno.h>

#define MAX_FDS_PER_MSG 256

int send_fds(int sock, int *fds, int count) {
    if (count > MAX_FDS_PER_MSG) {
        fprintf(stderr, "Too many fds to send at once: %d\n", count);
        return -1;
    }

    struct msghdr msg = {0};
    struct iovec iov = { .iov_base = "x", .iov_len = 1 };
    msg.msg_iov = &iov;
    msg.msg_iovlen = 1;

    char cmsgbuf[CMSG_SPACE(count * sizeof(int))];
    msg.msg_control = cmsgbuf;
    msg.msg_controllen = sizeof(cmsgbuf);

    struct cmsghdr *cmsg = CMSG_FIRSTHDR(&msg);
    cmsg->cmsg_level = SOL_SOCKET;
    cmsg->cmsg_type = SCM_RIGHTS;
    cmsg->cmsg_len = CMSG_LEN(count * sizeof(int));
    memcpy(CMSG_DATA(cmsg), fds, count * sizeof(int));

    if (sendmsg(sock, &msg, 0) == -1) {
        if (errno == ETOOMANYREFS) {
            fprintf(stderr, "Too many fd references (errno %d)\n", errno);
        }
        return -1;
    }
    return 0;
}

int main(void) {
    int sv[2];
    socketpair(AF_UNIX, SOCK_STREAM, 0, sv);
    int fds[] = {0, 1, 2};
    send_fds(sv[0], fds, 3);
    close(sv[0]);
    close(sv[1]);
    return 0;
}
```

## Examples

Passing excessive file descriptors:

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    // Attempting to pass too many fds
    int fds[1024];
    for (int i = 0; i < 1024; i++) fds[i] = i;

    // This may fail with ETOOMANYREFS
    fprintf(stderr, "Attempting to pass many fds (errno %d if it fails)\n", ETOOMANYREFS);
    return 0;
}
```

## Related Errors

- [errno-73 ETOOMANYREFS]({{< relref "/languages/c/errno-eTOOMANYREFS" >}}) — too many references (numeric).
- [errno-24 EMFILE]({{< relref "/languages/c/errno-emfile" >}}) — too many open files.
- [errno-11 EAGAIN](/languages/c/errno-eTOOMANYREFS-2/) — resource unavailable, try again.
