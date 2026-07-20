---
title: "[Solution] C RETURN_LOCAL_ADDRESS — Returning address of local variable"
description: "Fix C returning address of local variable errors by returning by value, using malloc, or using static. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["undefined-behavior"]
weight: 820
---

# C RETURN_LOCAL_ADDRESS — Returning address of local variable

Returning a pointer to a local (automatic) variable causes undefined behavior. When the function returns, the local variable's stack space is reclaimed, and the pointer becomes dangling. The variable may appear to work briefly but will be overwritten by subsequent function calls.

## Common Causes

```c
// Cause 1: Returning pointer to local array
int* get_array(void) {
    int arr[5] = {1, 2, 3, 4, 5};
    return arr;  // warning: returns address of local variable
}
```

```c
// Cause 2: Returning pointer to local struct
struct Point {
    int x, y;
};

struct Point make_point(int x, int y) {
    struct Point p = {x, y};
    return &p;  // warning: returns address of local variable
}
```

```c
// Cause 3: Returning pointer to function parameter passed by value
char* process_name(const char *name) {
    char buffer[256];
    snprintf(buffer, sizeof(buffer), "processed_%s", name);
    return buffer;  // dangling pointer
}
```

```c
// Cause 4: Storing address of local in an output parameter
void get_value(int **out) {
    int local = 42;
    *out = &local;  // *out now points to a local variable
}
```

```c
// Cause 5: Returning address from compound literal (C99)
// This is actually VALID if the compound literal is at file scope
// but INVALID if at block scope:
int* get_value(void) {
    return &(int){42};  // block-scope compound literal — dangling
}
```

## How to Fix

### Fix 1: Return by value (copy the struct)

```c
struct Point {
    int x, y;
};

struct Point make_point(int x, int y) {
    struct Point p = {x, y};
    return p;  // returns a copy of the struct — safe
}

// Usage:
struct Point pt = make_point(3, 4);
```

### Fix 2: Use malloc to allocate on the heap

```c
#include <stdlib.h>
#include <string.h>

char* process_name(const char *name) {
    size_t len = strlen("processed_") + strlen(name) + 1;
    char *result = malloc(len);
    if (result == NULL) return NULL;
    snprintf(result, len, "processed_%s", name);
    return result;  // caller must free()
}

// Usage:
char *processed = process_name("hello");
printf("%s\n", processed);
free(processed);
```

### Fix 3: Use a static local variable (persists after function returns)

```c
const char* get_status(int code) {
    static char buffer[64];
    switch (code) {
        case 200: return "OK";
        case 404: return "Not Found";
        default:
            snprintf(buffer, sizeof(buffer), "Status %d", code);
            return buffer;  // static — valid until next call overwrites it
    }
}
// Note: not thread-safe — concurrent calls share the static buffer
```

### Fix 4: Use caller-provided buffer

```c
#include <stdio.h>

int format_name(const char *name, char *buf, size_t buf_size) {
    if (buf == NULL || buf_size == 0) return -1;
    return snprintf(buf, buf_size, "processed_%s", name);
}

// Usage:
char buffer[256];
format_name("hello", buffer, sizeof(buffer));
printf("%s\n", buffer);
```

### Fix 5: Use file-scope or global variables

```c
#include <stdio.h>

static int g_result[256];

int* compute_values(int n) {
    for (int i = 0; i < n && i < 256; i++) {
        g_result[i] = i * i;
    }
    return g_result;  // static storage — valid indefinitely
}
```

## Examples

```c
// Real-world: dynamic string building
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char* join_strings(const char **strings, size_t count, const char *sep) {
    if (count == 0) {
        char *empty = malloc(1);
        if (empty) empty[0] = '\0';
        return empty;
    }

    size_t total_len = 0;
    for (size_t i = 0; i < count; i++) {
        total_len += strlen(strings[i]);
    }
    total_len += strlen(sep) * (count - 1) + 1;

    char *result = malloc(total_len);
    if (result == NULL) return NULL;

    result[0] = '\0';
    for (size_t i = 0; i < count; i++) {
        if (i > 0) strcat(result, sep);
        strcat(result, strings[i]);
    }
    return result;
}

// Usage:
const char *words[] = {"hello", "world", "foo"};
char *joined = join_strings(words, 3, " ");
printf("'%s'\n", joined);  // 'hello world foo'
free(joined);
```

```c
// Real-world: returning a dynamically allocated struct
#include <stdlib.h>

typedef struct {
    int *data;
    size_t size;
} IntArray;

IntArray array_create(size_t size) {
    IntArray arr;
    arr.data = calloc(size, sizeof(int));
    arr.size = arr.data ? size : 0;
    return arr;  // returns by value — struct is copied
}

void array_destroy(IntArray *arr) {
    free(arr->data);
    arr->data = NULL;
    arr->size = 0;
}
```

## Related Errors

- [C USE_AFTER_FREE_C](/languages/c/use-after-free-c) — Use after free UB
- [C NULL_POINTER_ARITHMETIC](/languages/c/null-pointer-arithmetic) — Null pointer arithmetic UB
- [C MODIFY_CONST_OBJECT](/languages/c/modify-const-object) — Modifying const object UB
