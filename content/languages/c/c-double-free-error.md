---
title: "[Solution] C Double Free Error — How to Fix"
description: "Fix C double free errors that cause heap corruption. Prevent calling free() twice on the same pointer."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Double Free Error — How to Fix

Double free occurs when free() is called on the same pointer twice, corrupting heap data structures. Common causes include missing NULL checks, error paths freeing already-freed memory, and aliased pointers.

## Common Error Messages

- `double free or corruption (fastbin)`
- `free(): double free detected`
- `malloc: memory corruption (fast)`
- `Aborted (core dumped) from double free`

## How to Fix It

### Set pointer to NULL after free

```c
#include <stdlib.h>

int main(void) {
    int *p = malloc(sizeof(int));
    if (!p) return 1;
    *p = 42;
    free(p);
    p = NULL;
    free(p);  // safe: free(NULL) is a no-op
    return 0;
}
```

### Use a safe free wrapper

```c
#include <stdlib.h>

#define SAFE_FREE(ptr) do { free(ptr); (ptr) = NULL; } while(0)

int main(void) {
    int *p = malloc(sizeof(int));
    if (!p) return 1;
    SAFE_FREE(p);
    SAFE_FREE(p);  // safe
    return 0;
}
```

### Track ownership

```c
#include <stdlib.h>

typedef struct { int *data; int owned; } OwnedBuffer;

void release_buffer(OwnedBuffer *b) {
    if (b->owned && b->data) {
        free(b->data);
        b->data = NULL;
        b->owned = 0;
    }
}
```

### Validate before freeing

```c
#include <stdlib.h>

void safe_free(void **ptr) {
    if (ptr && *ptr) { free(*ptr); *ptr = NULL; }
}
```

## Common Scenarios

### Scenario 1: Both error and normal path free the same pointer

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Two pointers alias same allocation and both are freed

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Freeing memory in a loop with overlapping data

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always set pointers to NULL after free
- **Tip 2:** Use a SAFE_FREE macro for automatic nulling
- **Tip 3:** Run with AddressSanitizer to detect double frees
