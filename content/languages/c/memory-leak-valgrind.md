---
title: "[Solution] C Valgrind: memory leak detected"
description: "Fix C memory leaks detected by Valgrind. Track and eliminate memory leaks in C programs."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["memory-leak", "valgrind", "leak-check", "heap", "malloc"]
weight: 5
---

# Valgrind: memory leak detected

A memory leak occurs when allocated memory is never freed. Valgrind reports lost blocks with stack traces showing where each allocation was made.

## Common Causes

```c
// Cause 1: Forgetting to free
void leak(void) {
    int *p = malloc(100 * sizeof(int));
    // never free(p)
}

// Cause 2: Early return without free
int process(void) {
    int *buf = malloc(1024);
    if (error_condition) {
        return -1; // buf leaked
    }
    free(buf);
    return 0;
}

// Cause 3: Lost pointer
int *p = malloc(sizeof(int));
p = NULL; // can't free anymore
```

## How to Fix

### Fix 1: Free all allocations

```c
void no_leak(void) {
    int *p = malloc(100 * sizeof(int));
    // ... use p ...
    free(p);
}
```

### Fix 2: Use cleanup pattern

```c
int process(void) {
    int *buf = malloc(1024);
    if (!buf) return -1;
    
    int result = do_work(buf);
    free(buf); // always free
    return result;
}
```

### Fix 3: Track with Valgrind

```bash
gcc -g -o prog prog.c
valgrind --leak-check=full --show-leak-kinds=all ./prog
```

## Examples

```bash
# Basic leak check
valgrind --leak-check=full ./prog

# Full report with summaries
valgrind --leak-check=full --show-leak-kinds=definite,possible ./prog

# Output example:
# ==12345== 100 bytes in 1 blocks are definitely lost
# ==12345==    at 0x4C2AB80: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
# ==12345==    by 0x108674: main (leak.c:5)
```

## Related Errors

- [Double free]({{< relref "/languages/c/double-free-heap.md" >}}) — freeing twice.
- [Use after free]({{< relref "/languages/c/use-after-free-heap" >}}) — accessing freed memory.
- [Out of memory: malloc failed]({{< relref "/languages/c/out-of-memory-malloc" >}}) — malloc failure.
