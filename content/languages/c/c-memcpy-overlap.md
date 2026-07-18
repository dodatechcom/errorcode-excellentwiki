---
title: "[Solution] C memcpy Overlap Error — How to Fix"
description: "Fix C memcpy undefined behavior from overlapping memory regions. Learn when to use memmove instead."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C memcpy Overlap Error — How to Fix

The C standard specifies that `memcpy` has undefined behavior when the source and destination memory regions overlap. When buffers overlap, `memcpy` may read from or write to addresses that have already been modified, producing corrupted data. The correct function for overlapping regions is `memmove`, which handles overlaps by copying in the appropriate direction.

## Common Error Messages

- `Segmentation fault from overlapping memcpy`
- `memcpy causes data corruption with overlapping buffers`
- `Source and destination overlap in memcpy`
- `Undefined behavior detected in memcpy`

## How to Fix It

### Use memmove for overlapping regions

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char buf[] = "Hello, World!";
    memmove(buf + 2, buf, 10);
    printf("%s\n", buf);
    return 0;
}
```

### Detect overlap before copying

```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool overlaps(const void *src, size_t src_len, const void *dst, size_t dst_len) {
    const char *s = (const char *)src;
    const char *d = (const char *)dst;
    return (s < d && s + src_len > d) || (d < s && d + dst_len > s);
}

int main(void) {
    char buf[] = "Hello, World!";
    if (overlaps(buf, 10, buf + 2, 10))
        memmove(buf + 2, buf, 10);
    else
        memcpy(buf + 2, buf, 10);
    printf("%s\n", buf);
    return 0;
}
```

### Use safe_memcpy wrapper

```c
#include <string.h>

void *safe_memcpy(void *dst, const void *src, size_t n) {
    if (dst == src || n == 0) return dst;
    if (src < dst && (const char *)src + n > (const char *)dst)
        return memmove(dst, src, n);
    return memcpy(dst, src, n);
}
```

### Compile with AddressSanitizer to detect overlap

```bash
gcc -fsanitize=address -g -o program program.c
./program
```

## Common Scenarios

### Scenario 1: Shifting elements within an array using memcpy instead of memmove

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Copying a substring within the same buffer using memcpy

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Implementing a ring buffer with memcpy on overlapping regions

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Default to memmove when unsure about overlap — it is only slightly slower than memcpy
- **Tip 2:** Enable -fsanitize=address during development to catch overlap bugs at runtime
- **Tip 3:** Use compiler intrinsics like __builtin_memmove for performance-critical overlapping copies
