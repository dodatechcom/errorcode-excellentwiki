---
title: "[Solution] C offsetof Error — How to Fix"
description: "Fix C offsetof macro errors including use on non-standard-layout types and incorrect member access."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C offsetof Error — How to Fix

offsetof returns byte offset of a struct member. Common errors include using on non-standard-layout types, packed structs, and incorrect member access via the calculated offset.

## Common Error Messages

- `offsetof applied to non-standard-layout type`
- `Undefined behavior from offsetof on packed struct`
- `Invalid member name in offsetof`
- `Offset wrong due to compiler padding`

## How to Fix It

### Use with standard structs

```c
#include <stddef.h>
#include <stdio.h>
typedef struct { int x; double y; char z[16]; } MyStruct;
int main(void) {
    printf("offset x: %zu\n", offsetof(MyStruct, x));
    printf("offset y: %zu\n", offsetof(MyStruct, y));
    printf("offset z: %zu\n", offsetof(MyStruct, z));
    return 0;
}
```

### Alternative with pointer arithmetic

```c
#include <stdio.h>
typedef struct { char a; int b; char c; } Packed;
int main(void) {
    Packed p;
    size_t off = (char *)&p.b - (char *)&p;
    printf("offset of b: %zu\n", off);
    return 0;
}
```

### Access via offset

```c
#include <stddef.h>
typedef struct { int id; char name[32]; double score; } Record;
Record r = {1, "Alice", 95.5};
double *score = (double *)((char *)&r + offsetof(Record, score));
printf("Score: %f\n", *score);
```

### container_of macro

```c
#include <stddef.h>
struct list_head { struct list_head *next, *prev; };
#define container_of(ptr, type, member) \
    ((type *)((char *)(ptr) - offsetof(type, member)))
typedef struct { int data; struct list_head node; } Item;
```

## Common Scenarios

### Scenario 1: Using offsetof on struct with bit-fields

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Casting offset result without correct pointer type

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Using offsetof with flexible array members

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Only use offsetof with standard-layout structs
- **Tip 2:** Cast base+offset to correct member type
- **Tip 3:** Use container_of for linked list implementations
