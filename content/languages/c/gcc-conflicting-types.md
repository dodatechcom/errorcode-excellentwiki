---
title: "[Solution] C CONFLICTING_TYPES — Conflicting types for function"
description: "Fix C conflicting types errors by ensuring declaration consistency, header synchronization, and correct static/extern usage. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["compile-error"]
weight: 810
---

# C CONFLICTING_TYPES — Conflicting types for function

GCC reports conflicting types when a function is declared with one signature and then re-declared or defined with a different signature. The types, return type, or parameter list must be identical across all declarations.

## Common Causes

```c
// Cause 1: Declaration in header doesn't match definition
// mylib.h
int process(int x);

// mylib.c
double process(int x) {  // returns double instead of int
    return x * 1.5;
}
// error: conflicting types for 'process'
```

```c
// Cause 2: Forward declaration with wrong parameter types
void init(int x);

void init(float x) {  // float instead of int
    // ...
}
// error: conflicting types for 'init'
```

```c
// Cause 3: Function declared in two headers with different signatures
// header_a.h
void handle(int fd, const char *buf);

// header_b.h
void handle(int fd, char *buf);  // missing const

// main.c includes both headers — conflicting types
```

```c
// Cause 4: Implicit declaration conflicts with later explicit declaration
int main(void) {
    int x = compute(5);  // implicit declaration: int compute(int)
    return x;
}

int compute(double x) {  // explicit declaration says double
    return (int)(x * 2);
}
// error: conflicting types for 'compute'
```

```c
// Cause 5: Static and extern declarations of the same function disagree
static int helper(int a, int b);

extern int helper(int a, float b);  // static vs extern + different type
// Two errors: storage class conflict and type conflict
```

## How to Fix

### Fix 1: Ensure header declarations match definitions exactly

```c
// mylib.h
int process(int x);  // declaration

// mylib.c
#include "mylib.h"
int process(int x) {  // definition matches declaration
    return x * 2;
}
```

### Fix 2: Use a single canonical header for each function

```c
// types.h — single source of truth for shared type declarations
#ifndef TYPES_H
#define TYPES_H

void handle(int fd, const char *buf);  // const char* is the correct signature

#endif

// All .c files include this one header — no conflicting declarations
#include "types.h"
```

### Fix 3: Forward-declare with matching types

```c
// WRONG: forward declaration doesn't match definition
void init(int x);
void init(float x) { /* ... */ }

// CORRECT: match types
void init(int x);
void init(int x) { /* ... */ }
```

### Fix 4: Include the header before using the function (avoid implicit declarations)

```c
#include "compute.h"  // declares: int compute(double x);

int main(void) {
    int result = compute(5.0);  // properly declared — no implicit declaration
    return result;
}
```

### Fix 5: Check for name collisions with macros or different translation units

```c
// If a macro redefines a function name:
#define process my_custom_process
// Then process() and my_custom_process() will have different types

// Solution: avoid #define name mangling for functions
// Use prefixed names instead:
void mylib_process(int x);
```

## Examples

```c
// Real-world: consistent API across header and implementation
// vector.h
#ifndef VECTOR_H
#define VECTOR_H

#include <stddef.h>

typedef struct {
    double *data;
    size_t size;
    size_t capacity;
} Vector;

Vector* vector_create(size_t initial_capacity);
void vector_destroy(Vector *v);
int vector_push(Vector *v, double value);
double vector_get(const Vector *v, size_t index);

#endif

// vector.c
#include "vector.h"
#include <stdlib.h>

Vector* vector_create(size_t initial_capacity) {
    Vector *v = malloc(sizeof(Vector));
    if (!v) return NULL;
    v->data = malloc(initial_capacity * sizeof(double));
    if (!v->data) { free(v); return NULL; }
    v->size = 0;
    v->capacity = initial_capacity;
    return v;
}

void vector_destroy(Vector *v) {
    if (v) { free(v->data); free(v); }
}

int vector_push(Vector *v, double value) {
    if (v->size >= v->capacity) return -1;
    v->data[v->size++] = value;
    return 0;
}

double vector_get(const Vector *v, size_t index) {
    return v->data[index];
}
```

```bash
# Debugging: find all declarations of a conflicting function
grep -rn 'void process' *.h *.c
grep -rn 'int process' *.h *.c

# Check preprocessor output to see what the compiler actually sees
gcc -E main.c | grep -A2 'process'
```

## Related Errors

- [C IMPLICIT_DECLARATION](/languages/c/gcc-implicit-declaration) — Implicit function declaration
- [C INCOMPATIBLE_POINTER_TYPE](/languages/c/gcc-incompatible-pointer-type) — Incompatible pointer type
- [C MULTIPLE_DEFINITION](/languages/c/linker-multiple-definition) — Multiple definition of symbol
