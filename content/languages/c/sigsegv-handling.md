---
title: "[Solution] C SIGSEGV — Segmentation fault handling"
description: "Fix and handle SIGSEGV segmentation faults by installing signal handlers, using sigaction, and enabling SA_SIGINFO for detailed diagnostics. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 826
---

# C SIGSEGV — Segmentation fault handling

SIGSEGV (Segmentation Fault) is delivered when a program performs an invalid memory access — dereferencing NULL, accessing freed memory, reading beyond array bounds, or writing to read-only memory. While the best fix is preventing the fault, signal handlers can provide diagnostics and graceful recovery.

## Common Causes

```c
// Cause 1: Dereferencing NULL pointer
int *p = NULL;
int val = *p;  // SIGSEGV
```

```c
// Cause 2: Accessing freed memory
char *buf = malloc(100);
free(buf);
strcpy(buf, "use after free");  // SIGSEGV likely
```

```c
// Cause 3: Stack overflow from deep recursion
void infinite(void) {
    char waste[1024];
    infinite();  // SIGSEGV when stack runs out
}
```

```c
// Cause 4: Writing to read-only memory (const data)
char *str = "hello";
str[0] = 'H';  // SIGSEGV: string literal is in read-only memory
```

```c
// Cause 5: Buffer overflow corrupting memory
char small[4];
strcpy(small, "this string is way too long");  // SIGSEGV from stack corruption
```

## How to Fix

### Fix 1: Prevent NULL pointer dereferences

```c
#include <stddef.h>

int safe_deref(const int *ptr) {
    if (ptr == NULL) {
        return -1;  // handle gracefully
    }
    return *ptr;
}
```

### Fix 2: Install a signal handler for diagnostics

```c
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>

void sigsegv_handler(int sig, siginfo_t *info, void *context) {
    (void)sig;
    (void)context;
    fprintf(stderr, "SIGSEGV: faulting address = %p\n", info->si_addr);
    _exit(1);
}

int main(void) {
    struct sigaction sa;
    sa.sa_sigaction = sigsegv_handler;
    sa.sa_flags = SA_SIGINFO;
    sigemptyset(&sa.sa_mask);
    sigaction(SIGSEGV, &sa, NULL);

    // Now crashes will print the faulting address
    int *p = NULL;
    *p = 42;  // prints "SIGSEGV: faulting address = (nil)" instead of just crashing
    return 0;
}
```

### Fix 3: Use guard pages and stack limits

```c
#include <sys/resource.h>
#include <stdio.h>

int main(void) {
    // Set stack size limit
    struct rlimit rl;
    rl.rlim_cur = 8 * 1024 * 1024;  // 8MB stack
    rl.rlim_max = 8 * 1024 * 1024;
    setrlimit(RLIMIT_STACK, &rl);

    return 0;
}
```

### Fix 4: Use memory debugging tools

```bash
# Valgrind — catches most memory errors
valgrind --tool=memcheck --leak-check=full ./app

# AddressSanitizer — fast, built into compiler
gcc -fsanitize=address -g main.c -o app
./app

# Electric Fence — lightweight malloc debugger
gcc -lefence main.c -o app
./app
```

### Fix 5: Write defensive code with bounds checking

```c
#include <stddef.h>

int array_get(const int *arr, size_t size, size_t index) {
    if (arr == NULL || index >= size) {
        return -1;  // out of bounds
    }
    return arr[index];
}

int array_set(int *arr, size_t size, size_t index, int value) {
    if (arr == NULL || index >= size) {
        return -1;
    }
    arr[index] = value;
    return 0;
}
```

## Examples

```c
// Real-world: signal handler for crash reporting
#define _GNU_SOURCE
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <ucontext.h>

static void crash_handler(int sig, siginfo_t *info, void *ucontext) {
    ucontext_t *uc = (ucontext_t *)ucontext;
    void *fault_addr = info->si_addr;

    fprintf(stderr, "=== CRASH REPORT ===\n");
    fprintf(stderr, "Signal: %d (SIGSEGV)\n", sig);
    fprintf(stderr, "Fault address: %p\n", fault_addr);

#if defined(__x86_64__)
    fprintf(stderr, "RIP: 0x%llx\n", (unsigned long long)uc->uc_mcontext.gregs[REG_RIP]);
    fprintf(stderr, "RSP: 0x%llx\n", (unsigned long long)uc->uc_mcontext.gregs[REG_RSP]);
#endif

    fprintf(stderr, "===================\n");
    _exit(1);
}

void install_crash_handler(void) {
    struct sigaction sa;
    sa.sa_sigaction = crash_handler;
    sa.sa_flags = SA_SIGINFO | SA_RESETHAND;
    sigemptyset(&sa.sa_mask);
    sigaction(SIGSEGV, &sa, NULL);
}
```

```c
// Real-world: safe linked list with NULL checks
struct Node {
    int data;
    struct Node *next;
};

int list_get(const struct Node *head, size_t index, int *result) {
    const struct Node *current = head;
    for (size_t i = 0; i < index; i++) {
        if (current == NULL) return -1;  // prevent SIGSEGV
        current = current->next;
    }
    if (current == NULL) return -1;
    *result = current->data;
    return 0;
}
```

## Related Errors

- [C USE_AFTER_FREE_C](/languages/c/use-after-free-c) — Use after free UB
- [C NULL_POINTER_ARITHMETIC](/languages/c/null-pointer-arithmetic) — Null pointer arithmetic UB
- [C RETURN_LOCAL_ADDRESS](/languages/c/return-local-address) — Returning address of local variable
