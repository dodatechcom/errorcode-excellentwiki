---
title: "[Solution] C Memory Leak — Valgrind Lost Bytes / Still Reachable Fix"
description: "Fix C memory leaks detected by Valgrind. Understand 'definitely lost', 'indirectly lost', and 'still reachable' reports and eliminate them."
languages: ["c"]
severities: ["error"]
error-types: ["memory-error"]
weight: 5
---

# [Solution] C Memory Leak — Valgrind Lost Bytes / Still Reachable Fix

A **memory leak** occurs when your program allocates heap memory (via `malloc`, `calloc`, or `realloc`) but fails to `free()` it before the pointer is lost. Valgrind reports this as `"definitely lost: N bytes in M blocks"` or `"still reachable: N bytes"`. While small leaks may be harmless in short-lived programs, large or repeated leaks exhaust memory and cause performance degradation or crashes.

## Common Causes

- **Allocating in a loop without freeing** — each iteration creates a new allocation but the old one is never released
- **Overwriting a pointer** — the original address is lost before `free()` is called
- **Error paths that skip cleanup** — `return` statements before the `free()` call
- **Global or static buffers never freed** — intentional in some cases but often a bug

## How to Fix

### Fix 1: Free memory at every exit path

```c
#include <stdlib.h>
#include <stdio.h>

int process_data(const char *input) {
    char *buffer = malloc(1024);
    if (buffer == NULL) return -1;

    /* If an error occurs early, make sure to free buffer first */
    if (input == NULL) {
        free(buffer);
        return -1;
    }

    /* ... process ... */
    free(buffer);
    return 0;
}
```

### Fix 2: Use goto cleanup pattern for complex functions

```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int complex_function(const char *input) {
    int result = -1;
    char *buf1 = NULL;
    char *buf2 = NULL;
    FILE *fp = NULL;

    buf1 = malloc(256);
    if (buf1 == NULL) goto cleanup;

    buf2 = malloc(256);
    if (buf2 == NULL) goto cleanup;

    fp = fopen("output.txt", "w");
    if (fp == NULL) goto cleanup;

    /* ... do work ... */
    result = 0;

cleanup:
    if (fp) fclose(fp);
    free(buf2);
    free(buf1);
    return result;
}
```

### Fix 3: Free in loops to prevent repeated leaks

```c
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    for (int i = 0; i < argc; i++) {
        char *copy = malloc(strlen(argv[i]) + 1);
        if (copy == NULL) continue;
        strcpy(copy, argv[i]);
        printf("Arg %d: %s\n", i, copy);
        free(copy);  /* free each iteration */
    }
    return 0;
}
```

### Fix 4: Free before overwriting pointers

```c
#include <stdlib.h>
#include <string.h>

void update_name(char **name, const char *new_name) {
    /* WRONG — original allocation is leaked */
    /* *name = strdup(new_name); */

    /* CORRECT — free old allocation first */
    free(*name);
    *name = strdup(new_name);
}
```

## Valgrind Output Explained

```bash
valgrind --leak-check=full ./myprogram
```

```
==12345== LEAK SUMMARY:
==12345==   definitely lost: 100 bytes in 5 blocks    ← must fix
==12345==   indirectly lost: 40 bytes in 2 blocks     ← lost via a leaked pointer
==12345==     possibly lost: 20 bytes in 1 blocks     ← may be reachable through a pointer
==12345==   still reachable: 16 bytes in 1 blocks     ← intentionally not freed (e.g., global)
==12345==        suppressed: 0 bytes in 0 blocks
```

## Examples

```c
#include <stdlib.h>
#include <string.h>

/* Leak 1: Lost pointer — allocation cannot be freed */
void leak1(void) {
    int *p = malloc(sizeof(int) * 100);
    p = NULL;  /* leak: original address is lost */
}

/* Leak 2: Early return skips free() */
int leak2(void) {
    char *buf = malloc(1024);
    if (/* error condition */) return -1;  /* leak: buf not freed */
    free(buf);
    return 0;
}

/* Leak 3: realloc that fails — original pointer is lost */
void leak3(void) {
    int *p = malloc(sizeof(int) * 10);
    int *q = realloc(p, sizeof(int) * 1000000);
    /* if realloc fails, q is NULL but p is still valid — p is now leaked */
}
```

## Related Errors

- [Use After Free]({{< relref "/languages/c/use-after-free" >}}) — accessing memory after freeing it
- [Heap Corruption Detected]({{< relref "/languages/c/heap-corruption" >}}) — heap metadata overwritten
- [Double Free or Corruption]({{< relref "/languages/c/double-free" >}}) — freeing the same pointer twice
