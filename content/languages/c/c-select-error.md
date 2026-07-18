---
title: "[Solution] C select() Error — How to Fix"
description: "Fix C select() errors including FD_SET overflow, EINTR, and fd_set management."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C select() Error — How to Fix

select() monitors file descriptors for readiness. Common errors include FD_SET with fd >= FD_SETSIZE (typically 1024), not re-initializing fd_sets before each call, and not handling EINTR.

## Common Error Messages

- `select: Bad file descriptor`
- `FD_SET: fd >= FD_SETSIZE`
- `select interrupted by signal (EINTR)`
- `fd_set not re-initialized — returns immediately`

## How to Fix It

### Check fd < FD_SETSIZE

```c
#include <sys/select.h>
#include <stdio.h>

int main(void) {
    int fd = 5;
    if (fd >= FD_SETSIZE) {
        fprintf(stderr, "fd too large for select\n");
        return 1;
    }
    fd_set readfds;
    FD_ZERO(&readfds);
    FD_SET(fd, &readfds);
    struct timeval tv = { .tv_sec = 5 };
    int ret = select(fd + 1, &readfds, NULL, NULL, &tv);
    if (ret > 0 && FD_ISSET(fd, &readfds))
        printf("fd ready\n");
    return 0;
}
```

### Re-initialize fd_sets before each call

```c
#include <sys/select.h>

int wait_for_fd(int fd) {
    fd_set readfds;
    struct timeval tv;
    while (1) {
        FD_ZERO(&readfds);
        FD_SET(fd, &readfds);
        tv = (struct timeval){ .tv_sec = 5 };
        int ret = select(fd + 1, &readfds, NULL, NULL, &tv);
        if (ret > 0 && FD_ISSET(fd, &readfds)) return 1;
        if (ret == 0) return 0;  // timeout
    }
}
```

### Use select for connection timeout

```c
#include <sys/select.h>
#include <sys/socket.h>
#include <unistd.h>

int connect_with_timeout(int fd, struct sockaddr *addr, socklen_t len, int secs) {
    int ret = connect(fd, addr, len);
    if (ret == 0 || errno != EINPROGRESS) return ret;
    fd_set wfds;
    FD_ZERO(&wfds);
    FD_SET(fd, &wfds);
    struct timeval tv = { .tv_sec = secs };
    ret = select(fd + 1, NULL, &wfds, NULL, &tv);
    if (ret > 0 && FD_ISSET(fd, &wfds)) return 0;
    return -1;
}
```

### Handle select EINTR

```c
#include <sys/select.h>
#include <errno.h>

int select_safe(int nfds, fd_set *r, fd_set *w, fd_set *e, struct timeval *tv) {
    int ret;
    do {
        ret = select(nfds, r, w, e, tv);
    } while (ret == -1 && errno == EINTR);
    return ret;
}
```

## Common Scenarios

### Scenario 1: FD_SET with fd >= FD_SETSIZE causes buffer overflow

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: fd_set not re-initialized causing select to return immediately

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Using select on Windows where behavior differs

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Never use select with fd >= FD_SETSIZE — use poll instead
- **Tip 2:** Always re-initialize fd_sets before calling select again
- **Tip 3:** Handle EINTR by retrying the select call
