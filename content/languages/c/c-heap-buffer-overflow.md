---
title: "[Solution] C Heap Buffer Overflow Error — How to Fix"
description: "Fix C heap buffer overflow bugs from writing past dynamically allocated memory boundaries."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Heap Buffer Overflow Error — How to Fix

Heap buffer overflows occur when writing beyond heap-allocated memory, corrupting heap metadata. Common causes include incorrect size calculations, off-by-one errors, and use-after-free.

## Common Error Messages

- `heap-buffer-overflow detected by ASan`
- `free(): invalid pointer -- heap corruption`
- `malloc(): memory corruption`
- `HEAP CORRUPTION DETECTED`

## How to Fix It

### Allocate correct size

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    const char *src = "Hello";
    char *dst = malloc(strlen(src) + 1);
    if (!dst) return 1;
    strcpy(dst, src);
    printf("%s\n", dst);
    free(dst);
    return 0;
}
```

### Validate sizes before allocation

```c
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

int safe_alloc(size_t count, size_t size, void **out) {
    if (count > SIZE_MAX / size) return -1;
    *out = malloc(count * size);
    return *out ? 0 : -1;
}
```

### Use safe copy functions

```c
void safe_copy(char *dst, size_t dst_size, const char *src) {
    if (dst_size == 0) return;
    strncpy(dst, src, dst_size - 1);
    dst[dst_size - 1] = 0;
}
```

### Enable heap protection

```bash
gcc -fsanitize=address -g -o program program.c
```

## Common Scenarios

### Scenario 1: Writing past end of malloc buffer due to off-by-one

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Wrong size in memcpy causing heap corruption

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Writing to freed heap memory corrupting allocator

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Validate allocation sizes to prevent integer overflow
- **Tip 2:** Use -fsanitize=address to detect heap overflows
- **Tip 3:** Set pointers to NULL after free
