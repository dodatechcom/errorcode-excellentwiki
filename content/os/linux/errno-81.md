---
title: "[Solution] Linux ECANCELED (errno 81) — Operation Canceled Fix"
description: "Fix Linux ECANCELED (errno 81) Operation canceled error. Solutions for asynchronous operation and cancellation issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux ECANCELED (errno 81) — Operation Canceled

ECANCELED (errno 81) means an asynchronous operation was canceled before completing. This error occurs when a pending I/O operation (such as `aio_read()` or `io_submit()`) is canceled before it finishes, or when a signal interrupts a blocking system call. It is distinct from EINTR (errno 4) because ECANCELED indicates explicit cancellation, not signal interruption.

## Common Causes

- Asynchronous I/O operation was canceled by the application
- Signal interrupted a blocking I/O operation
- Thread cancellation during I/O
- Application explicitly canceled pending operations

## How to Fix ECANCELED

### 1. Check for Pending AIO Operations

Verify active asynchronous I/O operations:

```bash
cat /proc/<pid>/status | grep -i aio
```

### 2. Handle Cancellation in Applications

Check for cancellation errors and retry:

```bash
# In C: handle ECANCELED
if (errno == ECANCELED) {
    // Operation was canceled, retry or clean up
    aio_error(&aiocb);
}
```

### 3. Avoid Cancelling During Critical I/O

Defer cancellation until I/O completes:

```bash
# In C: use aio_error to check status before canceling
int status = aio_error(&aiocb);
if (status == ECANCELED) {
    // Handle cancellation
}
```

### 4. Use Proper Signal Handling

Ensure signals don't interrupt critical I/O:

```bash
# In C: block signals during critical sections
sigset_t mask;
sigemptyset(&mask);
sigaddset(&mask, SIGINT);
sigprocmask(SIG_BLOCK, &mask, NULL);
```

## Verification

After handling cancellation properly, confirm operations complete:

```bash
strace -e trace=aio_read,aio_error ./program
```

## Related Error Codes

- [EINTR (errno 4)](/os/linux/errno-4/) — Interrupted system call
- [EIO (errno 5)](/os/linux/errno-5/) — Input/output error
- [EAGAIN (errno 11)](/os/linux/errno-11/) — Resource temporarily unavailable
