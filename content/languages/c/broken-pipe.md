---
title: "[Solution] C Broken pipe: EPIPE"
description: "Fix C broken pipe (EPIPE). Handle SIGPIPE signal and write errors on pipes."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Broken pipe: EPIPE

EPIPE occurs when you write to a pipe or socket whose read end has been closed. The process receives a `SIGPIPE` signal which, if not handled, terminates the program.

## Common Causes

```c
// Cause 1: Writing to closed pipe end
int fd[2];
pipe(fd);
close(fd[0]); // close read end
write(fd[1], "data", 4); // EPIPE

// Cause 2: Reading end of pipe closed
// Common with shell pipes: cmd1 | cmd2
// If cmd2 exits, cmd1 gets SIGPIPE

// Cause 3: Socket peer disconnected
send(sock, data, len, 0); // peer closed connection
```

## How to Fix

### Fix 1: Ignore SIGPIPE

```c
signal(SIGPIPE, SIG_IGN);
// write() will return -1 with errno = EPIPE
```

### Fix 2: Check write return value

```c
ssize_t written = write(fd[1], "data", 4);
if (written == -1) {
    if (errno == EPIPE) {
        fprintf(stderr, "Pipe closed\n");
    }
}
```

### Fix 3: Use MSG_NOSIGNAL on sockets

```c
send(sock, data, len, MSG_NOSIGNAL);
```

## Examples

```c
#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <errno.h>

int main(void) {
    signal(SIGPIPE, SIG_IGN);
    
    int fd[2];
    pipe(fd);
    close(fd[0]);
    
    ssize_t result = write(fd[1], "hello", 5);
    if (result == -1 && errno == EPIPE) {
        fprintf(stderr, "Broken pipe\n");
    }
    
    close(fd[1]);
    return 0;
}
```

## Related Errors

- [Connection reset]({{< relref "/languages/c/connection-reset" >}}) — ECONNRESET.
- [Connection refused]({{< relref "/languages/c/connection-refused-c" >}}) — ECONNREFUSED.
- [Bad file descriptor]({{< relref "/languages/c/bad-file-descriptor" >}}) — EBADF.
