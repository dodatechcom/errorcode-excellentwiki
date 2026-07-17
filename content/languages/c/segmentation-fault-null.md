---
title: "[Solution] C Segfault: NULL Pointer Dereference"
description: "Fix C segmentation fault from NULL pointer dereference. Learn to detect and prevent null pointer crashes."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["segfault", "null-pointer", "dereference", "sigsegv", "core-dumped"]
weight: 5
---

# Segfault: NULL Pointer Dereference

A NULL pointer dereference occurs when your program attempts to read or write memory through a pointer that is `NULL`. The operating system delivers a `SIGSEGV` signal, terminating the program with a segmentation fault.

## Common Causes

```c
// Cause 1: Dereferencing uninitialized pointer
int *ptr;
*ptr = 10; // segfault — ptr is uninitialized

// Cause 2: Dereferencing NULL explicitly
int *ptr = NULL;
printf("%d\n", *ptr); // segfault

// Cause 3: Failed malloc return
int *buf = malloc(100 * sizeof(int));
// malloc may return NULL if out of memory
*buf = 42; // segfault if malloc failed

// Cause 4: Function returning NULL
char *str = getenv("NONEXISTENT_VAR");
printf("%c\n", str[0]); // segfault if getenv returns NULL
```

## How to Fix

### Fix 1: Check pointers before use

```c
int *ptr = get_pointer();
if (ptr != NULL) {
    printf("%d\n", *ptr);
} else {
    fprintf(stderr, "pointer is NULL\n");
}
```

### Fix 2: Check malloc return value

```c
int *buf = malloc(100 * sizeof(int));
if (buf == NULL) {
    perror("malloc");
    return 1;
}
```

### Fix 3: Initialize pointers

```c
int *ptr = NULL; // explicitly set to NULL
// ... later
ptr = &some_variable; // now safe to use
```

### Fix 4: Use static analysis

```bash
gcc -Wall -Wextra -g -o myprogram myprogram.c
valgrind --tool=memcheck ./myprogram
```

## Examples

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *a = NULL;
    int *b = malloc(sizeof(int));
    
    // Safe: check before use
    if (a != NULL) {
        printf("a: %d\n", *a);
    }
    
    // Safe: check malloc
    if (b != NULL) {
        *b = 42;
        printf("b: %d\n", *b);
        free(b);
    }
    
    return 0;
}
```

## Related Errors

- [Segmentation fault: address 0x0]({{< relref "/languages/c/segmentation-fault-0" >}}) — similar segfault variant.
- [NULL pointer dereference]({{< relref "/languages/c/null-pointer-dereference" >}}) — detailed null pointer analysis.
- [Use after free]({{< relref "/languages/c/use-after-free-heap" >}}) — accessing freed memory.
