---
title: "[Solution] C Segmentation fault: address 0x0"
description: "Fix C segmentation fault at address 0x0. Resolve null pointer dereference crashes."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Segmentation fault: address 0x0

When a segfault occurs at address `0x0`, it means your program tried to access memory at the NULL address. This is the most common form of segmentation fault.

## Common Causes

```c
// Cause 1: Dereferencing NULL
int *ptr = NULL;
*ptr = 5; // segfault at 0x0

// Cause 2: Uninitialized pointer
struct Node *node;
node->next = NULL; // segfault — node is garbage

// Cause 3: Failed allocation
char *buffer = malloc(0);
strcpy(buffer, "hello"); // segfault if malloc returned NULL
```

## How to Fix

### Fix 1: Validate before dereferencing

```c
if (ptr != NULL) {
    *ptr = 5;
}
```

### Fix 2: Initialize all pointers

```c
struct Node *node = malloc(sizeof(struct Node));
if (node) {
    node->next = NULL;
}
```

### Fix 3: Use GDB to find crash location

```bash
gcc -g -o prog prog.c
gdb ./prog
(gdb) run
# When it crashes:
(gdb) bt
```

## Related Errors

- [NULL pointer dereference]({{< relref "/languages/c/null-pointer-dereference" >}}) — detailed null pointer analysis.
- [Double free]({{< relref "/languages/c/double-free-heap.md" >}}) — heap corruption from double free.
- [Use after free]({{< relref "/languages/c/use-after-free-heap" >}}) — accessing freed memory.
