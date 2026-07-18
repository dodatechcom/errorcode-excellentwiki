---
title: "[Solution] C strncat Error — How to Fix"
description: "Fix C strncat buffer overflows, off-by-one errors, and incorrect size arguments for safe concatenation."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C strncat Error — How to Fix

The `strncat` function appends at most n characters from the source to the destination. Common errors include passing `sizeof(buf)` as the size limit instead of the remaining space, which allows the total string to exceed the buffer. Not ensuring null termination before calling `strncat` also leads to undefined behavior.

## Common Error Messages

- `strncat buffer overflow — destination too small`
- `Stack smashing detected from strncat with wrong size`
- `strncat: no null terminator in destination`
- `Buffer overread from strncat with incorrect length`

## How to Fix It

### Calculate remaining space before strncat

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char buf[20] = "Hello";
    size_t remaining = sizeof(buf) - strlen(buf) - 1;
    strncat(buf, ", World!", remaining);
    printf("%s\n", buf);
    return 0;
}
```

### Use snprintf for safer concatenation

```c
#include <stdio.h>

int main(void) {
    char buf[20] = "Hello";
    snprintf(buf + strlen(buf), sizeof(buf) - strlen(buf), "%s", ", World!");
    printf("%s\n", buf);
    return 0;
}
```

### Create a safe strncat wrapper

```c
#include <string.h>

void safe_strncat(char *dst, const char *src, size_t dst_size) {
    size_t dst_len = strlen(dst);
    if (dst_len >= dst_size - 1) return;
    strncat(dst, src, dst_size - dst_len - 1);
}
```

### Ensure null termination before strncat

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char buf[20];
    buf[0] = '\0';
    strncat(buf, "Hello", sizeof(buf) - 1);
    strncat(buf, " World", sizeof(buf) - strlen(buf) - 1);
    printf("%s\n", buf);
    return 0;
}
```

## Common Scenarios

### Scenario 1: Passing sizeof(buf) as the count parameter instead of remaining space

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Assuming strncat appends at most n bytes including the null terminator

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Using strncat on a buffer that was not initialized or null-terminated

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always compute remaining space as sizeof(buf) - strlen(buf) - 1
- **Tip 2:** Consider snprintf for concatenation to avoid manual size tracking
- **Tip 3:** Verify the destination buffer has a null terminator before any string operation
