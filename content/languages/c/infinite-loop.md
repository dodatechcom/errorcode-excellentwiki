---
title: "[Solution] C Infinite Loop — CPU 100% / Program Not Responding Fix"
description: "Fix C infinite loops that cause CPU 100% usage. Identify missing break conditions, off-by-one errors, and blocking loops in C programs."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["infinite-loop", "cpu-100", "busy-wait", "hang", "not-responding", "deadlock"]
weight: 5
---

# [Solution] C Infinite Loop — CPU 100% / Program Not Responding Fix

An **infinite loop** occurs when a `while`, `for`, or `do-while` loop has no reachable exit condition, causing the program to consume 100% CPU indefinitely and become unresponsive. Unlike memory errors, infinite loops do not crash — they silently consume all available CPU time, making the program appear frozen.

## Common Causes

- **Missing or unreachable break condition** — the loop's exit condition is never satisfied
- **Off-by-one error in loop bounds** — the loop variable never reaches the termination value
- **Infinite recursion converted to a loop** — a `while(1)` without proper exit logic
- **Blocking I/O inside a loop** — the loop itself is fine but a blocking call never returns

## How to Fix

### Fix 1: Ensure every loop has a reachable exit condition

```c
#include <stdio.h>

int main(void) {
    int i = 0;

    /* WRONG — i is never incremented, loops forever */
    while (i < 10) {
        printf("%d\n", i);
    }

    /* CORRECT */
    while (i < 10) {
        printf("%d\n", i);
        i++;
    }
    return 0;
}
```

### Fix 2: Check for correct loop variable updates

```c
#include <stdio.h>

int main(void) {
    int count = 0;

    /* WRONG — condition uses wrong variable */
    while (count < 100) {
        printf("working...\n");
        /* forgot: count++ */
    }

    /* CORRECT */
    while (count < 100) {
        printf("working...\n");
        count++;
    }
    return 0;
}
```

### Fix 3: Add a timeout or iteration limit

```c
#include <stdio.h>
#include <time.h>
#include <stdbool.h>

bool wait_for_event(int max_iterations) {
    int iterations = 0;
    while (iterations < max_iterations) {
        /* check for event */
        if (/* event occurred */) {
            return true;
        }
        iterations++;
    }
    fprintf(stderr, "Timeout: no event after %d iterations\n", max_iterations);
    return false;
}
```

### Fix 4: Use non-blocking I/O in event loops

```c
#include <stdio.h>
#include <stdbool.h>
#include <unistd.h>
#include <fcntl.h>

int main(void) {
    int fd = open("/dev/input/event0", O_RDONLY | O_NONBLOCK);
    if (fd < 0) return 1;

    while (true) {
        char buf[64];
        ssize_t n = read(fd, buf, sizeof(buf));
        if (n > 0) {
            /* process event */
        } else if (n == -1 && (errno == EAGAIN || errno == EWOULDBLOCK)) {
            /* no data available — do other work or sleep briefly */
            usleep(10000);  /* 10ms to avoid spinning */
        }
    }

    close(fd);
    return 0;
}
```

## Examples

```c
#include <stdio.h>

/* Infinite loop: loop condition never changes */
void broken1(void) {
    int x = 0;
    while (x != 10) {
        x += 2;  /* x goes 0, 2, 4, 6, 8, 10... actually terminates */
    }
}

/* Infinite loop: x overflows */
void broken2(void) {
    unsigned int x = 0;
    while (x < 100) {
        x += 2000000000;  /* wraps around, never reaches < 100 in a stable way */
    }
}

/* Infinite loop: missing break */
void broken3(void) {
    int found = 0;
    while (!found) {
        /* search for something but never set found = 1 */
    }
}
```

## Debugging Tips

```bash
# Run the program and send SIGINT (Ctrl+C) to interrupt the loop
# Get a backtrace with GDB
gcc -g -o myprogram myprogram.c
gdb ./myprogram
# (gdb) run
# When hung, press Ctrl+C
# (gdb) bt    # shows which loop you're stuck in

# Use 'top' or 'htop' to identify the hung process
top -p $(pgrep myprogram)
```

## Related Errors

- [Segmentation Fault (Core Dumped)]({{< relref "/languages/c/segfault" >}}) — crashes from memory errors (infinite loops do not crash)
- [Stack Overflow: Deep Recursion]({{< relref "/languages/c/segfault" >}}) — unbounded recursion is a form of infinite call loop
- [Double Free or Corruption]({{< relref "/languages/c/double-free" >}}) — sometimes infinite loops trigger cleanup bugs
