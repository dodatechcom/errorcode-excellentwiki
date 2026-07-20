---
title: "[Solution] C MODIFY_CONST_OBJECT — Modifying const object UB"
description: "Fix C modifying const object undefined behavior by removing const, using mutable storage, or copying. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["warning"]
error-types: ["undefined-behavior"]
weight: 821
---

# C MODIFY_CONST_OBJECT — Modifying const object UB

Modifying an object that was declared `const` is undefined behavior. The compiler may place `const` objects in read-only memory, and attempting to write to them can cause a segmentation fault or silent corruption.

## Common Causes

```c
// Cause 1: Modifying a const variable directly
const int x = 10;
x = 20;  // error: assignment of read-only variable 'x'
```

```c
// Cause 2: Casting away const and writing through the pointer
const int x = 10;
int *p = (int *)&x;
*p = 20;  // undefined behavior: modifying const object
```

```c
// Cause 3: Modifying a string literal
char *str = "hello world";  // string literals are const in C
str[0] = 'H';  // undefined behavior: modifying const data
```

```c
// Cause 4: Modifying data through a const pointer parameter
void process(int *data, size_t n) {
    // Caller passed const data but you cast away const
    const int *cdata = data;
    int *mutable = (int *)cdata;
    mutable[0] = 42;  // UB if original data was const
}
```

```c
// Cause 5: Modifying a compound literal marked const
const int *arr = &(const int[]){1, 2, 3, 4, 5};
((int *)arr)[0] = 99;  // undefined behavior: modifying const compound literal
```

## How to Fix

### Fix 1: Remove const if you need to modify the object

```c
// WRONG: const when you need to modify
const int value = 10;
int *p = (int *)&value;
*p = 20;

// CORRECT: don't use const
int value = 10;
value = 20;  // fine
```

### Fix 2: Create a mutable copy of const data

```c
#include <string.h>

void process_data(const int *src, int *dst, size_t n) {
    memcpy(dst, src, n * sizeof(int));
    // Now modify dst, not src
    for (size_t i = 0; i < n; i++) {
        dst[i] *= 2;
    }
}
```

### Fix 3: Use char arrays instead of string literals for modifiable strings

```c
// WRONG: string literal — cannot be modified
char *str = "hello";
str[0] = 'H';  // UB

// CORRECT: char array — can be modified
char str[] = "hello";
str[0] = 'H';  // OK: str is now "Hello"
```

### Fix 4: Design APIs that separate read and write access

```c
// WRONG: function takes non-const but shouldn't modify
void print_config(struct Config *cfg) {
    printf("name: %s\n", cfg->name);
    // Should not modify cfg, but type allows it
}

// CORRECT: use const for read-only access
void print_config(const struct Config *cfg) {
    printf("name: %s\n", cfg->name);
}

// For modification:
void update_config(struct Config *cfg, const char *name) {
    strncpy(cfg->name, name, sizeof(cfg->name));
}
```

### Fix 5: Use volatile or restrict carefully, and respect const

```c
// If a function promises not to modify data, trust the const
void sort_array(const int *arr, size_t n) {
    // Don't cast away const here — the function's contract is read-only
    // If sorting is needed, work on a copy
    int *copy = malloc(n * sizeof(int));
    if (!copy) return;
    memcpy(copy, arr, n * sizeof(int));
    // sort copy...
    free(copy);
}
```

## Examples

```c
// Real-world: correct use of const in a config system
typedef struct {
    char name[64];
    int value;
    int enabled;
} Config;

// Read-only access
void print_config(const Config *cfg) {
    printf("[%s] value=%d enabled=%d\n", cfg->name, cfg->value, cfg->enabled);
}

// Read-only access to array
void print_all_configs(const Config *configs, size_t n) {
    for (size_t i = 0; i < n; i++) {
        print_config(&configs[i]);
    }
}

// Write access — separate function
void update_config_value(Config *cfg, int new_value) {
    cfg->value = new_value;
}

// Modify a copy of config
Config config_modified(const Config *original, int new_value) {
    Config copy = *original;  // stack copy
    copy.value = new_value;
    return copy;  // return modified copy, original unchanged
}
```

```c
// Real-world: const-correct linked list
struct Node {
    int data;
    struct Node *next;
};

// Read-only traversal
int list_sum(const struct Node *head) {
    int sum = 0;
    for (const struct Node *n = head; n != NULL; n = n->next) {
        sum += n->data;
    }
    return sum;
}

// Mutation
void list_double(struct Node *head) {
    for (struct Node *n = head; n != NULL; n = n->next) {
        n->data *= 2;
    }
}
```

## Related Errors

- [C RETURN_LOCAL_ADDRESS](/languages/c/return-local-address) — Returning address of local variable
- [C USE_AFTER_FREE_C](/languages/c/use-after-free-c) — Use after free UB
- [C STRICT_ALIASING_VIOLATION](/languages/c/strict-aliasing-violation) — Strict aliasing violation
