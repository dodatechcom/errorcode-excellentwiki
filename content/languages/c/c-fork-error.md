---
title: "[Solution] C fork() Error — How to Fix"
description: "Fix C fork() errors including resource limits, zombie processes, and file descriptor leaks."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C fork() Error — How to Fix

fork() creates a child process. Common errors include not handling fork failure (returns -1), creating zombie processes by not waiting, and duplicating file descriptors that should be close-on-exec.

## Common Error Messages

- `fork: Resource temporarily unavailable (EAGAIN)`
- `Zombie process from fork without wait`
- `fork: Cannot allocate memory`
- `File descriptor leak in child process`

## How to Fix It

### Check fork return value

```c
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

int main(void) {
    pid_t pid = fork();
    if (pid < 0) {
        perror("fork");
        return 1;
    } else if (pid == 0) {
        printf("Child\n");
        _exit(0);
    } else {
        waitpid(pid, NULL, 0);
        printf("Parent\n");
    }
    return 0;
}
```

### Use waitpid to prevent zombies

```c
#include <unistd.h>
#include <sys/wait.h>
#include <stdio.h>

int main(void) {
    for (int i = 0; i < 3; i++) {
        pid_t pid = fork();
        if (pid == 0) { _exit(0); }
    }
    while (wait(NULL) > 0) {}
    printf("All children reaped\n");
    return 0;
}
```

### Use close-on-exec for inherited fds

```c
#include <fcntl.h>
#include <unistd.h>

int main(void) {
    int fd = open("file.txt", O_RDONLY | O_CLOEXEC);
    pid_t pid = fork();
    if (pid == 0) {
        // fd is auto-closed by O_CLOEXEC
        execlp("ls", "ls", NULL);
    }
    close(fd);
    return 0;
}
```

### Use double-fork to prevent zombies

```c
#include <unistd.h>
#include <sys/wait.h>

void daemonize(void) {
    pid_t pid = fork();
    if (pid > 0) { waitpid(pid, NULL, 0); return; }
    setsid();
    pid = fork();
    if (pid > 0) _exit(0);
}
```

## Common Scenarios

### Scenario 1: fork returns -1 and program continues using invalid pid

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Child processes become zombies without wait/waitpid

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Child inherits all parent file descriptors including sockets

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always check fork return value
- **Tip 2:** Call waitpid or set SIGCHLD handler to reap zombies
- **Tip 3:** Use O_CLOEXEC on file descriptors that should not be inherited
