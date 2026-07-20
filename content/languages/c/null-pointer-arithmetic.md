---
title: "[Solution] C NULL_POINTER_ARITHMETIC — Null pointer arithmetic UB"
description: "Fix C null pointer arithmetic undefined behavior by checking for NULL and avoiding subtraction of null pointers. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["warning"]
error-types: ["undefined-behavior"]
weight: 819
---

# C NULL_POINTER_ARITHMETIC — Null pointer arithmetic UB

Performing arithmetic on null pointers is undefined behavior in C. This includes dereferencing a null pointer, adding or subtracting from a null pointer, and subtracting two null pointers. While some platforms tolerate null pointer arithmetic, the standard explicitly forbids it.

## Common Causes

```c
// Cause 1: Dereferencing a NULL pointer
int *p = NULL;
int val = *p;  // undefined behavior: dereference of NULL pointer
```

```c
// Cause 2: Pointer arithmetic on NULL
char *p = NULL;
char *next = p + 1;  // undefined behavior: arithmetic on NULL
```

```c
// Cause 3: Subtracting two NULL pointers
char *a = NULL;
char *b = NULL;
ptrdiff_t diff = a - b;  // undefined behavior: two null pointers
```

```c
// Cause 4: NULL pointer passed to functions expecting valid pointers
#include <string.h>
void *dest = NULL;
void *src = "hello";
memcpy(dest, src, 6);  // undefined behavior: NULL arguments
```

```c
// Cause 5: Array access that results in NULL pointer arithmetic
int *arr = NULL;
int val = arr[5];  // equivalent to *(arr + 5) — undefined behavior
```

## How to Fix

### Fix 1: Always check for NULL before dereferencing

```c
#include <stddef.h>

int get_value(const int *p) {
    if (p == NULL) {
        return -1;  // or handle error appropriately
    }
    return *p;  // safe: p is guaranteed non-NULL
}
```

### Fix 2: Check for NULL before pointer arithmetic

```c
#include <stddef.h>

char* safe_offset(char *ptr, ptrdiff_t offset) {
    if (ptr == NULL) {
        return NULL;
    }
    return ptr + offset;  // safe: ptr is non-NULL
}
```

### Fix 3: Guard pointer subtraction

```c
#include <stddef.h>

ptrdiff_t safe_diff(const char *a, const char *b) {
    if (a == NULL || b == NULL) {
        return 0;  // or handle error
    }
    return a - b;  // safe: both pointers are non-NULL
}
```

### Fix 4: Use defensive programming with function return values

```c
#include <stdlib.h>
#include <stddef.h>

int process_data(size_t n) {
    int *buf = malloc(n * sizeof(int));
    if (buf == NULL) {
        return -1;  // allocation failed — don't use buf
    }

    // Safe to use buf here
    for (size_t i = 0; i < n; i++) {
        buf[i] = (int)i;
    }

    free(buf);
    return 0;
}
```

### Fix 5: Use static analysis tools to detect NULL dereferences

```bash
# GCC/Clang static analyzer
gcc -fanalyzer main.c -o app

# Clang's scan-build
scan-build gcc main.c -o app

# Valgrind (catches at runtime)
valgrind --tool=memcheck ./app

# Coverity, cppcheck, etc.
cppcheck main.c
```

## Examples

```c
// Real-world: linked list traversal with NULL safety
#include <stdlib.h>
#include <stdio.h>

struct Node {
    int data;
    struct Node *next;
};

int sum_list(const struct Node *head) {
    int sum = 0;
    const struct Node *current = head;

    while (current != NULL) {  // check before dereference
        sum += current->data;
        current = current->next;
    }

    return sum;
}

// Safe array-like access with bounds checking
int safe_get(const int *arr, size_t size, size_t index) {
    if (arr == NULL || index >= size) {
        return -1;  // error: null pointer or out of bounds
    }
    return arr[index];
}
```

```c
// Real-world: string operations with NULL safety
#include <string.h>
#include <stddef.h>

size_t safe_strlen(const char *s) {
    if (s == NULL) return 0;  // handle NULL gracefully
    return strlen(s);
}

char* safe_strcat(char *dest, const char *src, size_t dest_size) {
    if (dest == NULL || src == NULL) return dest;
    size_t len = strlen(dest);
    if (len >= dest_size - 1) return dest;
    strncat(dest, src, dest_size - len - 1);
    return dest;
}
```

## Related Errors

- [C USE_AFTER_FREE_C](/languages/c/use-after-free-c) — Use after free UB
- [C RETURN_LOCAL_ADDRESS](/languages/c/return-local-address) — Returning address of local variable
- [C CASTING_OUT_OF_RANGE](/languages/c/casting-out-of-range) — Casting out of range value
