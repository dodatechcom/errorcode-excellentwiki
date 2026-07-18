---
title: "[Solution] C Memory Leak Error — How to Fix"
description: "Fix C memory leaks from forgotten free() calls. Use Valgrind and ASan to detect and prevent leaks."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Memory Leak Error — How to Fix

Memory leaks occur when allocated memory is never freed. In long-running programs leaks accumulate and exhaust memory. Common causes include early returns skipping free(), reassigning pointers, and complex ownership.

## Common Error Messages

- `definitely lost: X bytes in Y blocks`
- `Invalid read after memory leak`
- `Out of memory from accumulated leaks`
- `heap block leaked at program exit`

## How to Fix It

### Free memory on all exit paths

```c
#include <stdlib.h>
#include <stdio.h>

int process(void) {
    int *buf = malloc(1024);
    if (!buf) return -1;
    FILE *fp = fopen("data.txt", "r");
    if (!fp) { free(buf); return -1; }
    fclose(fp);
    free(buf);
    return 0;
}
```

### Use goto for cleanup

```c
#include <stdlib.h>
#include <stdio.h>

int process(const char *path) {
    int ret = -1;
    int *buf = malloc(1024);
    if (!buf) goto done;
    FILE *fp = fopen(path, "r");
    if (!fp) goto cleanup_buf;
    ret = 0;
    fclose(fp);
cleanup_buf: free(buf);
done: return ret;
}
```

### Use Valgrind to detect leaks

```bash
gcc -g -o program program.c
valgrind --leak-check=full --show-leak-kinds=all ./program
```

### Track allocations

```c
#include <stdlib.h>
static int alloc_count = 0;
void *tracked_malloc(size_t s) { void *p = malloc(s); if (p) alloc_count++; return p; }
void tracked_free(void *p) { if (p) alloc_count--; free(p); }
```

## Common Scenarios

### Scenario 1: Early return from function skips free()

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Pointer reassigned without freeing old allocation

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Circular references between allocated structures

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Pair every malloc with a corresponding free
- **Tip 2:** Use Valgrind or ASan during development
- **Tip 3:** Use goto-based cleanup for multiple exit paths
