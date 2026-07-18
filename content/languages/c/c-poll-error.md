---
title: "[Solution] C poll() Error — How to Fix"
description: "Fix C poll() errors including timeout handling, EINTR, and event processing."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C poll() Error — How to Fix

poll() monitors file descriptors for events. Common errors include not handling EINTR, not checking revents (returned events), using incorrect timeout values, and not processing all pollfd entries.

## Common Error Messages

- `poll: Interrupted system call (EINTR)`
- `poll returns 0 — timeout expired`
- `poll returns -1 — invalid fd`
- `revents not checked — missed events`

## How to Fix It

### Handle EINTR and check revents

```c
#include <poll.h>
#include <errno.h>
#include <stdio.h>

int wait_for_data(int fd, int timeout_ms) {
    struct pollfd pfd = { .fd = fd, .events = POLLIN };
    int ret;
    do {
        ret = poll(&pfd, 1, timeout_ms);
    } while (ret == -1 && errno == EINTR);
    if (ret > 0 && (pfd.revents & POLLIN)) {
        return 1;  // data available
    }
    return ret;
}
```

### Monitor multiple fds with poll

```c
#include <poll.h>
#include <stdio.h>

int main(void) {
    struct pollfd fds[2];
    fds[0] = (struct pollfd){ .fd = STDIN_FILENO, .events = POLLIN };
    fds[1] = (struct pollfd){ .fd = STDOUT_FILENO, .events = POLLOUT };
    int ret = poll(fds, 2, 5000);
    if (ret > 0) {
        if (fds[0].revents & POLLIN) printf("stdin readable\n");
        if (fds[1].revents & POLLOUT) printf("stdout writable\n");
    }
    return 0;
}
```

### Handle poll errors

```c
#include <poll.h>
#include <errno.h>
#include <stdio.h>

int poll_with_retry(struct pollfd *fds, nfds_t nfds, int timeout) {
    int ret;
    do {
        ret = poll(fds, nfds, timeout);
    } while (ret == -1 && errno == EINTR);
    if (ret == -1) perror("poll");
    return ret;
}
```

### Use poll for idle detection

```c
#include <poll.h>
#include <stdio.h>

int is_fd_ready(int fd, short events, int timeout_ms) {
    struct pollfd pfd = { .fd = fd, .events = events };
    int ret = poll(&pfd, 1, timeout_ms);
    if (ret > 0) return pfd.revents & events;
    return 0;
}
```

## Common Scenarios

### Scenario 1: poll returns -1 because fd was closed

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Timeout value -1 causes infinite wait

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Forgetting to check revents after poll returns

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always check revents, not just return value
- **Tip 2:** Handle EINTR by retrying poll
- **Tip 3:** Use positive timeout for finite waits, -1 for infinite, 0 for non-blocking
