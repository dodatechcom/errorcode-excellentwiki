---
title: "[Solution] C String Length Error — How to Fix"
description: "Fix C string length errors including off-by-one, missing null terminator, and buffer overflows with strlen."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C String Length Error — How to Fix

String length errors occur when the null terminator is missing, the wrong buffer size is used, or `strlen` is applied to non-null-terminated data. Off-by-one errors in buffer allocation are extremely common — allocating `strlen(s)` bytes instead of `strlen(s) + 1` leaves no room for the terminator.

## Common Error Messages

- `strlen returns unexpected value — missing null terminator`
- `Stack buffer overflow from off-by-one in string allocation`
- `Segmentation fault in strlen — string not null-terminated`
- `Use of strlen result without accounting for null terminator`

## How to Fix It

### Always allocate strlen(s) + 1 bytes

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void) {
    const char *src = "Hello";
    size_t len = strlen(src);
    char *copy = malloc(len + 1);
    if (!copy) return 1;
    memcpy(copy, src, len + 1);
    printf("%s\n", copy);
    free(copy);
    return 0;
}
```

### Ensure null termination after strncpy

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char buf[16];
    strncpy(buf, "Hello, World!", sizeof(buf) - 1);
    buf[sizeof(buf) - 1] = '\0';
    printf("%s\n", buf);
    return 0;
}
```

### Use strnlen to bound searches

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char buf[16] = {0};
    buf[0] = 'H'; buf[1] = 'i';
    size_t len = strnlen(buf, sizeof(buf));
    printf("Length: %zu\n", len);
    return 0;
}
```

### Validate length before copying

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    const char *input = "long untrusted string";
    char buf[10];
    size_t copy_len = sizeof(buf) - 1;
    if (strlen(input) < copy_len) copy_len = strlen(input);
    memcpy(buf, input, copy_len);
    buf[copy_len] = '\0';
    printf("%s\n", buf);
    return 0;
}
```

## Common Scenarios

### Scenario 1: Allocating strlen(s) instead of strlen(s)+1 before strcpy

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Using strlen on a buffer that contains embedded null bytes

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Comparing string lengths to sizeof() instead of strlen()

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always add +1 for the null terminator when allocating for a C string copy
- **Tip 2:** Use strnlen when reading from untrusted or network-supplied buffers
- **Tip 3:** Enable compiler warnings with -Wstringop-overflow to catch length miscalculations
