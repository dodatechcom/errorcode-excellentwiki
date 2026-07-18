---
title: "[Solution] C pipe() Error — How to Fix"
description: "Fix C pipe() errors including EMFILE, broken pipes, and unidirectional data flow issues."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C pipe() Error — How to Fix

pipe() creates a unidirectional data channel. Common errors include not closing read/write ends properly, ignoring EPIPE on write, and exceeding the pipe buffer capacity causing blocking.

## Common Error Messages

- `pipe: Too many open files (EMFILE)`
- `Broken pipe (EPIPE)`
- `pipe buffer full — write blocks`
- `File descriptor leak from unclosed pipe ends`

## How to Fix It

### Close unused pipe ends

```c
#include <unistd.h>
#include <stdio.h>

int main(void) {
    int pipefd[2];
    if (pipe(pipefd) == -1) { perror("pipe"); return 1; }
    if (fork() == 0) {
        close(pipefd[1]);  // close write end
        char buf[64];
        read(pipefd[0], buf, sizeof(buf));
        close(pipefd[0]);
    } else {
        close(pipefd[0]);  // close read end
        write(pipefd[1], "hello", 5);
        close(pipefd[1]);
    }
    return 0;
}
```

### Handle broken pipe gracefully

```c
#include <signal.h>
#include <unistd.h>

void ignore_pipe(int sig) {}

int main(void) {
    struct sigaction sa = { .sa_handler = ignore_pipe };
    sigemptyset(&sa.sa_mask);
    sigaction(SIGPIPE, &sa, NULL);
    // writes will return -1 with EPIPE instead of terminating
    return 0;
}
```

### Use pipe2 for close-on-exec

```c
#include <fcntl.h>
#include <unistd.h>

int main(void) {
    int pipefd[2];
    if (pipe2(pipefd, O_CLOEXEC) == -1) {
        perror("pipe2");
        return 1;
    }
    // auto-close on exec
    close(pipefd[0]);
    close(pipefd[1]);
    return 0;
}
```

### Use pipe with select/poll for non-blocking I/O

```c
#include <unistd.h>
#include <poll.h>

int main(void) {
    int pipefd[2];
    pipe(pipefd);
    struct pollfd pfd = { .fd = pipefd[0], .events = POLLIN };
    int ret = poll(&pfd, 1, 5000);  // 5s timeout
    if (ret > 0 && (pfd.revents & POLLIN)) {
        char buf[64];
        read(pipefd[0], buf, sizeof(buf));
    }
    close(pipefd[0]);
    close(pipefd[1]);
    return 0;
}
```

## Common Scenarios

### Scenario 1: pipe() returns -1 with EMFILE

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Write to pipe after reader closes causes EPIPE

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Child inherits both pipe ends causing data loops

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always close unused pipe ends in parent and child
- **Tip 2:** Handle SIGPIPE or check for EPIPE on writes
- **Tip 3:** Use pipe2 with O_CLOEXEC to prevent fd leaks to child processes
