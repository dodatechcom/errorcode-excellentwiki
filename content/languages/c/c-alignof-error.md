---
title: "[Solution] C _Alignof / alignof Error — How to Fix"
description: "Fix C alignment errors using _Alignof and alignment attributes. Prevent misaligned access."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C _Alignof / alignof Error — How to Fix

_Alignof returns type alignment requirement. Misaligned access causes performance penalties or hardware faults. Common errors include assuming alignment, allocating without alignment, and casting without checking.

## Common Error Messages

- `Bus error from misaligned access`
- `Undefined behavior from misaligned pointer`
- `Alignment fault on ARM`
- `Performance penalty from misaligned struct`

## How to Fix It

### Check alignment with _Alignof

```c
#include <stdio.h>
#include <stdalign.h>
typedef struct { char a; int b; double c; } Mixed;
int main(void) {
    printf("_Alignof(int): %zu\n", _Alignof(int));
    printf("_Alignof(Mixed): %zu\n", _Alignof(Mixed));
    printf("sizeof(Mixed): %zu\n", sizeof(Mixed));
    return 0;
}
```

### Use aligned_alloc

```c
#include <stdlib.h>
#include <stdalign.h>
typedef struct { int x; double y; } Aligned;
int main(void) {
    void *p = aligned_alloc(_Alignof(Aligned), sizeof(Aligned));
    if (!p) return 1;
    Aligned *a = (Aligned *)p;
    a->x = 42; a->y = 3.14;
    free(p);
    return 0;
}
```

### Use alignment attributes

```c
typedef struct __attribute__((aligned(64))) { int data[16]; } CacheAligned;
printf("alignof: %zu\n", _Alignof(CacheAligned));
```

### Manual pointer alignment

```c
#include <stdint.h>
void *align_ptr(void *ptr, size_t alignment) {
    uintptr_t addr = (uintptr_t)ptr;
    uintptr_t aligned = (addr + alignment - 1) & ~(alignment - 1);
    return (void *)aligned;
}
```

## Common Scenarios

### Scenario 1: Casting char buffer to int pointer without alignment

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Using wrong alignment for target type

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Assuming all types have 4-byte alignment

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Use _Alignof before casting pointers
- **Tip 2:** Use aligned_alloc for properly aligned memory
- **Tip 3:** Use alignment attributes for cache-line aligned data
