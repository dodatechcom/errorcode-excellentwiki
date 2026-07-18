---
title: "[Solution] C syscall() Error — How to Fix"
description: "Fix C syscall() errors including wrong argument types, EINTR handling, and return value interpretation."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C syscall() Error — How to Fix

syscall() invokes a system call by number. Common errors include wrong argument types (all args should be long), not handling EINTR, and confusing -1 return with errno value.

## Common Error Messages

- `syscall: Invalid argument`
- `syscall returns -1 but errno not set`
- `Wrong argument size passed to syscall`
- `syscall interrupted by signal (EINTR)`

## How to Fix It

### Handle return value correctly

```c
#include <sys/syscall.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>

int main(void) {
    long ret = syscall(SYS_getpid);
    if (ret == -1) {
        perror("syscall");
        return 1;
    }
    printf("PID: %ld\n", ret);
    return 0;
}
```

### Pass correct argument types

```c
#include <sys/syscall.h>
#include <unistd.h>

int main(void) {
    // syscall args must be long
    long ret = syscall(SYS_write, (long)STDOUT_FILENO, (long)"hello\n", (long)6);
    if (ret == -1) perror("syscall");
    return 0;
}
```

### Handle EINTR for interruptible syscalls

```c
#include <sys/syscall.h>
#include <unistd.h>
#include <errno.h>

long syscall_safe(long num, long a1, long a2, long a3) {
    long ret;
    do {
        ret = syscall(num, a1, a2, a3);
    } while (ret == -1 && errno == EINTR);
    return ret;
}
```

### Use wrapper functions instead of raw syscall

```c
#include <unistd.h>
#include <stdio.h>

int main(void) {
    // Prefer wrapper: getpid() instead of syscall(SYS_getpid)
    printf("PID: %d\n", getpid());
    return 0;
}
```

## Common Scenarios

### Scenario 1: Passing int instead of long to syscall arguments

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Not checking errno after syscall returns -1

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Using raw syscall instead of libc wrapper when available

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** All syscall arguments must be cast to long
- **Tip 2:** Check errno after syscall returns -1 for error details
- **Tip 3:** Prefer libc wrappers over raw syscall when available
