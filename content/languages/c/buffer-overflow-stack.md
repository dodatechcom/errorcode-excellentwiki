---
title: "[Solution] C Stack smashing detected — buffer overflow"
description: "Fix C stack buffer overflow (stack smashing). Prevent stack-based buffer overflows with bounds checking."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["stack-smashing", "buffer-overflow", "stack", "canary", "security"]
weight: 5
---

# Stack smashing detected — buffer overflow

"Stack smashing detected" occurs when a buffer overflow overwrites the stack canary (a guard value placed between local variables and the return address). The program aborts when it detects the canary has been corrupted.

## Common Causes

```c
// Cause 1: Writing past array bounds
char buf[10];
strcpy(buf, "this string is way too long"); // overflow

// Cause 2: Gets() with no bounds checking
char buf[100];
gets(buf); // dangerous — no length limit

// Cause 3: Wrong buffer size in memcpy
int arr[5];
memcpy(arr, large_data, 100 * sizeof(int)); // overflow
```

## How to Fix

### Fix 1: Use bounds-checked functions

```c
// Instead of strcpy
strncpy(buf, src, sizeof(buf) - 1);
buf[sizeof(buf) - 1] = '\0';

// Instead of gets
fgets(buf, sizeof(buf), stdin);
```

### Fix 2: Validate buffer sizes

```c
void copy_string(char *dest, size_t dest_size, const char *src) {
    if (dest_size == 0) return;
    size_t i;
    for (i = 0; i < dest_size - 1 && src[i] != '\0'; i++) {
        dest[i] = src[i];
    }
    dest[i] = '\0';
}
```

### Fix 3: Compile with stack protection

```bash
gcc -fstack-protector-strong -o prog prog.c
```

## Examples

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char buf[20];
    
    // Safe: use fgets
    printf("Enter name: ");
    fgets(buf, sizeof(buf), stdin);
    
    // Remove trailing newline
    buf[strcspn(buf, "\n")] = '\0';
    
    printf("Hello, %s\n", buf);
    return 0;
}
```

## Related Errors

- [Buffer overflow on stack]({{< relref "/languages/c/buffer-overflow-stack" >}}) — stack overflow details.
- [Use after free]({{< relref "/languages/c/use-after-free-heap" >}}) — heap memory error.
- [Segfault at 0x0]({{< relref "/languages/c/segmentation-fault-0" >}}) — null pointer crash.
