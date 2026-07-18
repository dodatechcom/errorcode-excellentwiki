---
title: "[Solution] C fseek Error — How to Fix"
description: "Fix C fseek errors including invalid whence values, seeking on non-seekable streams, and offset overflow."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C fseek Error — How to Fix

The `fseek` function can fail when the file descriptor is not seekable (e.g., pipes, sockets), when the offset causes overflow, or when the whence parameter is invalid. Common mistakes include using SEEK_CUR without clearing the error indicator and not checking the return value.

## Common Error Messages

- `fseek: Invalid argument — non-seekable stream`
- `fseek fails on pipe or socket file descriptor`
- `ftell returns -1 after fseek — stream state corrupted`
- `fseek offset overflow on 32-bit systems`

## How to Fix It

### Check fseek return value before ftell

```c
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("data.txt", "r");
    if (!fp) return 1;
    if (fseek(fp, 0, SEEK_END) != 0) {
        fprintf(stderr, "fseek failed\n");
        fclose(fp); return 1;
    }
    long size = ftell(fp);
    printf("File size: %ld bytes\n", size);
    fclose(fp);
    return 0;
}
```

### Verify seek position with ftell

```c
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("data.txt", "r");
    if (!fp) return 1;
    fseek(fp, 10, SEEK_SET);
    long pos = ftell(fp);
    if (pos == -1)
        fprintf(stderr, "ftell failed\n");
    else
        printf("Position: %ld\n", pos);
    fclose(fp);
    return 0;
}
```

### Handle non-seekable streams

```c
#include <stdio.h>

int seekable(FILE *fp) {
    long pos = ftell(fp);
    if (pos == -1) return 0;
    if (fseek(fp, 0, SEEK_CUR) != 0) return 0;
    return 1;
}

int main(void) {
    if (seekable(stdin))
        printf("stdin is seekable\n");
    else
        printf("stdin is not seekable\n");
    return 0;
}
```

### Use fseeko for large file support

```c
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("large.bin", "rb");
    if (!fp) return 1;
    if (fseeko(fp, (off_t)1 << 32, SEEK_SET) != 0) {
        fprintf(stderr, "fseeko failed\n");
        fclose(fp); return 1;
    }
    off_t pos = ftello(fp);
    printf("Position: %lld\n", (long long)pos);
    fclose(fp);
    return 0;
}
```

## Common Scenarios

### Scenario 1: Calling fseek without checking the return value, then using an invalid file position

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Seeking on a non-seekable file descriptor like a pipe or socket

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Using fseek instead of fseeko for files larger than 2 GB on 32-bit long systems

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always check fseek return value before calling ftell or fread
- **Tip 2:** Test if a stream is seekable before calling fseek on it
- **Tip 3:** Use fseeko/ftello for large file support on systems with 32-bit long
