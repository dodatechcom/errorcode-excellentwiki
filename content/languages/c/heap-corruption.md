---
title: "[Solution] C Heap corruption detected"
description: "Fix C heap corruption. Prevent heap metadata damage from buffer overflows and invalid operations."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["heap-corruption", "heap", "metadata", "buffer-overflow", "glibc"]
weight: 5
---

# Heap corruption detected

Heap corruption occurs when a program writes beyond the boundaries of heap-allocated memory, corrupting the heap metadata. The corruption is often detected later when `free()` is called.

## Common Causes

```c
// Cause 1: Buffer overflow on heap
char *buf = malloc(10);
strcpy(buf, "this is a very long string"); // overflows

// Cause 2: Writing before allocated block
int *p = malloc(5 * sizeof(int));
*(p - 1) = 42; // corrupts metadata

// Cause 3: Overlapping memcpy
char *src = malloc(20);
char *dst = src + 5;
memcpy(dst, src, 10); // overlapping
```

## How to Fix

### Fix 1: Respect buffer boundaries

```c
char *buf = malloc(10);
strncpy(buf, "short", 9);
buf[9] = '\0';
```

### Fix 2: Don't access outside allocated block

```c
int *p = malloc(5 * sizeof(int));
// Only access p[0] through p[4]
```

### Fix 3: Use memmove for overlapping regions

```c
memmove(dst, src, 10); // handles overlap
```

### Fix 4: Use Valgrind to detect

```bash
gcc -g -o prog prog.c
valgrind --tool=memcheck ./prog
```

## Related Errors

- [Double free]({{< relref "/languages/c/double-free-heap.md" >}}) — heap metadata damage.
- [Invalid free]({{< relref "/languages/c/invalid-free" >}}) — invalid pointer.
- [Use after free]({{< relref "/languages/c/use-after-free-heap" >}}) — accessing freed memory.
