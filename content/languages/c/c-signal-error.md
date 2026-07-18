---
title: "[Solution] C Signal Handling Error — How to Fix"
description: "Fix C signal handler errors including async-signal-safe functions and handler restrictions."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Signal Handling Error — How to Fix

Signal handlers have strict restrictions: only async-signal-safe functions may be called. Common errors include calling malloc, printf, or mutex lock inside a handler, using global variables without volatile sig_atomic_t, and failing to re-register handlers for SIGILL/SIGSEGV.

## Common Error Messages

- `signal handler called non-async-safe function`
- `Undefined behavior from malloc inside signal handler`
- `Race condition on global flag in signal handler`
- `SIGSEGV handler re-triggered without re-registration`

## How to Fix It

### Use only async-signal-safe functions

```c
#include <signal.h>
#include <unistd.h>

volatile sig_atomic_t got_signal = 0;

void handler(int sig) {
    got_signal = 1;
    const char msg[] = "Signal caught\n";
    write(STDOUT_FILENO, msg, sizeof(msg) - 1);
}

int main(void) {
    signal(SIGINT, handler);
    while (!got_signal) {}
    return 0;
}
```

### Use volatile sig_atomic_t for flags

```c
#include <signal.h>

static volatile sig_atomic_t shutdown_requested = 0;

void sigint_handler(int sig) {
    shutdown_requested = 1;
}

int main(void) {
    signal(SIGINT, sigint_handler);
    while (!shutdown_requested) {
        // do work
    }
    return 0;
}
```

### Re-register handlers for SIG_DFL signals

```c
#include <signal.h>
#include <stdio.h>

void segfault_handler(int sig) {
    fprintf(stderr, "Caught SIGSEGV\n");
    _exit(1);
}

int main(void) {
    struct sigaction sa;
    sa.sa_handler = segfault_handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;
    sigaction(SIGSEGV, &sa, NULL);
    return 0;
}
```

### Use sigaction instead of signal

```c
#include <signal.h>
#include <stdio.h>

void handler(int sig) {
    write(STDOUT_FILENO, "caught\n", 7);
}

int main(void) {
    struct sigaction sa = {
        .sa_handler = handler,
        .sa_flags = SA_RESTART
    };
    sigemptyset(&sa.sa_mask);
    sigaction(SIGINT, &sa, NULL);
    return 0;
}
```

## Common Scenarios

### Scenario 1: Calling printf/malloc inside signal handler

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Global variable modified in handler without volatile sig_atomic_t

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: SIGSEGV handler causes infinite loop when re-triggered

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Only use async-signal-safe functions (write, _exit) in handlers
- **Tip 2:** Use volatile sig_atomic_t for flags shared with handler
- **Tip 3:** Use sigaction with SA_RESTART instead of signal()
