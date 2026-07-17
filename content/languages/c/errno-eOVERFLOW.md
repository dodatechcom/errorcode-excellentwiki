---
title: "[Solution] C errno EOVERFLOW — Value too large for defined data type Fix"
description: "Fix C EOVERFLOW (Value too large for defined data type) by using large file support, _FILE_OFFSET_BITS, and appropriate types."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EOVERFLOW — Value too large for defined data type Fix

When a system call returns a value that exceeds the range of the data type used to store it (e.g., a file offset exceeding 32-bit `off_t`), the call fails and sets `errno` to `EOVERFLOW`. This commonly occurs with files larger than 2 GB on 32-bit systems without large file support.

## Common Causes

- File size exceeds the range of 32-bit `off_t` (files > 2 GB).
- A file's inode number or block count exceeds the representable range.
- Using `_FILE_OFFSET_BITS=32` or compiling without large file support.
- `stat()` fails on files with very large inode numbers on 32-bit systems.

## How to Fix

Define `_FILE_OFFSET_BITS=64` before including any headers to use 64-bit file offsets on all platforms.

```c
#define _FILE_OFFSET_BITS 64
#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct stat st;
    if (stat("largefile.bin", &st) == -1) {
        if (errno == EOVERFLOW) {
            fprintf(stderr, "File too large for stat — recompile with _FILE_OFFSET_BITS=64\n");
        } else {
            perror("stat");
        }
        return 1;
    }
    printf("File size: %ld bytes\n", (long)st.st_size);
    return 0;
}
```

## Examples

Stat on a large file without large file support:

```c
// Compile with: gcc -m32 -o test test.c (without _FILE_OFFSET_BITS=64)
#include <sys/stat.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct stat st;
    if (stat("largefile.bin", &st) == -1) {
        if (errno == EOVERFLOW) {
            fprintf(stderr, "EOVERFLOW: value too large\n");
        }
    }
    return 0;
}
```

## Related Errors

- [errno-75 EOVERFLOW]({{< relref "/languages/c/errno-eOVERFLOW" >}}) — value too large for defined data type (numeric).
- [errno-22 EINVAL](/languages/c/errno-eOVERFLOW/) — invalid argument.
- [errno-27 EFBIG](/languages/c/errno-eOVERFLOW/) — file too large.
