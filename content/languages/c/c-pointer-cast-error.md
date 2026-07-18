---
title: "[Solution] C Pointer Cast Error — How to Fix"
description: "Fix C pointer cast errors including alignment issues, strict aliasing violations, and casting between incompatible types."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Pointer Cast Error — How to Fix

Casting pointers in C can cause undefined behavior when alignment requirements differ, strict aliasing rules are violated, or the target type has stricter alignment. Common mistakes include casting char* to struct pointers without alignment, casting between unrelated struct types, and casting function pointers incorrectly.

## Common Error Messages

- `Undefined behavior from misaligned pointer cast`
- `Strict aliasing violation from incompatible pointer cast`
- `Alignment fault from casting byte pointer to struct pointer`
- `Incompatible pointer type warning from unsafe cast`

## How to Fix It

### Use memcpy instead of pointer casting for type punning

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    unsigned char buf[4] = {0x00, 0x00, 0x80, 0x3F};
    float f;
    memcpy(&f, buf, sizeof(f));
    printf("float=%f\n", f);
    return 0;
}
```

### Ensure proper alignment before casting

```c
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int main(void) {
    void *p = malloc(sizeof(int) + 4);
    if (!p) return 1;
    char *aligned = (char *)p + (4 - (uintptr_t)p % 4) % 4;
    int *ip = (int *)aligned;
    *ip = 42;
    printf("%d\n", *ip);
    free(p);
    return 0;
}
```

### Use proper struct typedef with compatible types

```c
#include <stdio.h>

typedef struct { int x; int y; } Point;
typedef struct { int a; int b; } Coord;

int main(void) {
    Point p = {10, 20};
    // WRONG: Coord *c = (Coord *)&p;  // strict aliasing violation
    // CORRECT:
    Coord c;
    c.a = p.x;
    c.b = p.y;
    printf("Coord: %d, %d\n", c.a, c.b);
    return 0;
}
```

### Use union for type-safe punning

```c
#include <stdio.h>
#include <stdint.h>

typedef union {
    uint32_t i;
    float f;
} pun;

int main(void) {
    pun u;
    u.f = 3.14f;
    printf("bits=0x%08X\n", u.i);
    return 0;
}
```

## Common Scenarios

### Scenario 1: Casting char buffer pointer to struct pointer without alignment

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Casting between pointers of unrelated struct types causing UB

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Casting between int and pointer types on platforms where sizes differ

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Prefer memcpy over pointer casting for type punning
- **Tip 2:** Ensure proper alignment before casting between pointer types
- **Tip 3:** Use unions instead of pointer casts for accessing same memory as different types
