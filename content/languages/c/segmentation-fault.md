---
title: "[Solution] C Segmentation Fault (SIGSEGV) — Memory Access Violation Fix"
description: "Fix C segmentation fault (core dumped) errors with these proven techniques. Debug memory access violations, null pointer dereferences, and buffer overflows."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
tags: ["segfault", "sigsegv", "memory", "null-pointer", "core-dumped"]
weight: 10
---

# [Solution] C Segmentation Fault (SIGSEGV) — Memory Access Violation Fix

A segmentation fault occurs when your C program tries to access memory it is not allowed to touch. The OS sends a `SIGSEGV` signal and terminates the process, often printing "Segmentation fault (core dumped)". This is one of the most common runtime errors in C and almost always indicates a memory bug.

## Common Causes of Segmentation Faults

There are four primary reasons a segmentation fault occurs: null pointer dereference, buffer overflows, stack overflows, and use-after-free.

### 1. Null Pointer Dereference

Dereferencing a pointer that has not been initialized or is set to `NULL` will immediately cause a segfault.

```c
// WRONG — segfault!
#include <stdio.h>

int main(void) {
    int *ptr = NULL;
    printf("%d\n", *ptr); // dereferencing NULL
    return 0;
}
```

**Fix:** Always validate pointers before use.

```c
// CORRECT
#include <stdio.h>

int main(void) {
    int *ptr = NULL;
    if (ptr != NULL) {
        printf("%d\n", *ptr);
    } else {
        printf("ptr is NULL, skipping dereference\n");
    }
    return 0;
}
```

### 2. Buffer Overflow

Writing past the end of an allocated array corrupts adjacent memory and causes a segfault.

```c
// WRONG — buffer overflow
#include <stdio.h>

int main(void) {
    int arr[5];
    arr[10] = 42; // index 10 is out of bounds
    return 0;
}
```

**Fix:** Always keep array indices within bounds.

```c
// CORRECT
#include <stdio.h>

int main(void) {
    int arr[5];
    int index = 10;
    if (index >= 0 && index < 5) {
        arr[index] = 42;
    } else {
        printf("Index %d is out of bounds\n", index);
    }
    return 0;
}
```

### 3. Stack Overflow (Deep Recursion)

Extremely deep recursion can exhaust the stack, causing a segfault.

```c
// WRONG — infinite recursion
void recurse(void) {
    recurse(); // no base case
}
```

**Fix:** Always define a proper base case.

```c
// CORRECT
void recurse(int n) {
    if (n <= 0) return; // base case
    recurse(n - 1);
}
```

### 4. Use-After-Free

Accessing memory after it has been `free()`d leads to undefined behavior and possible segfaults.

```c
// WRONG — use-after-free
#include <stdlib.h>

int main(void) {
    int *p = malloc(sizeof(int));
    *p = 10;
    free(p);
    printf("%d\n", *p); // accessing freed memory
    return 0;
}
```

**Fix:** Set pointers to `NULL` after freeing and never access freed memory.

```c
// CORRECT
#include <stdlib.h>
#include <stdio.h>

int main(void) {
    int *p = malloc(sizeof(int));
    *p = 10;
    free(p);
    p = NULL; // safe — any future dereference is caught
    return 0;
}
```

## How to Debug Segmentation Faults

### Use GDB to Find the Exact Line

Compile with debug symbols and use `gdb` to pinpoint the crash location:

```bash
gcc -g -o myprogram myprogram.c
gdb ./myprogram
```

Inside GDB, run `run` and when it crashes, use `backtrace` (or `bt`) to see the call stack:

```
(gdb) run
Program received signal SIGSEGV, Segmentation fault.
0x0000555555555149 in main () at myprogram.c:5
5:      printf("%d\n", *ptr);
(gdb) bt
#0  0x0000555555555149 in main () at myprogram.c:5
```

### Use Valgrind to Detect Memory Errors

Valgrind catches null dereferences, buffer overflows, use-after-free, and memory leaks at runtime:

```bash
gcc -g -o myprogram myprogram.c
valgrind --leak-check=full ./myprogram
```

Valgrind will report the exact line and type of memory error.

## Summary of Fixes

| Cause | Prevention |
|---|---|
| Null pointer | Check `ptr != NULL` before dereferencing |
| Buffer overflow | Validate all array indices before access |
| Stack overflow | Add a base case to every recursive function |
| Use-after-free | Set pointers to `NULL` after `free()` |
| Uninitialized pointer | Initialize every pointer at declaration |

## Best Practices

- Compile with `-Wall -Wextra -g` to enable warnings and debug symbols.
- Use `valgrind` regularly during development.
- Prefer `calloc` over `malloc` to zero-initialize memory.
- Use static analysis tools like `cppcheck` or `clang-tidy`.
- Never ignore compiler warnings about uninitialized variables.
