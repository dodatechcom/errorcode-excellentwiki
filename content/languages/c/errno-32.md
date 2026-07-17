---
title: "[Solution] C errno 32 EPIPE — Broken pipe"
description: "Fix C errno 32 EPIPE (Broken pipe) by handling SIGPIPE signal, checking peer connection, and using socket options."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno 32 EPIPE — Broken pipe

Broken pipe occurs when a system call fails and sets `errno` to 32. This error indicates that the requested operation cannot be performed due to the specific condition described by EPIPE.

## Common Causes

- A client disconnects mid-response on a socket or pipe.
- A subprocess closes its stdin before the parent finishes writing.
- Writing to a pipe whose read end was closed by the receiving process.
- A reverse proxy or load balancer closes the connection before the backend responds.

## How to Fix

```c
#include <signal.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    signal(SIGPIPE, SIG_IGN);
    int pipefd[2];
    pipe(pipefd);
    close(pipefd[0]);
    char msg[] = "Hello";
    ssize_t n = write(pipefd[1], msg, sizeof(msg));
    if (n == -1) {
        perror("write");  // "write: Broken pipe"
        fprintf(stderr, "errno: %d\n", errno);  // 32
    }
    close(pipefd[1]);
    return 0;
}
```

## Examples

```c
#include <sys/socket.h>
#include <stdio.h>
#include <errno.h>

ssize_t safe_send(int sockfd, const void *buf, size_t len, int flags) {
    return send(sockfd, buf, len, flags | MSG_NOSIGNAL);
}
```

## Related Errors

- [errno-110 ETIMEDOUT]({{< relref "/languages/c/errno-110" >}}) — connection timed out.
- [errno-115 EINPROGRESS]({{< relref "/languages/c/errno-115" >}}) — operation in progress.
- [errno-32 EPIPE]({{< relref "/languages/c/errno-32" >}}) — broken pipe (self).
