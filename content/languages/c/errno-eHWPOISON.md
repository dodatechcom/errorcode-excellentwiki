---
title: "[Solution] C errno EHWPOISON — Memory page has hardware error Fix"
description: "Fix C EHWPOISON (Memory page has hardware error) by handling hardware memory errors, replacing DIMMs, and using MCE recovery."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EHWPOISON — Memory page has hardware error Fix

When a process accesses a memory page that has been identified as containing a hardware error (typically uncorrectable ECC errors), the system call fails and sets `errno` to `EHWPOISON`. The kernel has poisoned the page to prevent further corruption.

## Common Causes

- A DIMM module has developed uncorrectable ECC errors.
- The kernel's Machine Check Exception (MCE) handler has poisoned the page.
- The memory page has intermittent hardware faults.
- The hardware is failing and needs replacement.

## How to Fix

Handle the error gracefully. The system logs MCE events — check `mcelog` or `journalctl`. Replace failing hardware.

```bash
# Check for MCE errors
journalctl -k | grep -i "hardware error"
mcelog --client 2>/dev/null

# Check for poisoned pages
cat /proc/meminfo | grep -i poison
```

```c
#include <stdio.h>
#include <errno.h>

int main(void) {
    // When accessing a poisoned memory page
    fprintf(stderr, "Hardware memory error detected (errno %d)\n", EHWPOISON);
    fprintf(stderr, "Check: journalctl -k | grep 'hardware error'\n");
    fprintf(stderr, "The failing DIMM should be replaced\n");
    return 1;
}
```

## Examples

Accessing poisoned memory:

```c
#include <stdio.h>
#include <signal.h>
#include <setjmp.h>
#include <errno.h>

sigjmp_buf jmpbuf;

void bus_error_handler(int sig) {
    siglongjmp(jmpbuf, 1);
}

int main(void) {
    signal(SIGBUS, bus_error_handler);

    if (sigsetjmp(jmpbuf, 1) == 0) {
        // Accessing poisoned memory page triggers SIGBUS
        // and EHWPOISON is set internally
        fprintf(stderr, "Potential hardware memory error\n");
    } else {
        fprintf(stderr, "Hardware error recovered via signal handler\n");
        fprintf(stderr, "errno would be EHWPOISON: %d\n", EHWPOISON);
    }
    return 0;
}
```

## Related Errors

- [errno-133 EHWPOISON]({{< relref "/languages/c/errno-eHWPOISON" >}}) — memory page has hardware error (numeric).
- [errno-5 EIO](/languages/c/errno-eHWPOISON/) — input/output error.
- [errno-12 ENOMEM]({{< relref "/languages/c/errno-enomem" >}}) — cannot allocate memory.
