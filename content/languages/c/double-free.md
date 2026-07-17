---
title: "[Solution] C Double Free or Corruption — Freeing Already-Freed Memory Fix"
description: "Fix C 'double free or corruption' errors. Learn why freeing the same pointer twice causes heap corruption and how to prevent it."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error", "memory-error"]
weight: 5
---

# [Solution] C Double Free or Corruption — Freeing Already-Freed Memory Fix

A **"double free or corruption"** error occurs when your program attempts to `free()` a pointer that has already been freed, or when it frees a pointer that was never allocated on the heap. This corrupts the heap metadata used by the memory allocator, which can cause crashes, data corruption, or exploitable security vulnerabilities. The error message typically reads `double free or corruption (fasttop)` or `double free or corruption (!prev)`.

## Common Causes

- **Freeing the same pointer twice** — calling `free()` on a pointer without setting it to `NULL` in between
- **Freeing a non-heap pointer** — passing a stack-allocated or global variable to `free()`
- **Freeing an already-freed pointer after reallocation** — a second pointer to the same memory is freed after the first was freed
- **Use-after-free followed by double free** — a dangling pointer is freed again due to a logic error

## How to Fix

### Fix 1: Always set pointers to NULL after freeing

```c
#include <stdlib.h>

int main(void) {
    int *p = malloc(sizeof(int));
    if (p == NULL) return 1;

    *p = 42;
    free(p);
    p = NULL;  /* safe — free(NULL) is a no-op */

    free(p);  /* no crash — free(NULL) does nothing */
    return 0;
}
```

### Fix 2: Use a wrapper or guard to prevent double free

```c
#include <stdlib.h>

void safe_free(void **ptr) {
    if (ptr != NULL && *ptr != NULL) {
        free(*ptr);
        *ptr = NULL;
    }
}

int main(void) {
    int *p = malloc(sizeof(int));
    *p = 10;
    safe_free((void **)&p);  /* frees and sets to NULL */
    safe_free((void **)&p);  /* safe — no-op */
    return 0;
}
```

### Fix 3: Ensure each allocation has exactly one owner

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *name;
} User;

User *user_create(const char *name) {
    User *u = malloc(sizeof(User));
    if (!u) return NULL;
    u->name = strdup(name);  /* strdup allocates — user owns this */
    return u;
}

void user_destroy(User *u) {
    if (u == NULL) return;
    free(u->name);
    free(u);
    /* caller must not use 'u' after this */
}
```

## Examples

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    /* Double free — same pointer freed twice */
    int *a = malloc(sizeof(int));
    *a = 5;
    free(a);
    free(a);  /* ERROR: double free or corruption */

    /* Freeing stack memory */
    int x = 10;
    free(&x);  /* ERROR: free() on non-heap address */

    return 0;
}
```

## Debugging Tips

```bash
# Compile with debug symbols
gcc -g -o myprogram myprogram.c

# Valgrind catches double frees immediately
valgrind --tool=memcheck --track-origins=yes ./myprogram

# AddressSanitizer also detects this
gcc -fsanitize=address -g -o myprogram myprogram.c
./myprogram
```

## Related Errors

- [Heap Corruption Detected]({{< relref "/languages/c/heap-corruption" >}}) — heap metadata written to by an unrelated bug
- [Segmentation Fault (Core Dumped)]({{< relref "/languages/c/segfault" >}}) — crash from accessing invalid memory
- [Use After Free]({{< relref "/languages/c/use-after-free" >}}) — accessing memory after it has been freed
