---
title: "[Solution] C wait / waitpid Error — How to Fix"
description: "Fix C wait() and waitpid() errors including zombie processes, EINTR, and exit status handling."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C wait / waitpid Error — How to Fix

wait/waitpid collect child process exit status. Common errors include not calling wait (zombie processes), using WEXITSTATUS incorrectly, and not handling EINTR from signal interruption during wait.

## Common Error Messages

- `Zombie process — wait never called`
- `waitpid: No child processes (ECHILD)`
- `Incorrect exit status from WEXITSTATUS`
- `wait interrupted by signal (EINTR)`

## How to Fix It

### Always call waitpid for specific children

```c
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>

int main(void) {
    pid_t pid = fork();
    if (pid == 0) { _exit(42); }
    int status;
    waitpid(pid, &status, 0);
    if (WIFEXITED(status))
        printf("Exit status: %d\n", WEXITSTATUS(status));
    return 0;
}
```

### Handle EINTR during wait

```c
#include <sys/wait.h>
#include <errno.h>
#include <unistd.h>

pid_t wait_safe(pid_t pid, int *status, int options) {
    pid_t ret;
    do {
        ret = waitpid(pid, status, options);
    } while (ret == -1 && errno == EINTR);
    return ret;
}
```

### Use WNOHANG for non-blocking wait

```c
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>

int main(void) {
    pid_t pid = fork();
    if (pid == 0) { _exit(0); }
    int status;
    pid_t result;
    do {
        result = waitpid(pid, &status, WNOHANG);
    } while (result == 0);
    printf("Child exited\n");
    return 0;
}
```

### Use waitid for detailed info

```c
#include <sys/wait.h>
#include <stdio.h>

int main(void) {
    siginfo_t info;
    if (waitid(P_ALL, 0, &info, WEXITED) == 0)
        printf("Child %d exited with status %d\n", info.si_pid, info.si_status);
    return 0;
}
```

## Common Scenarios

### Scenario 1: Not calling wait causing zombie accumulation

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Using WEXITSTATUS without checking WIFEXITED first

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Blocking in wait while signal handler needs to run

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always waitpid for child processes you create
- **Tip 2:** Check WIFEXITED before using WEXITSTATUS
- **Tip 3:** Use WNOHANG or handle EINTR in signal-heavy programs
