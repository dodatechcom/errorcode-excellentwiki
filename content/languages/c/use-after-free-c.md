---
title: "[Solution] C USE_AFTER_FREE — Use after free UB (C-specific)"
description: "Fix C use after free undefined behavior by setting pointers to NULL after free, using after-free detection tools, and careful memory management. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["warning"]
error-types: ["undefined-behavior"]
weight: 824
---

# C USE_AFTER_FREE — Use after free UB (C-specific)

Using a pointer after the memory it points to has been freed is undefined behavior. The freed memory may be reused by another allocation, causing corruption, crashes, or security vulnerabilities.

## Common Causes

```c
// Cause 1: Direct use after free
char *str = malloc(16);
strcpy(str, "hello");
free(str);
printf("%s\n", str);  // use after free — str points to freed memory
```

```c
// Cause 2: Double free
char *str = malloc(16);
free(str);
free(str);  // double free — undefined behavior
```

```c
// Cause 3: Use after free through a copied pointer
char *a = malloc(16);
char *b = a;  // b points to same memory
free(a);
printf("%s\n", b);  // b is now dangling
```

```c
// Cause 4: Use after free in data structures
struct Node {
    int data;
    struct Node *next;
};

void remove_node(struct Node **head, struct Node *target) {
    // unlink target from list
    // ... unlink logic ...
    free(target);
    // BUG: if caller still has a pointer to target and uses it
}
```

```c
// Cause 5: Returning a pointer to freed memory
char* get_string(void) {
    char *buf = malloc(64);
    strcpy(buf, "hello");
    free(buf);
    return buf;  // returning dangling pointer
}
```

## How to Fix

### Fix 1: Set pointers to NULL immediately after free

```c
char *str = malloc(16);
if (str == NULL) return -1;
strcpy(str, "hello");
free(str);
str = NULL;  // subsequent use of NULL is detectable (crash with clear reason)

// Now any accidental use is a NULL dereference (debuggable) rather than use-after-free
```

### Fix 2: Use after-free detection tools

```bash
# Valgrind (most thorough)
valgrind --tool=memcheck --track-origins=yes ./app

# AddressSanitizer (faster, built into GCC/Clang)
gcc -fsanitize=address -g main.c -o app
./app  # reports use-after-free at the exact point of occurrence

# MemorySanitizer (for uninitialized memory)
gcc -fsanitize=memory -g main.c -o app
```

### Fix 3: Use safe free-and-null pattern consistently

```c
#include <stdlib.h>

// Safe free macro
#define SAFE_FREE(ptr) do { free(ptr); (ptr) = NULL; } while(0)

void process(void) {
    char *data = malloc(1024);
    if (data == NULL) return;

    // use data...

    SAFE_FREE(data);  // frees and sets to NULL
    // SAFE_FREE(data);  // safe: free(NULL) is a no-op
}
```

### Fix 4: Design ownership semantics clearly

```c
// Clear ownership: caller owns the memory and must free it
char* create_string(const char *input) {
    char *result = malloc(strlen(input) + 1);
    if (result) strcpy(result, input);
    return result;  // caller must free()
}

// Usage:
char *s = create_string("hello");
printf("%s\n", s);
free(s);       // caller frees
s = NULL;      // prevent use-after-free

// Library takes ownership and frees internally
void store_string(char **dest, const char *src) {
    free(*dest);           // free old value if any
    *dest = strdup(src);   // store new copy
}
```

### Fix 5: Use reference counting for shared memory

```c
#include <stdlib.h>
#include <stdio.h>

typedef struct {
    int ref_count;
    char data[64];
} SharedData;

SharedData* shared_create(const char *str) {
    SharedData *d = malloc(sizeof(SharedData));
    if (d) {
        d->ref_count = 1;
        snprintf(d->data, sizeof(d->data), "%s", str);
    }
    return d;
}

void shared_retain(SharedData *d) {
    if (d) d->ref_count++;
}

void shared_release(SharedData *d) {
    if (d && --d->ref_count == 0) {
        free(d);
    }
}
```

## Examples

```c
// Real-world: safe dynamic array with proper cleanup
#include <stdlib.h>
#include <string.h>

typedef struct {
    char **items;
    size_t size;
    size_t capacity;
} StringArray;

StringArray* array_create(void) {
    StringArray *arr = calloc(1, sizeof(StringArray));
    return arr;
}

void array_add(StringArray *arr, const char *str) {
    if (arr->size >= arr->capacity) {
        size_t new_cap = arr->capacity ? arr->capacity * 2 : 8;
        char **new_items = realloc(arr->items, new_cap * sizeof(char*));
        if (!new_items) return;
        arr->items = new_items;
        arr->capacity = new_cap;
    }
    arr->items[arr->size++] = strdup(str);
}

void array_destroy(StringArray *arr) {
    if (!arr) return;
    for (size_t i = 0; i < arr->size; i++) {
        free(arr->items[i]);
        arr->items[i] = NULL;  // prevent use-after-free of individual items
    }
    free(arr->items);
    arr->items = NULL;
    free(arr);
}
```

```bash
# Detecting use-after-free with AddressSanitizer
gcc -fsanitize=address -g -O1 main.c -o app
./app
# Output: ERROR: AddressSanitizer: stack-use-after-return on address 0x...
```

## Related Errors

- [C RETURN_LOCAL_ADDRESS](/languages/c/return-local-address) — Returning address of local variable
- [C NULL_POINTER_ARITHMETIC](/languages/c/null-pointer-arithmetic) — Null pointer arithmetic UB
- [C MODIFY_CONST_OBJECT](/languages/c/modify-const-object) — Modifying const object UB
