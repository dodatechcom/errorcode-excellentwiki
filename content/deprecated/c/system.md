---
title: "[Solution] C system() Deprecated — Replace with exec Family"
description: "Replace system() with exec family functions in C for security and reliability. Migration guide with code examples."
deprecated_function: "system"
replacement_function: "exec family"
languages: ["c"]
error-types: ["deprecated"]
severities: ["warning"]
weight: 5
---

# [Solution] C system() Deprecated — Replace with exec Family

The `system()` function is deprecated in secure coding guidelines because it invokes a shell to execute commands, making it vulnerable to shell injection attacks. If any part of the command string comes from user input, an attacker can inject arbitrary commands. The safe replacement is the `exec` family of functions, which execute programs directly without a shell.

## What You'll See

Compiler warnings with security flags:

```
warning: 'system' is deprecated: use exec family or posix_spawn() instead
```

On MSVC:

```
warning C4996: 'system': This function or variable may be unsafe. Consider using _execl or execv instead.
```

## Why Deprecated

`system()` is deprecated because:

- **Shell injection**: User input is passed through a shell, allowing command injection.
- **No process control**: You cannot control environment variables, file descriptors, or signal handling.
- **Shell-dependent**: Behavior varies between `/bin/sh`, `bash`, `cmd.exe`, etc.
- **Overhead**: Spawning a shell for every command is expensive.
- **Security bypass**: Even with input sanitization, injection is hard to prevent completely.

## Old Code (Deprecated)

```c
#include <stdio.h>
#include <stdlib.h>

int list_directory(const char *path) {
    char command[256];
    snprintf(command, sizeof(command), "ls -la %s", path);  // INJECTABLE
    return system(command);  // DANGEROUS — shell injection
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <directory>\n", argv[0]);
        return 1;
    }

    if (list_directory(argv[1]) != 0) {
        fprintf(stderr, "Command failed\n");
        return 1;
    }

    return 0;
}
```

## New Code — execvp() Replacement

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int list_directory(const char *path) {
    pid_t pid = fork();

    if (pid == -1) {
        perror("fork");
        return -1;
    }

    if (pid == 0) {
        // Child process — exec ls directly, no shell
        execlp("ls", "ls", "-la", path, NULL);
        perror("execlp");  // Only reaches here if exec fails
        _exit(1);
    }

    // Parent process — wait for child
    int status;
    waitpid(pid, &status, 0);

    if (WIFEXITED(status)) {
        return WEXITSTATUS(status);
    }
    return -1;
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <directory>\n", argv[0]);
        return 1;
    }

    return list_directory(argv[1]);
}
```

## New Code — posix_spawn() (Portable)

```c
#include <stdio.h>
#include <stdlib.h>
#include <spawn.h>
#include <sys/wait.h>

extern char **environ;

int run_command(const char *path, const char *const args[]) {
    pid_t pid;
    posix_spawnattr_t attr;
    posix_spawnattr_init(&attr);

    if (posix_spawn(&pid, path, NULL, &attr, (char *const *)args, environ) != 0) {
        perror("posix_spawn");
        posix_spawnattr_destroy(&attr);
        return -1;
    }

    posix_spawnattr_destroy(&attr);

    int status;
    waitpid(pid, &status, 0);

    if (WIFEXITED(status)) {
        return WEXITSTATUS(status);
    }
    return -1;
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <directory>\n", argv[0]);
        return 1;
    }

    const char *args[] = {"ls", "-la", argv[1], NULL};
    return run_command("/bin/ls", args);
}
```

## Migration Steps

1. **Find all system() calls**:

```bash
grep -rn "\bsystem\s*(" --include="*.c" /path/to/project/
```

2. **Identify user input** in command strings — these are injection vulnerabilities.

3. **Replace `system(cmd)` with `fork()` + `execvp()`** for simple command execution.

4. **Use `posix_spawn()`** if you need portable process creation or fine-grained control.

5. **Pass arguments as an array**, not a single string — this avoids shell parsing entirely.

6. **For popen() replacements**, use `fork()` + `exec()` + `pipe()`.

7. **Never construct command strings from user input** — use argument arrays instead.

## Related Deprecations

- [getenv → secure_getenv]({{< relref "/deprecated/c/getenv" >}}) — environment variable access.
- [tmpnam → mkstemp]({{< relref "/deprecated/c/tmpnam" >}}) — temp file race conditions.
- [gets → fgets]({{< relref "/deprecated/c/gets" >}}) — unsafe input handling.
