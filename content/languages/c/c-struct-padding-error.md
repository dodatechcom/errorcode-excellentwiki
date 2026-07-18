---
title: "[Solution] C Struct Padding Error — How to Fix"
description: "Fix C struct padding and alignment errors causing serialization mismatches and unexpected sizeof values."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Struct Padding Error — How to Fix

C compilers insert padding bytes between struct members to satisfy alignment requirements. Common errors include assuming sizeof(struct) equals the sum of member sizes, writing struct padding to files, and comparing serialized structs across platforms. Padding is determined by the compiler and target architecture.

## Common Error Messages

- `sizeof(struct) larger than expected due to padding`
- `Serialization includes padding bytes — file format mismatch`
- `Struct layout differs between 32-bit and 64-bit`
- `Padding causes memcmp to return non-zero for equivalent structs`

## How to Fix It

### Check struct size with sizeof

```c
#include <stdio.h>

typedef struct { char a; int b; char c; } Padded;
typedef struct { int b; char a; char c; } Reordered;

int main(void) {
    printf("sizeof(Padded): %zu\n", sizeof(Padded));
    printf("sizeof(Reordered): %zu\n", sizeof(Reordered));
    return 0;
}
```

### Remove padding with pragma pack

```c
#include <stdio.h>

#pragma pack(push, 1)
typedef struct { char a; int b; char c; } __attribute__((packed)) Packed;
#pragma pack(pop)

int main(void) {
    printf("sizeof(Packed): %zu\n", sizeof(Packed));
    return 0;
}
```

### Serialize individual fields, not raw struct bytes

```c
#include <stdio.h>

typedef struct { char a; int b; char c; } Data;

int serialize_data(FILE *fp, const Data *d) {
    if (fwrite(&d->a, sizeof(d->a), 1, fp) != 1) return -1;
    if (fwrite(&d->b, sizeof(d->b), 1, fp) != 1) return -1;
    if (fwrite(&d->c, sizeof(d->c), 1, fp) != 1) return -1;
    return 0;
}
```

### Reorder members to minimize padding

```c
#include <stdio.h>

typedef struct { char a; int b; char c; } Bad;
typedef struct { int b; char a; char c; } Good;

int main(void) {
    printf("Bad: %zu bytes\n", sizeof(Bad));
    printf("Good: %zu bytes\n", sizeof(Good));
    return 0;
}
```

## Common Scenarios

### Scenario 1: Assuming sizeof(struct) equals the sum of all member sizes

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Writing raw struct bytes to a file and reading back on different architecture

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Using memcmp to compare structs with different padding content

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Use sizeof and offsetof to understand struct layout on your target
- **Tip 2:** Reorder struct members from largest to smallest to minimize padding
- **Tip 3:** Serialize individual fields instead of writing raw struct bytes
