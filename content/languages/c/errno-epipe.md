---
title: "[Solution] C errno EPIPE — Broken pipe Fix"
description: "Fix C EPIPE (Broken pipe) by handling SIGPIPE signal, checking for closed read end, and using MSG_NOSIGNAL."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EPIPE — Broken pipe Fix

When a process writes to a pipe or socket whose read end has been closed, the write fails and sets `errno` to `EPIPE`. By default, the kernel delivers a `SIGPIPE` signal to the process, which typically terminates it. This is common when piping output to a command that exits early.

## Common Causes

- The read end of a pipe has been closed (e.g., the downstream process exited).
- A socket connection has been closed by the peer before the write.
- Writing to a FIFO where no process has the read end open.
- The `SIGPIPE` signal is not being handled, causing unexpected termination.

## How to Fix

Either handle `SIGPIPE` or ignore it and check for `EPIPE` on write. Use `MSG_NOSIGNAL` for sockets.

```c
#include <signal.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>

int main(void) {
    // Ignore SIGPIPE so write() returns -1 with errno=EPIPE instead of killing us
    signal(SIGPIPE, SIG_IGN);

    int fds[2];
    pipe(fds);

    close(fds[0]);  // Close read end

    ssize_t n = write(fds[1], "hello", 5);
    if (n == -1) {
        fprintf(stderr, "write failed: %s (errno %d)\n", strerror(errno), errno);
    }
    close(fds[1]);
    return 0;
}
```

## Examples

Piping to a command that exits early:

```bash
# head closes its stdin after 1 line, causing SIGPIPE in cat
cat largefile.txt | head -1
```

Writing to a socket after peer disconnect:

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = /* connected socket */;
    // Peer closes connection
    ssize_t n = send(sock, "data", 4, MSG_NOSIGNAL);
    if (n == -1) {
        perror("send");  // "send: Broken pipe"
        fprintf(stderr, "errno: %d (EPIPE)\n", errno);
    }
    return 0;
}
```

## Related Errors

- [errno-32 EPIPE](/languages/c/errno-epipe/) — broken pipe (numeric).
- [errno-11 EAGAIN](/languages/c/errno-epipe/) — resource unavailable, try again.
- [errno-32 EPIPE](/languages/c/errno-epipe/) — broken pipe signal.
