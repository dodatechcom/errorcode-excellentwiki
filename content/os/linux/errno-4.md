---
title: "[Solution] Linux EINTR (errno 4) — Interrupted System Call Fix"
description: "Fix Linux EINTR (errno 4) Interrupted System Call error. Handle signal interruptions, retry logic, and SA_RESTART for reliable programs."
platforms: ["linux"]
severities: ["error"]
error_types: ["runtime"]
weight: 40
---

# Linux EINTR (errno 4) — Interrupted System Call

EINTR (errno 4) occurs when a blocking system call is interrupted by a signal and the signal handler returns. The kernel aborts the system call and returns this error to inform your program that the call did not complete. Commonly affected calls include `read()`, `write()`, `accept()`, `connect()`, `sleep()`, and `wait()`. This error is fundamental to Unix signal handling and must be handled in any robust application.

## Common Causes

- A signal (e.g., SIGALRM, SIGCHLD, SIGTERM) was delivered during a blocking I/O call
- Using `sleep()` or `nanosleep()` when a timer signal is pending
- Network operations interrupted by periodic keepalive or timeout signals
- Child process exits and SIGCHLD is delivered during `wait()`
- Default signal handlers that do not set SA_RESTART

## How to Fix EINTR

### 1. Retry the System Call

The simplest and most common approach is to retry the interrupted call:

```c
ssize_t result;
do {
    result = read(fd, buffer, sizeof(buffer));
} while (result == -1 && errno == EINTR);
```

This pattern works for `read()`, `write()`, `accept()`, `connect()`, `recv()`, `send()`, and many other system calls.

### 2. Use SA_RESTART When Registering Signal Handlers

The `SA_RESTART` flag tells the kernel to automatically restart interrupted system calls:

```c
#include <signal.h>

struct sigaction sa;
sa.sa_handler = my_signal_handler;
sa.sa_flags = SA_RESTART;
sigemptyset(&sa.sa_mask);
sigaction(SIGCHLD, &sa, NULL);
```

With `SA_RESTART`, calls like `read()`, `write()`, and `sleep()` restart automatically. Note that some calls like `accept()` and `connect()` are **not** restarted even with `SA_RESTART` on Linux.

### 3. Handle EINTR in a Retry Loop with Timeout

For network programming, combine retry logic with a timeout:

```c
#include <sys/select.h>

int read_with_timeout(int fd, void *buf, size_t n, int timeout_sec) {
    struct timeval tv = { .tv_sec = timeout_sec, .tv_usec = 0 };
    fd_set fds;
    ssize_t result;

    while (1) {
        FD_ZERO(&fds);
        FD_SET(fd, &fds);

        int ready = select(fd + 1, &fds, NULL, NULL, &tv);
        if (ready < 0) {
            if (errno == EINTR) continue;
            return -1;
        }
        if (ready == 0) return -2; // timeout

        result = read(fd, buf, n);
        if (result < 0 && errno == EINTR) continue;
        return result;
    }
}
```

### 4. Check EINTR After sleep() and nanosleep()

Sleep functions can be interrupted by signals:

```c
#include <unistd.h>
#include <time.h>

// Simple retry for sleep
unsigned int remaining = sleep(10);
if (remaining > 0) {
    // Sleep was interrupted, remaining seconds left
    printf("Interrupted with %u seconds remaining\n", remaining);
}

// More precise with nanosleep
struct timespec req = { .tv_sec = 1, .tv_nsec = 0 };
struct timespec rem;
while (nanosleep(&req, &rem) == -1 && errno == EINTR) {
    req = rem; // Sleep for the remaining time
}
```

### 5. Use signalfd to Avoid EINTR Entirely (Linux-Specific)

On Linux, `signalfd()` lets you handle signals via file descriptor reads, avoiding EINTR on other file descriptors:

```c
#include <sys/signalfd.h>
#include <signal.h>

sigset_t mask;
sigemptyset(&mask);
sigaddset(&mask, SIGCHLD);
sigprocmask(SIG_BLOCK, &mask, NULL);

int sfd = signalfd(-1, &mask, SFD_NONBLOCK);

// Now read() on sfd delivers signals without interrupting other I/O
```

### 6. Handle EINTR in Python

Python's higher-level I/O generally handles EINTR, but lower-level code may need explicit handling:

```python
import os
import signal
import errno

# Retry wrapper for os.read
def read_eintr(fd, n):
    while True:
        try:
            return os.read(fd, n)
        except OSError as e:
            if e.errno != errno.EINTR:
                raise
```

Python 3.5+ handles EINTR automatically in most built-in I/O operations via PEP 475.

### 7. Use pselect() for Signal-Safe Multiplexing

`pselect()` atomically unblocks signals and calls select, reducing EINTR-related races:

```c
#include <sys/select.h>

sigset_t sigmask, origmask;
sigemptyset(&sigmask);
sigaddset(&sigmask, SIGCHLD);
sigprocmask(SIG_BLOCK, &sigmask, &origmask);

fd_set fds;
FD_SET(fd, &fds);
struct timespec timeout = { .tv_sec = 5, .tv_nsec = 0 };

int ready = pselect(fd + 1, &fds, NULL, NULL, &timeout, &origmask);
```

## Best Practices

- Always handle EINTR in retry loops for portable code
- Use `SA_RESTART` where appropriate but do not rely on it for `accept()` or `connect()`
- Log EINTR occurrences at debug level for troubleshooting
- Consider using `signalfd()` or `epoll` signal handling on Linux for complex applications

## Related Error Codes

- [EAGAIN (errno 11)](/os/linux/errno-11/) — Resource temporarily unavailable
- [EIO (errno 5)](/os/linux/errno-5/) — Input/output error
- [ECANCELED (errno 125)](/os/linux/errno-125/) — Operation canceled
