---
title: "[Solution] C dup2() Error — How to Fix"
description: "Fix C dup2() file descriptor redirection errors for I/O redirection and subprocess management."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C dup2() Error — How to Fix

dup2() duplicates a file descriptor to a specific number. Common errors include not closing the target fd before dup2 (fd leak), using invalid fd numbers, and not handling the case where dup2 fails.

## Common Error Messages

- `dup2: Bad file descriptor`
- `dup2: Invalid argument — negative fd`
- `File descriptor leak from not closing original`
- `dup2: Too many open files`

## How to Fix It

### Close target fd before dup2

```c
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

int redirect_stdout(const char *path) {
    int fd = open(path, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd == -1) return -1;
    close(STDOUT_FILENO);  // close original stdout
    if (dup2(fd, STDOUT_FILENO) == -1) {
        close(fd);
        return -1;
    }
    close(fd);
    return 0;
}
```

### Use dup2 in pipe redirection

```c
#include <unistd.h>
#include <stdio.h>

int main(void) {
    int pipefd[2];
    pipe(pipefd);
    pid_t pid = fork();
    if (pid == 0) {
        close(pipefd[1]);
        dup2(pipefd[0], STDIN_FILENO);
        close(pipefd[0]);
        execlp("cat", "cat", NULL);
        perror("exec");
    } else {
        close(pipefd[0]);
        write(pipefd[1], "hello", 5);
        close(pipefd[1]);
    }
    return 0;
}
```

### Save and restore original fd

```c
#include <unistd.h>
#include <stdio.h>

int main(void) {
    int saved_stdout = dup(STDOUT_FILENO);
    int fd = open("/dev/null", O_WRONLY);
    dup2(fd, STDOUT_FILENO);
    close(fd);
    printf("This goes nowhere\n");
    dup2(saved_stdout, STDOUT_FILENO);
    close(saved_stdout);
    printf("This goes to terminal\n");
    return 0;
}
```

### Use dup2 for subprocess I/O redirection

```c
#include <unistd.h>
#include <fcntl.h>

void redirect_to_file(const char *path, int target_fd) {
    int fd = open(path, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd != -1) {
        dup2(fd, target_fd);
        close(fd);
    }
}
```

## Common Scenarios

### Scenario 1: dup2 without closing original fd causes descriptor leak

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Using negative fd number causes EINVAL

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Not handling dup2 failure in error path

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Close the target fd before calling dup2
- **Tip 2:** Always check dup2 return value
- **Tip 3:** Save and restore fds when temporary redirection is needed
