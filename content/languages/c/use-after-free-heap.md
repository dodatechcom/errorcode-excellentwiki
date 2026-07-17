---
title: "[Solution] C Use after free — heap memory"
description: "Fix C use-after-free heap memory errors. Prevent accessing freed heap memory."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["use-after-free", "heap", "memory", "dangling-pointer", "undefined-behavior"]
weight: 5
---

# Use after free — heap memory

Use-after-free occurs when a program continues to use a pointer after the memory it points to has been freed. This is undefined behavior that can lead to crashes, data corruption, or security vulnerabilities.

## Common Causes

```c
// Cause 1: Accessing freed memory
int *p = malloc(sizeof(int));
*p = 42;
free(p);
printf("%d\n", *p); // use-after-free

// Cause 2: Using freed pointer in function
char *get_string(void) {
    char *s = malloc(100);
    strcpy(s, "hello");
    free(s);
    return s; // dangling pointer
}

// Cause 3: Use-after-free in data structure
struct Node {
    int data;
    struct Node *next;
};
// free node but still reference node->next
```

## How to Fix

### Fix 1: Set pointer to NULL after free

```c
int *p = malloc(sizeof(int));
*p = 42;
free(p);
p = NULL; // safe
```

### Fix 2: Don't return freed pointers

```c
char *get_string(void) {
    char *s = malloc(100);
    strcpy(s, "hello");
    return s; // caller must free
}
```

### Fix 3: Use Valgrind to detect

```bash
gcc -g -o prog prog.c
valgrind --tool=memcheck ./prog
```

## Examples

```c
#include <stdlib.h>
#include <stdio.h>

int main(void) {
    int *arr = malloc(5 * sizeof(int));
    if (!arr) return 1;
    
    for (int i = 0; i < 5; i++) {
        arr[i] = i * 10;
    }
    
    free(arr);
    arr = NULL; // prevent use-after-free
    
    // Don't access arr here
    
    return 0;
}
```

## Related Errors

- [Double free]({{< relref "/languages/c/double-free-heap.md" >}}) — freeing twice.
- [Heap corruption]({{< relref "/languages/c/heap-corruption" >}}) — general heap damage.
- [Invalid free]({{< relref "/languages/c/invalid-free" >}}) — freeing invalid pointer.
