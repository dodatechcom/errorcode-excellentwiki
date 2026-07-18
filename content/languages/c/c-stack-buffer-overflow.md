---
title: "[Solution] C Stack Buffer Overflow Error — How to Fix"
description: "Fix C stack buffer overflow vulnerabilities from writing past array bounds. Prevent stack smashing."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C Stack Buffer Overflow Error — How to Fix

Stack buffer overflows occur when writing beyond a stack-allocated array, corrupting return addresses. Common causes include gets(), unbounded strcpy/sprintf, and missing bounds checks on array indices.

## Common Error Messages

- `*** stack smashing detected ***: terminated`
- `Segmentation fault from stack corruption`
- `Stack buffer-overflow detected by ASan`
- `SIGABRT after buffer overflow`

## How to Fix It

### Use bounded string functions

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char buf[32];
    snprintf(buf, sizeof(buf), "%s", "Hello, World!");
    printf("%s\n", buf);
    return 0;
}
```

### Validate array bounds

```c
#include <stdio.h>

void set_value(int *arr, size_t len, size_t idx, int val) {
    if (idx < len) arr[idx] = val;
    else fprintf(stderr, "Index out of bounds\n");
}

int main(void) {
    int arr[5] = {0};
    set_value(arr, 5, 2, 42);
    return 0;
}
```

### Enable stack protection

```bash
gcc -fstack-protector-strong -o program program.c
```

### Use AddressSanitizer

```bash
gcc -fsanitize=address -g -o program program.c
```

## Common Scenarios

### Scenario 1: Using gets() or unbounded strcpy with user input

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Off-by-one error writing past array bounds

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Format string vulnerability causing stack corruption

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Never use gets() -- use fgets() with size limit
- **Tip 2:** Compile with -fstack-protector-strong
- **Tip 3:** Use -fsanitize=address during development
