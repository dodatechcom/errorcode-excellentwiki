---
title: "[Solution] C exec Error — How to Fix"
description: "Fix C exec family (execl, execv, execvp) errors including path resolution and argument passing."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C exec Error — How to Fix

exec replaces the current process. Common errors include not checking return value (exec only returns on failure), passing arguments incorrectly, and forgetting to handle PATH resolution with execvp.

## Common Error Messages

- `exec: No such file or directory`
- `exec: Permission denied`
- `execl: argument list too long (E2BIG)`
- `exec returns — failure not handled`

## How to Fix It

### Check exec return value

```c
#include <unistd.h>
#include <stdio.h>

int main(void) {
    execlp("ls", "ls", "-la", NULL);
    perror("exec failed");  // only reached on error
    return 1;
}
```

### Use execvp for PATH resolution

```c
#include <unistd.h>

int main(void) {
    char *args[] = {"ls", "-la", NULL};
    execvp("ls", args);
    perror("execvp");
    return 1;
}
```

### Pass arguments correctly to exec

```c
#include <unistd.h>

int main(void) {
    char *args[] = {"grep", "-r", "pattern", "/path", NULL};
    execv("/usr/bin/grep", args);
    perror("execv");
    return 1;
}
```

### Use posix_spawn as alternative

```c
#include <spawn.h>
#include <stdio.h>

extern char **environ;

int main(void) {
    pid_t pid;
    char *args[] = {"ls", "-la", NULL};
    if (posix_spawn(&pid, "/usr/bin/ls", NULL, NULL, args, environ) != 0) {
        perror("posix_spawn");
        return 1;
    }
    waitpid(pid, NULL, 0);
    return 0;
}
```

## Common Scenarios

### Scenario 1: exec returns because the program was not found

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Arguments passed incorrectly causing segfault

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Not handling E2BIG from too many arguments

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always check if exec returns — it only returns on failure
- **Tip 2:** Use execvp when you want PATH resolution
- **Tip 3:** Terminate argument list with NULL
