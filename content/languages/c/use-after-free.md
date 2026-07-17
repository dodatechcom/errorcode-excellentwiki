---
title: "[Solution] C Use After Free — Invalid Read/Write of Freed Memory Fix"
description: "Fix C 'use after free' errors detected by Valgrind and AddressSanitizer. Learn how dangling pointers cause undefined behavior and crashes."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error", "memory-error"]
weight: 5
---

# [Solution] C Use After Free — Invalid Read/Write of Freed Memory Fix

A **use-after-free** occurs when your program reads from or writes to memory that has already been freed. After `free()`, the memory may be reallocated for a different purpose, reused by the allocator, or left in a corrupted state. Accessing it causes undefined behavior — crashes, data corruption, or exploitable vulnerabilities. Valgrind reports this as `Invalid read/write of size N` and AddressSanitizer reports it as `heap-use-after-free`.

## Common Causes

- **Accessing a pointer after `free()`** — the pointer is still valid syntactically but the memory is no longer yours
- **Returning a pointer to stack or freed heap memory** — the caller receives a dangling pointer
- **Storing a pointer in a data structure after freeing** — the structure outlives the allocation
- **Race condition in multi-threaded code** — one thread frees memory while another still reads it

## How to Fix

### Fix 1: Set pointers to NULL after freeing

```c
#include <stdlib.h>
#include <stdio.h>

int main(void) {
    int *p = malloc(sizeof(int));
    *p = 42;
    free(p);
    p = NULL;

    /* Any later dereference is now a predictable NULL dereference
       instead of undefined behavior */
    if (p != NULL) {
        printf("%d\n", *p);
    }
    return 0;
}
```

### Fix 2: Don't use pointers after freeing

```c
#include <stdlib.h>
#include <stdio.h>

int main(void) {
    char *name = malloc(32);
    if (name == NULL) return 1;

    snprintf(name, 32, "Alice");
    printf("Name: %s\n", name);

    free(name);
    /* WRONG: printf("Name: %s\n", name); — use-after-free */

    name = NULL;  /* good practice */
    return 0;
}
```

### Fix 3: Zero the reference count in shared data

```c
#include <stdlib.h>
#include <stdio.h>

typedef struct {
    int refcount;
    char *data;
} Shared;

Shared *shared_create(const char *str) {
    Shared *s = malloc(sizeof(Shared));
    if (!s) return NULL;
    s->refcount = 1;
    s->data = strdup(str);
    return s;
}

void shared_release(Shared *s) {
    if (s == NULL) return;
    s->refcount--;
    if (s->refcount <= 0) {
        free(s->data);
        free(s);
    }
}
```

### Fix 4: Remove pointers from data structures before freeing

```c
#include <stdlib.h>
#include <stdio.h>

typedef struct Node {
    int value;
    struct Node *next;
} Node;

void remove_node(Node **head, Node *target) {
    if (*head == target) {
        *head = target->next;
    } else {
        Node *curr = *head;
        while (curr && curr->next != target) {
            curr = curr->next;
        }
        if (curr) curr->next = target->next;
    }
    free(target);  /* safe — removed from list first */
}
```

## Examples

```c
#include <stdlib.h>
#include <stdio.h>

int main(void) {
    /* Invalid read after free */
    int *arr = malloc(sizeof(int) * 10);
    arr[0] = 100;
    free(arr);
    printf("%d\n", arr[0]);  /* use-after-free */

    /* Invalid write after free */
    int *p = malloc(sizeof(int));
    *p = 5;
    free(p);
    *p = 10;  /* use-after-free */

    return 0;
}
```

## Debugging Tips

```bash
# Valgrind catches use-after-free
gcc -g -o myprogram myprogram.c
valgrind --leak-check=full --track-origins=yes ./myprogram

# AddressSanitizer gives precise reports
gcc -fsanitize=address -g -o myprogram myprogram.c
./myprogram
```

## Related Errors

- [Segmentation Fault (Core Dumped)]({{< relref "/languages/c/segfault" >}}) — often the visible symptom of use-after-free
- [Double Free or Corruption]({{< relref "/languages/c/double-free" >}}) — freeing the same pointer twice
- [Memory Leak: Valgrind Lost Bytes]({{< relref "/languages/c/memory-leak" >}}) — forgetting to free memory
