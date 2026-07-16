---
title: "[Solution] C Segmentation Fault (Core Dumped) — SIGSEGV Memory Access Violation Fix"
description: "Fix C segmentation fault (core dumped) with proven techniques. Debug null pointer dereferences, buffer overflows, and invalid memory access errors."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error", "memory-error"]
tags: ["segfault", "sigsegv", "core-dumped", "memory-access", "null-pointer", "signal-11"]
weight: 5
---

# [Solution] C Segmentation Fault (Core Dumped) — SIGSEGV Memory Access Violation Fix

A segmentation fault (often printed as **"Segmentation fault (core dumped)"**) occurs when a C program attempts to access memory that it is not permitted to read or write. The operating system sends a `SIGSEGV` signal (signal 11) and terminates the process immediately. This is one of the most common and dangerous errors in C programming, and it almost always points to a memory management bug.

## Common Causes

- **Null pointer dereference** — dereferencing a `NULL` or uninitialized pointer
- **Buffer overflow** — writing past the end of an allocated array or buffer
- **Stack overflow** — excessively deep recursion exhausting the call stack
- **Use-after-free** — accessing memory after it has been freed

## How to Fix

### Fix 1: Always check pointers before dereferencing

```c
#include <stdio.h>

int main(void) {
    int *ptr = NULL;
    if (ptr != NULL) {
        printf("%d\n", *ptr);
    } else {
        printf("ptr is NULL\n");
    }
    return 0;
}
```

### Fix 2: Validate array indices

```c
#include <stdio.h>

int main(void) {
    int arr[5] = {10, 20, 30, 40, 50};
    int index = 10;
    if (index >= 0 && index < 5) {
        printf("%d\n", arr[index]);
    } else {
        printf("Index %d is out of bounds (size 5)\n", index);
    }
    return 0;
}
```

### Fix 3: Set pointers to NULL after freeing

```c
#include <stdlib.h>
#include <stdio.h>

int main(void) {
    int *p = malloc(sizeof(int));
    *p = 10;
    free(p);
    p = NULL;  /* prevents accidental use-after-free */
    return 0;
}
```

### Fix 4: Add a base case to recursive functions

```c
/* WRONG — infinite recursion causes stack overflow (segfault) */
void recurse(void) {
    recurse();
}

/* CORRECT */
void recurse(int n) {
    if (n <= 0) return;
    recurse(n - 1);
}
```

## Examples

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    /* Example 1: Null pointer dereference */
    char *str = NULL;
    printf("%c\n", str[0]);  /* segfault */

    /* Example 2: Buffer overflow */
    int buf[3];
    buf[5] = 42;  /* segfault — writes outside allocated memory */

    /* Example 3: Use-after-free */
    int *data = malloc(sizeof(int) * 10);
    free(data);
    data[0] = 1;  /* segfault — accessing freed memory */

    return 0;
}
```

## Debugging Tips

```bash
# Compile with debug symbols
gcc -g -o myprogram myprogram.c

# Use GDB to find the exact crash location
gdb ./myprogram
# (gdb) run
# (gdb) bt          # backtrace shows the call stack

# Use Valgrind to detect the memory bug
valgrind --leak-check=full ./myprogram
```

## Related Errors

- [Double Free or Corruption]({{< relref "/languages/c/double-free" >}}) — freeing the same memory twice
- [Heap Corruption Detected]({{< relref "/languages/c/heap-corruption" >}}) — writing to freed or invalid heap memory
- [Buffer Overflow: Stack Smashing]({{< relref "/languages/c/buffer-overflow" >}}) — stack canary corruption detected
