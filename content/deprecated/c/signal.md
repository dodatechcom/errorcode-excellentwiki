---
title: "[Solution] C signal() Deprecated — Replace with sigaction()"
description: "Replace signal() with sigaction() in C for reliable signal handling. Migration guide with code examples."
deprecated_function: "signal"
replacement_function: "sigaction"
languages: ["c"]
error-types: ["deprecated"]
severities: ["warning"]
weight: 5
---

# [Solution] C signal() Deprecated — Replace with sigaction()

The `signal()` function is deprecated in POSIX because its behavior is unreliable and implementation-defined. When a signal handler is invoked, the handler disposition may be reset to `SIG_DFL`, requiring the handler to re-register itself — creating a race condition. `sigaction()` provides explicit control over signal behavior and is the recommended replacement.

## What You'll See

Compiler warnings with strict POSIX compliance flags:

```
warning: 'signal' is deprecated: use sigaction() for reliable signal handling
```

## Why Deprecated

`signal()` is deprecated because:

- **Handler reset race**: After the handler runs, the disposition may reset to `SIG_DFL`. Before the handler re-registers itself, another signal of the same type can kill the process.
- **Implementation-defined behavior**: The standard allows different systems to handle `signal()` differently, making behavior non-portable.
- **No control over signal blocking**: You cannot specify which signals are blocked during handler execution.
- **No way to detect if handler was interrupted**: No `SA_RESTART` or `SA_NODEFER` options.

## Old Code (Deprecated)

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handler(int sig) {
    printf("Caught signal %d\n", sig);
    // Must re-register the handler — race condition!
    signal(SIGINT, handler);
}

int main(void) {
    signal(SIGINT, handler);  // UNRELIABLE

    while (1) {
        printf("Running...\n");
        sleep(1);
    }
    return 0;
}
```

## New Code — sigaction() Replacement

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handler(int sig, siginfo_t *info, void *context) {
    printf("Caught signal %d from PID %d\n", sig, info->si_pid);
}

int main(void) {
    struct sigaction sa;
    sa.sa_sigaction = handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = SA_SIGINFO | SA_RESTART;  // Get signal info, restart interrupted syscalls

    if (sigaction(SIGINT, &sa, NULL) == -1) {
        perror("sigaction");
        return 1;
    }

    while (1) {
        printf("Running...\n");
        sleep(1);
    }
    return 0;
}
```

## New Code — Signal Mask Control

```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

volatile sig_atomic_t got_signal = 0;

void handler(int sig) {
    got_signal = 1;
}

int main(void) {
    struct sigaction sa;
    sa.sa_handler = handler;
    sigemptyset(&sa.sa_mask);
    sigaddset(&sa.sa_mask, SIGTERM);  // Block SIGTERM while handler runs
    sa.sa_flags = SA_RESTART;

    sigaction(SIGINT, &sa, NULL);
    sigaction(SIGTERM, &sa, NULL);

    while (!got_signal) {
        pause();  // Wait for a signal
    }

    printf("Received signal, cleaning up...\n");
    return 0;
}
```

## Migration Steps

1. **Find all signal() calls**:

```bash
grep -rn "\bsignal\s*(" --include="*.c" /path/to/project/
```

2. **Create a `struct sigaction`** and set `sa_handler` (or `sa_sigaction` for extended info).

3. **Call `sigemptyset(&sa.sa_mask)`** to initialize the signal mask.

4. **Set `sa.flags`** — use `SA_RESTART` to restart interrupted syscalls, `SA_SIGINFO` for extended signal info.

5. **Replace `signal(sig, handler)` with `sigaction(sig, &sa, NULL)`**.

6. **Remove any re-registration** inside the handler — `sigaction()` does not reset the handler.

7. **For signals that must not be interrupted**, use `sigprocmask()` to control signal blocking.

## Related Deprecations

- [setjmp/longjmp → C++ exceptions]({{< relref "/deprecated/c/setjmp" >}}) — non-local goto alternatives.
- [exit → atexit cleanup]({{< relref "/deprecated/c/exit" >}}) — cleanup alternatives.
- [abort → proper error handling]({{< relref "/deprecated/c/abort" >}}) — graceful error recovery.
