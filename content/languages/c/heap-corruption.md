---
title: "[Solution] C Heap Corruption Detected — Invalid Heap Memory Access Fix"
description: "Fix C 'heap corruption detected' errors. Understand how buffer overflows, double frees, and invalid pointer arithmetic corrupt the heap."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error", "memory-error"]
tags: ["heap-corruption", "heap-buffer", "memory-corruption", "malloc", "glibc"]
weight: 5
---

# [Solution] C Heap Corruption Detected — Invalid Heap Memory Access Fix

A **"heap corruption detected"** error occurs when the memory allocator (glibc's `malloc`/`free`) discovers that its internal metadata has been overwritten. This usually happens because your program wrote beyond the bounds of a heap-allocated buffer, freeing a bad pointer, or using memory after it was freed. Unlike a simple segfault, heap corruption is insidious — the crash may happen far from the actual bug.

## Common Causes

- **Heap buffer overflow** — writing past the end of a `malloc`-allocated buffer, corrupting adjacent allocations or heap metadata
- **Double free** — freeing the same heap pointer twice corrupts the free list
- **Wild pointer writes** — an uninitialized or dangling pointer writes to random heap memory
- **Mismatched allocator** — allocating with one library (e.g., `malloc`) and freeing with another

## How to Fix

### Fix 1: Check buffer sizes before writing

```c
#include <stdlib.h>
#include <string.h>

void process(const char *input, size_t input_len) {
    /* WRONG — may overflow if input_len >= 256 */
    char buf[256];
    memcpy(buf, input, input_len);

    /* CORRECT — allocate exactly what is needed */
    char *buf = malloc(input_len + 1);
    if (buf == NULL) return;
    memcpy(buf, input, input_len);
    buf[input_len] = '\0';
    /* ... use buf ... */
    free(buf);
}
```

### Fix 2: Never free pointers you didn't allocate

```c
#include <stdlib.h>

int main(void) {
    int arr[10];
    /* WRONG — arr is on the stack, free() is invalid */
    free(arr);

    /* CORRECT — only free heap memory */
    int *heap_arr = malloc(sizeof(int) * 10);
    if (heap_arr) {
        /* ... use heap_arr ... */
        free(heap_arr);
    }
    return 0;
}
```

### Fix 3: Don't access freed memory

```c
#include <stdlib.h>
#include <stdio.h>

int main(void) {
    int *p = malloc(sizeof(int) * 100);
    if (!p) return 1;

    free(p);

    /* WRONG — p is dangling, writing here corrupts the heap */
    p[0] = 42;

    /* CORRECT — set to NULL, never access after free */
    p = NULL;
    return 0;
}
```

### Fix 4: Use consistent allocation functions

```c
#include <stdlib.h>
#include <malloc.h>  /* Windows: _free_dbg for debug builds */

/* WRONG — mixing allocators */
void *p = HeapAlloc(GetProcessHeap(), 0, 100);
free(p);  /* heap corruption — wrong deallocator */

/* CORRECT — use the same allocator throughout */
void *p = malloc(100);
free(p);  /* matches malloc */
```

## Examples

```c
#include <stdlib.h>
#include <string.h>

int main(void) {
    /* Heap overflow — writes 10 bytes past a 10-byte buffer */
    char *small = malloc(10);
    memset(small, 'A', 20);  /* writes 10 bytes past the end */

    /* Off-by-one in string copy */
    char *name = malloc(5);
    strcpy(name, "hello");  /* needs 6 bytes (5 + NUL), allocates 5 */

    return 0;
}
```

## Debugging Tips

```bash
# AddressSanitizer is the fastest way to find heap corruption
gcc -fsanitize=address -g -o myprogram myprogram.c
./myprogram
# Reports the exact line where corruption occurred

# Valgrind is slower but very thorough
valgrind --tool=memcheck --track-origins=yes ./myprogram

# MALLOC_CHECK_=0 in glibc disables heap checks (not recommended for debugging)
```

## Related Errors

- [Double Free or Corruption]({{< relref "/languages/c/double-free" >}}) — freeing the same pointer twice
- [Buffer Overflow: Stack Smashing]({{< relref "/languages/c/buffer-overflow" >}}) — stack-based buffer overflow
- [Use After Free]({{< relref "/languages/c/use-after-free" >}}) — reading or writing freed memory
