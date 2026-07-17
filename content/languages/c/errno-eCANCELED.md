---
title: "[Solution] C errno ECANCELED — Operation canceled Fix"
description: "Fix C ECANCELED (Operation canceled) by handling AIO cancellations, checking error returns, and managing async operations."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ECANCELED — Operation canceled Fix

When an asynchronous I/O operation is canceled before completing (via `aio_cancel()`), or a system call is explicitly canceled by another thread, the operation fails and sets `errno` to `ECANCELED`. This error indicates the operation was intentionally terminated.

## Common Causes

- An AIO operation was canceled via `aio_cancel()` before it completed.
- A thread canceled a blocking operation of another thread.
- The `pthread_cancel()` function terminated a blocking system call.
- A timer or watchdog killed a pending I/O operation.

## How to Fix

Check the return value and `errno` of AIO operations. Handle `ECANCELED` by cleaning up resources.

```c
#include <aio.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct aiocb aio = {0};
    aio.aio_fildes = open("data.txt", O_RDONLY);
    aio.aio_buf = malloc(4096);
    aio.aio_nbytes = 4096;

    aio_read(&aio);

    // Cancel the operation
    aio_cancel(aio.aio_fildes, &aio);

    int ret = aio_error(&aio);
    if (ret == ECANCELED) {
        fprintf(stderr, "AIO operation was canceled (errno %d)\n", ECANCELED);
    } else if (ret == 0) {
        ssize_t bytes = aio_return(&aio);
        printf("Read %zd bytes\n", bytes);
    }

    free(aio.aio_buf);
    close(aio.aio_fildes);
    return 0;
}
```

## Examples

Canceling an AIO operation:

```c
#include <aio.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct aiocb aio = {0};
    aio.aio_fildes = fileno(stdin);
    aio.aio_buf = malloc(1024);
    aio.aio_nbytes = 1024;

    aio_read(&aio);
    aio_cancel(fileno(stdin), &aio);

    int err = aio_error(&aio);
    if (err == ECANCELED) {
        fprintf(stderr, "Read canceled successfully\n");
    }

    free(aio.aio_buf);
    return 0;
}
```

## Related Errors

- [errno-125 ECANCELED]({{< relref "/languages/c/errno-eCANCELED" >}}) — operation canceled (numeric).
- [errno-4 EINTR](/languages/c/errno-eCANCELED/) — interrupted system call.
- [errno-11 EAGAIN](/languages/c/errno-eCANCELED/) — resource unavailable, try again.
