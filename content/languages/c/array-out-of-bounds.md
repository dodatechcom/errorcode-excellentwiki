---
title: "[Solution] C Array Index Out of Bounds — Undefined Behavior Fix"
description: "Fix C 'array index out of bounds' errors. Prevent buffer overflows, stack smashing, and undefined behavior from invalid array access."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error", "memory-error"]
weight: 5
---

# [Solution] C Array Index Out of Bounds — Undefined Behavior Fix

An **array index out of bounds** occurs when your program accesses an array element using an index that is less than zero or greater than or equal to the array's size. In C, arrays have no built-in bounds checking — accessing an out-of-bounds element reads or writes whatever memory happens to be adjacent, causing undefined behavior, crashes, or silent data corruption.

## Common Causes

- **Off-by-one error** — loop iterates one too many times (e.g., `i <= n` instead of `i < n`)
- **Unvalidated user input** — using an index from user input without checking the range
- **Signed/unsigned mismatch** — a negative signed index wraps to a large unsigned value
- **Incorrect array size calculation** — using `sizeof` on a pointer instead of an array

## How to Fix

### Fix 1: Always validate indices before access

```c
#include <stdio.h>

int get_element(const int *arr, size_t size, int index) {
    if (index < 0 || (size_t)index >= size) {
        fprintf(stderr, "Index %d out of bounds (size %zu)\n", index, size);
        return -1;
    }
    return arr[index];
}

int main(void) {
    int data[] = {10, 20, 30, 40, 50};
    size_t len = sizeof(data) / sizeof(data[0]);

    printf("%d\n", get_element(data, len, 2));   /* OK: 30 */
    printf("%d\n", get_element(data, len, 10));  /* Error message */

    return 0;
}
```

### Fix 2: Use correct loop bounds

```c
#include <stdio.h>

int main(void) {
    int arr[5] = {1, 2, 3, 4, 5};

    /* WRONG — off-by-one: i < 5 is correct, but arr[5] is out of bounds */
    for (int i = 0; i <= 5; i++) {  /* i <= 5 is wrong */
        printf("%d\n", arr[i]);
    }

    /* CORRECT — strict less-than */
    for (int i = 0; i < 5; i++) {
        printf("%d\n", arr[i]);
    }
    return 0;
}
```

### Fix 3: Use size_t for array indices to avoid signed issues

```c
#include <stdio.h>

int main(void) {
    int arr[10] = {0};

    /* WRONG — signed int can be negative */
    int index = -1;
    arr[index] = 42;  /* undefined behavior — negative index */

    /* CORRECT — size_t is always non-negative */
    size_t safe_index = 0;
    if (safe_index < 10) {
        arr[safe_index] = 42;
    }
    return 0;
}
```

### Fix 4: Don't use sizeof on pointers

```c
#include <stdio.h>
#include <stdlib.h>

/* WRONG — sizeof(ptr) is 4 or 8, not array size */
void process_wrong(int *arr) {
    size_t count = sizeof(arr) / sizeof(arr[0]);  /* always 1 on 64-bit */
    for (size_t i = 0; i < count; i++) {
        arr[i] = i;  /* only writes to first element */
    }
}

/* CORRECT — pass size explicitly */
void process_correct(int *arr, size_t count) {
    for (size_t i = 0; i < count; i++) {
        arr[i] = i;
    }
}

int main(void) {
    int data[100];
    process_correct(data, 100);
    return 0;
}
```

## Examples

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    /* Example 1: Stack buffer overflow from out-of-bounds write */
    int nums[4] = {10, 20, 30, 40};
    nums[4] = 50;  /* writes past the end — corrupts adjacent stack data */

    /* Example 2: Negative index reads adjacent stack memory */
    int arr[3] = {100, 200, 300};
    int i = -1;
    printf("%d\n", arr[i]);  /* reads whatever is before arr on the stack */

    /* Example 3: String buffer overflow */
    char name[8];
    strcpy(name, "Hello, World!");  /* 13 chars + NUL — overflows name */

    return 0;
}
```

## Compilation Flags

```bash
# Enable bounds checking at compile time where possible
gcc -fsanitize=address -g -o myprogram myprogram.c

# Enable all warnings
gcc -Wall -Wextra -Warray-bounds -o myprogram myprogram.c

# Use -D_FORTIFY_SOURCE=2 for runtime checks on some string/array functions
gcc -D_FORTIFY_SOURCE=2 -O2 -o myprogram myprogram.c
```

## Related Errors

- [Buffer Overflow: Stack Smashing]({{< relref "/languages/c/buffer-overflow" >}}) — out-of-bounds write corrupts the stack canary
- [Heap Corruption Detected]({{< relref "/languages/c/heap-corruption" >}}) — out-of-bounds write on a heap buffer
- [Segmentation Fault (Core Dumped)]({{< relref "/languages/c/segfault" >}}) — out-of-bounds access hits unmapped memory
