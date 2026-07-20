---
title: "[Solution] C INCOMPATIBLE_POINTER_TYPE — Incompatible pointer type"
description: "Fix C incompatible pointer type warnings by using correct types, explicit casts, and const qualifiers. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["warning"]
error-types: ["compile-error"]
weight: 808
---

# C INCOMPATIBLE_POINTER_TYPE — Incompatible pointer type

GCC warns when you pass a pointer of one type where a pointer of a different (incompatible) type is expected. While C allows implicit conversions between `void*` and other pointer types, converting between unrelated pointer types without a cast is a warning or error.

## Common Causes

```c
// Cause 1: Passing wrong pointer type to a function
#include <string.h>
int main(void) {
    int numbers[] = {1, 2, 3};
    char *dest = "hello";
    memcpy(dest, numbers, sizeof(numbers));  // warning: incompatible pointer types
    return 0;
}
// memcpy expects void*, but the intent is wrong — types don't match
```

```c
// Cause 2: Assigning between unrelated pointer types
int main(void) {
    int *ip;
    float *fp;
    ip = fp;  // warning: assignment from incompatible pointer type
    return 0;
}
```

```c
// Cause 3: Passing char** where char* is expected
void print_string(const char *str);

int main(void) {
    char *args[] = {"hello", "world"};
    print_string(args);  // warning: passing 'char **' to 'const char *'
    return 0;
}
```

```c
// Cause 4: Missing const qualifier
void process(const int *data);

int main(void) {
    int values[] = {1, 2, 3};
    const int *cp = values;
    int *p = values;
    process(p);    // works, but might warn about discarding const
    process(cp);   // correct
    return 0;
}
```

```c
// Cause 5: Function pointer type mismatch
void callback_int(int x);
void (*cb)(float) = callback_int;  // warning: incompatible function pointer types
```

## How to Fix

### Fix 1: Use matching types

```c
#include <string.h>

int main(void) {
    int numbers[] = {1, 2, 3};
    int dest[3];
    memcpy(dest, numbers, sizeof(numbers));  // both int* — no warning
    return 0;
}
```

### Fix 2: Use explicit casts when conversion is intentional

```c
#include <stdlib.h>

int main(void) {
    int *ip = malloc(100 * sizeof(int));  // malloc returns void*
    // In C, void* converts implicitly, but for clarity:
    ip = (int *)malloc(100 * sizeof(int));

    float *fp = (float *)ip;  // explicit cast — programmer takes responsibility
    return 0;
}
```

### Fix 3: Add const qualifier where data should not be modified

```c
void process(const int *data);
void modify(int *data);

int main(void) {
    int values[] = {1, 2, 3};
    const int *read_only = values;

    process(read_only);   // correct: const matches const
    modify(values);       // correct: non-const where modification is needed
    // modify(read_only); // WRONG: would discard const
    return 0;
}
```

### Fix 4: Fix function pointer types to match the callback signature

```c
void callback_int(int x) { printf("%d\n", x); }
void callback_float(float x) { printf("%f\n", x); }

int main(void) {
    void (*cb_int)(int) = callback_int;     // correct
    void (*cb_float)(float) = callback_float; // correct
    // void (*cb_bad)(int) = callback_float; // WRONG: type mismatch
    return 0;
}
```

### Fix 5: Use proper array/pointer conversions

```c
void print_string(const char *str);

int main(void) {
    const char *msg = "hello";
    print_string(msg);        // correct: char* to const char*

    char buffer[] = "world";
    print_string(buffer);     // correct: char[] decays to char*, implicit to const char*

    // If you have char** and need char*, dereference first
    char *args[] = {"a", "b"};
    print_string(args[0]);    // correct: args[0] is char*
    return 0;
}
```

## Examples

```c
// Real-world: qsort callback with wrong signature
#include <stdlib.h>

// WRONG: callback doesn't match expected signature
// int compare(int *a, int *b) { return *a - *b; }  // warning

// CORRECT: matches const void* signature
int compare(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

int main(void) {
    int arr[] = {5, 2, 8, 1, 9};
    qsort(arr, 5, sizeof(int), compare);
    return 0;
}
```

```c
// Real-world: callback registration with type safety
typedef void (*event_handler_t)(const char *event, void *user_data);

void on_click(const char *event, void *user_data) {
    int *count = (int *)user_data;
    (*count)++;
}

void register_handler(event_handler_t handler);

int main(void) {
    int click_count = 0;
    register_handler(on_click);  // types match exactly
    return 0;
}
```

## Related Errors

- [C IMPLICIT_DECLARATION](/languages/c/gcc-implicit-declaration) — Implicit function declaration
- [C CONFLICTING_TYPES](/languages/c/gcc-conflicting-types) — Conflicting types for function
- [C RETURN_LOCAL_ADDRESS](/languages/c/return-local-address) — Returning address of local variable
