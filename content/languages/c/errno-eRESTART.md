---
title: "[Solution] C errno ERESTART — Interrupted system call should be restarted Fix"
description: "Fix C ERESTART (Interrupted system call should be restarted) by handling signal interruption and using SA_RESTART."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["erestart", "interrupted-system-call", "signal-restart", "sa-restart"]
weight: 5
---

# [Solution] C errno ERESTART — Interrupted system call should be restarted Fix

When a system call is interrupted by a signal and the kernel determines it should be automatically restarted, the internal error `ERESTART` is set. This error is typically not visible to user-space programs because the kernel transparently restarts the call, but it can manifest in certain edge cases.

## Common Causes

- A signal interrupts a blocking system call (`read()`, `write()`, `select()`, etc.).
- The `SA_RESTART` flag is not set on the signal handler, causing the call to fail with `EINTR`.
- The kernel's restart mechanism fails for certain system calls.
- A debugger (ptrace) intercepted the restart attempt.

## How to Fix

Use `SA_RESTART` with `sigaction()` for automatic restart, or handle `EINTR` with retry logic.

```c
#include <signal.h>
#include <stdio.h>

void handler(int sig) {
    printf("Signal %d received\n", sig);
}

int main(void) {
    struct sigaction sa;
    sa.sa_handler = handler;
    sa.sa_flags = SA_RESTART;  // Restart interrupted system calls
    sigemptyset(&sa.sa_mask);

    sigaction(SIGUSR1, &sa, NULL);

    // read() will be automatically restarted after SIGUSR1
    char buf[100];
    ssize_t n = read(STDIN_FILENO, buf, sizeof(buf));
    return 0;
}
```

## Examples

Handling `EINTR` with manual retry:

```c
#include <unistd.h>
#include <signal.h>
#include <stdio.h>
#include <errno.h>

volatile sig_atomic_t interrupted = 0;

void handler(int sig) {
    interrupted = 1;
}

int main(void) {
    signal(SIGINT, handler);

    char buf[256];
    ssize_t n;
    do {
        n = read(STDIN_FILENO, buf, sizeof(buf));
    } while (n == -1 && errno == EINTR);

    if (n == -1) {
        perror("read");
    }
    return 0;
}
```

## Related Errors

- [errno-4 EINTR](/languages/c/errno-eRESTART/) — interrupted system call.
- [errno-4 ERESTART]({{< relref "/languages/c/errno-eRESTART" >}}) — system call should be restarted (internal).
- [errno-11 EAGAIN](/languages/c/errno-eRESTART/) — resource unavailable, try again.
